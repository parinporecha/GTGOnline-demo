This is a demo for the online version of GTG.
The demo uses Django framework and MySQL database.

To run it on your local machine, follow these steps -
1) Change the mysql username and password in 'Inception/settings.py' to the one which you use other than root.
2) Create a new database 'demo'
3) Run the command - 'python manage.py syncdb'

Now, the application has been installed on your machine and you can start the development server by - 'python manage.py runserver'
It will be deployed at localhost:8000/demo
