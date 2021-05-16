# porfolio-api 

## Checks

- [x] Validations like “quantity of a stock should always be positive” should be in place.
- [x] API routes should be well documented.
- [x] Demo should be hosted somewhere (AWS, Heroku, etc.)


## Additional Things

- [x] Pagination to API
- [x] Test case for Login, Model and RestAPI separately.
- [x] test API through curl file.
- [x] API documentation automatically generated through redoc.
- [x] code comment for developer.
- [x] sqlite database support for localhost.


## Technology Stack


### Database

Production: Postgresql

LocalHost: sqllite


### Backend Framework

Django

### Platform as a Service

Heroku


## Test Credits

<b> Username: </b> vishal
<b> Password: </b> 123456

## How to Create virtual env

It always better to create virtual environment for development.

Create virtual environment through given commands.

```
virtualenv <env_name>
source <env_name>/bin/activate
```

Deactivate virtualenv through following command

```
deactivate
```

## How to start project on localhost

First step, install pip packages through following command.

```
pip install -r requirements.txt
```

Second step, follow note step given as subheading below.

Final step, run following command to start django server.

```
python manage.py runserver
```


### Note

If you want to run this project on localhost, then comment production database setting and uncomment localhost database setting inside 'portfolioapi/settings.py' file. Comments have been added to the file.

## Admin area

You can access django admin area by adding '/admin/' to host url, e.g 'https://<domain_name>/admin/'


## Test Command

Test folder structure:


- trade
  -- tests
    --- __init__.py
    --- test_login.py
    --- test_model.py
    --- test_restapi.py


Total unit test case: 9


```

python manage.py test

```

## Note

Postman can also be used to check API response with different values

## Bash Script

Location: test.sh
 
Run: 'bash test.sh'

Note: If script give 500 status code on terminal, then there is some problem with database connection, please verify it inside the file having location 'portfolioapi/settings.py'.


## Author

Vishal Sharma

## Email Address

vishalsharma.gbpecdelhi@gmail.com
