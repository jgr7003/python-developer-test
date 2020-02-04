# https://www.django-rest-framework.org/api-guide/serializers/
from bank.models import Client, Account, Movements, AuditClient
from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from django.utils.translation import ugettext_lazy as _


class AuditClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditClient
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ['current_date']
        validators = [
            UniqueTogetherValidator(
                queryset=Client.objects.all(),
                fields=['type_identification', 'number_identification']
            )
        ]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        audit_serializer = AuditClientSerializer(
            AuditClient.objects.filter(client_id=instance.id).order_by('current_date'),
            many=True
        )
        ret['audit'] = audit_serializer.data
        return ret


class AccountSerializer(serializers.ModelSerializer):
    number = serializers.CharField(
        max_length=250,
        validators=[UniqueValidator(queryset=Account.objects.all())]
    )
    
    class Meta:
        model = Account
        fields = '__all__'
        read_only_fields = ['current_date']

    def to_representation(self, instance):
        return super().to_representation()


class MovementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movements
        fields = '__all__'

    def to_movement(self, obj):
        return {
            'id_movement': obj.id,
            'value': obj.value,
        }

    def to_internal_value(self, data):
        try:
            try:
                obj_value = data['value']
                obj_id = data['id_movement']
                if obj_value > 0:
                    return Movements.objects.get(id=obj_id)
            except KeyError:
                raise serializers.ValidationError(
                    'id is a required field.'
                )
            except ValueError:
                raise serializers.ValidationError(
                    'id must be an integer.'
                )
        except Movements.DoesNotExist:
            raise serializers.ValidationError(
                'Obj does not exist.'
            )


