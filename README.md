# django-notesapp
Notes Sharing App using django(python framework)

# PREREQUISITES
1.  Python Version >> 3.7.8
2.  Virtualenv setup
  
 
Features
1. A registerd user can access all the notes shared/added by the admin
2. Can download the pdfs
3. can request specific notes
4. Admin can handle all the feattures like adding/updating/deleting the notes/users and can have overall control.
5. sqlite3 database

Give It 🌟 if u find it useful.

How to Run this project?

## Virtualenv Setup
&nbsp;
&nbsp;
1.    <code>python -m install virtualenv</code> or <code>pip install virtualenv</code> 
2.    <code>virtualenv (environment_name)</code>
3.    <code>environment_name\Scripts\activate</code>

## Run Project

1.  <code>First Locate to project folder in cmd with virtual environment running</code>
2.  <code>pip install -r requirements.txt</code>
3.  <code>python manage.py makemigrations</code>
4.  <code>python manage.py migrate</code>
5.  <code>python manage.py createsuperuser</code>
6.  <code>python manage.py runserver</code>

Paste this <code>127.0.0.1:8000</code> IP Address on any browser and it will start.

1.  <code>127.0.0.1:8000/admin</code> and enter your superuser's username/pass for django admin panel access
