Teck Books 📚
-----

## Introduction

Free technology Books Market

This site lists free download computer science, software engineer and programming books, textbooks and lecture notes, cheat sheet, all of which are freely available.

Full stack flask project.


## Tech Stack (Dependencies)

### 1. Backend Dependencies
Our tech stack will include the following:
* **virtualenv** as a tool to create isolated Python environments
* **Python3** and **Flask** as our server language and server framework
* **SQLAlchemy ORM** to be our ORM library of choice
* **SQLite** as our database of choice
* You can download and install the dependencies mentioned above using `pip` as:
```
alembic          1.8.1  
autopep8         1.6.0  
bcrypt           4.0.0  
click            8.1.3  
colorama         0.4.5  
dnspython        2.2.1  
email-validator  1.3.0  
Flask            2.0.3  
Flask-Admin      1.6.0
Flask-Bcrypt     1.0.0
Flask-Login      0.6.0
Flask-Migrate    3.1.0
Flask-SQLAlchemy 2.5.1
Flask-WTF        1.0.0
greenlet         1.1.3
idna             3.4  
itsdangerous     2.1.2
Jinja2           3.1.2
Mako             1.2.3
MarkupSafe       2.1.1
pip              22.2.2
psycopg2         2.9.3
pycodestyle      2.9.1
setuptools       58.1.0
SQLAlchemy       1.4.41
toml             0.10.2
Werkzeug         2.2.2
WTForms          3.0.1
```

### 2. Frontend Dependencies
You must have the **HTML**, **CSS**, with [Bootstrap 4](https://getbootstrap.com/) for our website's frontend. 


## Development Setup

1. **Initialize and activate a virtualenv using:**
```
py -3 -m venv venv 
source app\Scripts\activate.bat
```

2. **Install the dependencies:**
```
pip install -r requirements.txt
```

3. **Run the development server:**
```
In Bash
export FLASK_APP=myapp
export FLASK_ENV=development # enables debug mode
flask run --reload 

In Windows
set FLASK_APP=myapp
set FLASK_ENV=development # enables debug mode
flask run --reload 
```

4. **Verify on the Browser**<br>
Navigate to project homepage [http://127.0.0.1:5000/](http://127.0.0.1:5000/) or [http://localhost:5000](http://localhost:5000) 


## Screenshots

### Home page 

![](./static/images/screenshots/home.png)


### Market page 

![](./static/images/screenshots/market.png)

### Register page 

![](./static/images/screenshots/register.png)

### Login page 

![](./static/images/screenshots/login.png)