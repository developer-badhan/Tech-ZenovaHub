# Zenova

![image alt](https://github.com/developer-badhan/Tech-ZenovaHub/blob/f8470a04922b68007e801afd20756ee73a05d42b/static/images/logo.png)

Zenova is a tech-driven e-commerce platform focused on **electrical** and **smart home** products. It's designed to be **fast**, **scalable**, and **user-friendly** — the go-to hub for future-ready solutions.This project is being developed using the **Django web framework**, and it's aimed at delivering a modern, intuitive experience for both customers and administrators.

---

## 🚀 Project Goals

- Provide a seamless shopping experience for users interested in smart home tech and electrical goods.
- Enable quick product browsing, searching, filtering, and secure purchasing.
- Build a responsive, clean, and modern UI with user-friendly navigation.

---

## 🔧 Tech Stack

- **Backend**: Django (Python) , Django-Rest_Framework(Python)
- **Frontend**: HTML, CSS (Bootstrap), Vanila JavaScript 
- **Database**: PostgreSQL

---

## 🛠️ Setup the Project

1) **Clone the Repository**

    => git clone https://github.com/developer-badhan/Zenova.git  
    => cd Zenova


2) **Open Terminal in VS Code**

    => ctrl + shift + ` (Window)

    => Cmd + Shift + `` (Mac)


3) **Create Virtual Environment**

    => python -m venv venv (Window)

    => python3 -m venv venv


4) **Activate Virtual Environment**

    🪟Windows: => venv\Scripts\activate

    📠 Mac: => source venv/bin/activate


5) **Install All Dependencies**

    => pip install -r requirements.txt  (Windows)

    => pip3 install -r requirements.txt (Mac)


6) **Database Setup**

    => Open pgadmin 

    => Create database <name> 


7) **Add .env in root directory**

    => .env (attached all requirements) | for additional help , we provide .env.sample


8) **Makemigrations & Migare**

    => python manage.py makemigrations

    => python manage.py migrate

    (If on Mac, use python3 instead of python if needed.)


6) **Run the Project**

    => python manage.py runserver

7) **Open the url in browser**

    => http://127.0.0.1:8000/


