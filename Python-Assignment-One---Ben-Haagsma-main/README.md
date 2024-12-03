Assignment-One

Repo for the first assignment for my Advanced Python Course

This project is a basic django project which has the following features: 
1. a basic index page at the "/" route 
2. a super user setup 
3. the default sql-lite database connected 
4. a very basic testing suite setup

To run the project on your own machine do the following 

1. download the code 
2. run pip install -r requirements.txt 
3. run python manage.py migrate to handle any migrations if needed 
4. run the server with python manage.py runserver 
5. you can also run the pytest test using the command "pytest"
6. also dont forget you need to have the venv activated to run the pytest command!
7. you must also be in the myworld/my_project/ directory (the one which contains the manage.py file)

