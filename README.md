# DJANGO API

A demo api includes REST and GraphQL

### Project setup (Windows)

1. starting a project

    ```
    mkdir django_api
    cd django_api
    activate py36
    
    # main framework
    pip install django
    
    # REST
    pip install djangorestframework
    
    # GQL
    pip install graphene_django
    
    # please replace below directory to yours
    python C:\Users\xy\Anaconda3\envs\py36\Lib\site-packages\django\bin\django-admin.py startproject django_api
    ```

1. create API app

    ```
    python manage.py startapp rest_dailycompleteness
    python manage.py startapp gql_toymodels
    ```

1. add frameworks and apps into django_api/settings.py

    ```
    INSTALLED_APPS = [
        ...
        
        'rest_framework',                       # REST framework
        'graphene_django',                      # GQL framework
        
        'django_api.rest_dailycompleteness,     # dailycompleteness app
        'django_api.gql_toymodels',             # toymodels app
    ]
    ```

1. make project available on server

    ```
    ALLOWED_HOSTS = ['*']
    ```

1. production mode

    ```
    DEBUG = False
    ```

1. runserver

    ```
    python manage.py runserver
    ```
    
    or
    
    ```
    python manage.py runserver 10.144.64.68:8000  # replace host and port by yours
    ```


### REST API

##### structure

```
rest_dailycompleteness
    |__renderers.py         # custom renderer; currently works for exporting different file types
    |__models.py            # schema of returns 
    |__resolvers.py         # business logic
    |__urls.py              # REST urls patterns; linking above files all together

```

##### notes

1. the connector of Django framework and REST framework is ../rest_completeness/urls.py and ../urls.py;

1. ../urls.py uses `include` to import urls you written in ../rest_completeness

1. 

### GraphQL API

##### structure

```
rest_dailycompleteness
    |__models.py            # schema of returns 
    |__resolvers.py         # business logic
    |__schema.py            # GQL request schema; linking above files all together

```


##### notes

1. put GRAPHENE into `setting.py`:
    
    ```
    GRAPHENE = {
        'SCHEMA': 'django_api.schema.schema'
    }
    ```

1. the connector of Django framework and GQL framework is ../gql_models/schema.py, ../schema.py and ../urls.py

1. ../schema.py import all schemas no matter how many gql api you have


### Last

1. every time you add an API you always have to add it into setting.py INSTALLED_APPS

1. I wrote some functions in ../utils.py to make things easier, feel free to modify it
