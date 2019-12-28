## Tasks Project  


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
`$: python3 manage.py migrate tasks`  
`$: python3 manage.py migrate`  

## Load Initial Data  
`$: python3 manage.py loaddata user_data.json`  
`$: python3 manage.py loaddata user_data.json`    
