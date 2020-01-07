# python-developer-test
Python developer test

## Introduction

This is basic apis to administration a bank, follow the installation instructions and latter initialize the test.

## Installation 

The easiest install process, install first
[git](https://git-scm.com/downloads) and [docker](https://www.docker.com/get-started) in your system, latter continue with instructions.

Clone the repository:

```bash
$ git clone https://github.com/jgr7003/python-developer-test.git
```

Ingress to project directory: create a new branch and up the docker, wait while installing the container

```bash
$ cd python-developer-test/
$ git branch my_complete_name_branch
$ git checkout my_complete_name_branch 
$ docker-compose up &
```

This will start the server on port 8008, and bind it to all network
interfaces. You can then visit the site at http://localhost:8008/ (Windows) or 
http://0.0.0.0:8008 (Mac)

## Administrator user

```
user: admin
password: admin
```

# Test 

Please, when solving a question, leave a comment with the number of the result, for example:

```
# Solution 4
# Solution 6 (iii)
```

1. Add a unique key composed of the identification type and identification number in the client model (1 point)
2. Modify the foreign key of the client model with one that restricts cascade deletion (1 point)
3. Add an index for the number field in account model (1 point)
4. Add the user accounts in the client API response (3 points)
5. Modify the movement serializer so that only transaction values ​​greater than 0 are accepted (1 point)
6. Using Django filters, add the following filters:
    1. By identification number in the client API (1 point)
    2. By customer identification number in the account API (1 point)
    3. By account number in the movement API (1 point)
7. Modify the MovementViewSet, so that at the time of registering any transaction, modify the account balance according to the following instructions:
    1. Consignments add to the balance (2 points)
    2. Transfer sent subtracted from the balance "if the balance is less than zero, indicate that the transaction cannot be made" (3 points)
    3. Transfer received add to the balance (1 point)
    4. 4 * 1000 in case of sending transfer or making a withdrawal, deduct 4 for each 1000 (4 points)
    5. Withdrawals subtract from the balance "if the balance is less than zero, indicate that the transaction cannot be made" (2 points)
8. Modify the account serializer so that the last 10 movements of the account are sorted from the most current to the oldest (3 points)
9. Implement an audit system to bring balance changes to the account "you can be guided by the one that exists to carry out the client's audit" (3 points)