
# Sales Data Project

## Introduction

This System to trace the sales data and manipulating the data

## Technology Considerations
### Consideration1: Development 
    1. Programming Language                Python
    2. Version                             v3.10
    3. Framework                           Django
    5. IDE                                 Pycharm, Visual Studio Code
    
### Consideration2: Services Design

    1. Database                            sqlite3 

``` bash

├── salesdata
    ├── env 
       ├── account
            ├──migrations
                └──__init__.py
            ├──__init__.py
            ├──admin.py
            ├──apps.py
            ├──models.py
            ├──seriaalizer.py
            ├──tests.py         
            ├──urls.py
            ├──views.py 
       ── salesdata
            ├──__init__.py
            ├──asgi.py
            ├──sonstant.py
            ├──settings.py
            ├──urls.py
            ├──wsgi.py
    ├──manage.py
    ├──readme.md
    ├──Dockerfile
    ├──requirements.txt 
```
   
## Setup Instructions
__Steps__

1.  Install Required Packages for Server  
   
        sudo apt-get install python3  
        
        sudo apt-get install python3-pip python3-dev
        
        sudo pip3 install virtualenv
    

2. Django Environment Setup
    
        virtualenv -p python3 env_name 
        
        source env_name/bin/activate
        
        pip install -r requirements.txt

3. Run Server
    
        python manage.py makemigrations     # to migrate all the migrations

        python manage.py migrate            # to migrate all the migrations
         
        python manage.py runserver          # to run the server
