Teck Books 📚
-----

## Introduction

Free Tech Books Market

This site lists free download computer science, engineering and programming books, textbooks and lecture notes, cheat sheet, all of which are legally and freely available.

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
pip install 
autopep8==1.6.0
click==8.0.4
colorama==0.4.4
dnspython==2.2.1
email-validator==1.1.3
Flask==2.0.3
Flask-SQLAlchemy==2.5.1
Flask-WTF==1.0.0
greenlet==1.1.2
idna==3.3
itsdangerous==2.1.2
Jinja2==3.1.1
MarkupSafe==2.1.1
pycodestyle==2.8.0
SQLAlchemy==1.4.32
toml==0.10.2
Werkzeug==2.0.3
WTForms==3.0.1
```

### 2. Frontend Dependencies
You must have the **HTML**, **CSS**, with [Bootstrap 4](https://getbootstrap.com/) for our website's frontend. 


## Main Files: Project Structure

```sh
├── README.md
├── run.py *** the main driver of the app. 
                  "python run.py" to run after installing dependences
├── forms.py *** Your forms
├── models.py *** Your ORM
├── requirements.txt *** The dependencies we need to install with "pip3 install -r requirements.txt"
├── static
│   ├── icon 
│   ├── images
├── templates
    ├── add-book
    ├── base
    ├── home
    ├── login
    ├── market
    └── register
```

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