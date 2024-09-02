# python-developer-test
Python developer test

## Introduction

This is the basic apis to administer a bank, follow the installation instructions and latter initialize the test.

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

1. Add a unique key to the Client model: Include a unique key composed of the identification type and identification number in the Client model (1 point).
2. Modify the foreign key in the Account model: Adjust the foreign key referencing the client in the Account model to restrict cascade deletion (1 point).
3. Add an index to the number field in the Account model: Create an index for the number field in the Account model (1 point).
4. Include user accounts in the Client representation: Add the user accounts to the to_representation method in the ClientSerializer (3 points).
5. Modify the MovementsSerializer to validate transaction values: Ensure that the MovementsSerializer only accepts transaction values greater than 0 (1 point).\
6. Add filters using Django filters:
    Filter by identification number in ClientViewSet (1 point).
    Filter by client identification number in AccountViewSet (1 point).
    Filter by account number in MovementsViewSet (1 point).
7. Modify the MovementSerializer to adjust the account balance:
    Add deposits to the balance (2 points).
    Subtract withdrawals from the balance "if the balance is less than zero, indicate that the transaction cannot be processed" (2 points).
    Subtract sent transfers from the balance "if the balance is less than zero, indicate that the transaction cannot be processed" (3 points).
    Add received transfers to the balance (2 points).
    Deduct 4 units for every 1000 in case of sending a transfer or making a withdrawal (3 points).
    Implement an audit system for balance changes: Develop an audit system to track balance changes in the account, using the existing client audit system as a reference (3 points).
    5. 4 * 1000 in case of sending transfer or making a withdrawal, deduct 4 for each 1000 (3 points)
8. Implement an audit system to bring balance changes to the account "you can be guided by the one that exists to carry out the client's audit" (3 points)
