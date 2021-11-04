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
1.    <code>python -m install virtualenv</code> or <code>pip install virtualenv</code> 
&nbsp;
3.    <code>virtualenv (environment_name)</code>
&nbsp;
5.    <code>environment_name\Scripts\activate</code>
&nbsp;

## Run Project
1.  <code>First Locate to project folder in cmd with virtual environment running</code>
&nbsp;
2.  <code>pip install -r requirements.txt</code>
&nbsp;
3.  <code>python manage.py makemigrations</code>
&nbsp;
4.  <code>python manage.py migrate</code>
&nbsp;
5.  <code>python manage.py createsuperuser</code>
&nbsp;
6.  <code>python manage.py runserver</code>

Paste this <code>127.0.0.1:8000</code> IP Address on any browser and it will start.<code>127.0.0.1:8000/admin</code> and enter your superuser's username/pass for django admin panel access
