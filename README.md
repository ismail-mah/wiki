# CS50 Wiki

🔗 Live Demo: https://wiki-production-5c77.up.railway.app/

CS50 Wiki is a Wikipedia-like web application built using Django as part of Harvard’s CS50 Web Programming with Python and JavaScript course (Project 1).

It allows users to create, edit, search, and browse encyclopedia entries written in Markdown, which are dynamically rendered into HTML.

---

## 🚀 Features

- Create new encyclopedia entries
- Edit existing pages
- Delete entries
- Search functionality (partial match support)
- Random page navigation
- Markdown rendering to HTML
- Clean and responsive UI using Bootstrap

---

## 🛠️ Tech Stack

- Python 3.13
- Django 5.2
- Bootstrap 5.3
- markdown2
- HTML / CSS / JavaScript

---

## ⚙️ Installation & Setup

Clone the repository:

```bash
git clone https://github.com/ismail-mah/wiki.git
cd wiki
````

Create virtual environment:

```bash id="u2m8qp"
python -m venv venv
```

Activate it:

```bash id="9xk3rj"
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

Install dependencies:

```bash id="q1v7sd"
pip install -r requirements.txt
```

Run the project:

```bash id="m8p2wa"
python manage.py runserver
```

Open in browser:

```text id="t6k9ld"
http://127.0.0.1:8000
```

---

## 🌐 Deployment

Live application:

👉 [https://wiki-production-5c77.up.railway.app/](https://wiki-production-5c77.up.railway.app/)

Hosted using:

* Railway
* Gunicorn
* WhiteNoise

---

## 📌 Notes

* Entries are stored as `.md` files on disk
* Markdown is rendered using `markdown2`
* Sidebar uses sticky positioning for navigation
* UTF-8 decoding with fallback support for older encodings

---

## 🎓 About This Project

This project was built as part of **CS50 Web Programming with Python and JavaScript** by Harvard University.

Course link: [https://cs50.harvard.edu/web/](https://cs50.harvard.edu/web/)

---

## 👨‍💻 Author

Built by **Ismail M. Adam**

