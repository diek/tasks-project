## Tasks Project  
Simple Learning project

## Tools Used
1. Python 3.7
2. Django 2.2.9
3. SQLite3


## Git Clone the project and cd into project 
Move to a working directory on your computer, and open terminal.   
`$: git clone git@github.com:diek/tasks-project.git`  
`$: cd tasks_project`  

## Create a venv and activate it  
`$: python3 -m venv _env`  
`$: source _env/bin/activate`  
`$: pip install --upgrade pip`  
`$: pip install -r requirements.txt`  

## Run migrations  
`$: python manage.py migrate tasks`  
`$: python manage.py migrate`  

## Load Initial Data  
`$: python manage.py loaddata user_data.json`  
`$: python manage.py loaddata task_data.json`    
