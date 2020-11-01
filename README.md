# Project Name 
Hood

# Project Description 
- A web application that allows users to be in the loop about everything happening in their neighbourhood. From contact information of different handymen to meeting announcements or even alerts.

# Link to Live Project
- https://realhood343.herokuapp.com

# Author 
- [John Karima](https://github.com/JohnKarima)

# Setup Instructions 

### Cloning
```
$ git clone https://github.com/JohnKarima/hood
```
### Move into directory and install requirements
```
$ cd hood

$ pip install -r requirements.txt 
```
### Install and activate a Virtual Environment
```
$ python3 -m venv virtual 

$ source virtual/bin/activate  
```
### Set-up a Database
```
Set your database User and Password 
```
### Make Migrations & Migrate
```
$ python manage.py makemigrations <DB Name> 

$ python manage.py migrate 
```
### Run the application
```
python manage.py runserver 
```
### Run the test for the application
```
$ python3 manage.py test hoodapp
```

# Technologies Used
- Python
- Django
- Bootstrap
- pillow
- cloudinary
- crispy forms
- djangorestframework

# Contact Information
karimajohn24@gmail.com

# License Copyright 
- 2020, John Karima.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

