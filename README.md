# CS50 Wiki

A simple Wikipedia-like encyclopedia built with Django. This is Project 1 of CS50 Web Programming with Python and JavaScript.

---

## What it does

You can create, edit, delete, and search encyclopedia entries. Entries are written in Markdown and rendered as HTML when you view them. There is also a random page button that takes you to a random entry.

---

## Tech stack

- Python 3.13
- Django 5.2
- Bootstrap 5.3
- markdown2

---

## Getting started

Clone the repo and navigate into it:

```bash
git clone https://github.com/your-username/wiki.git
cd wiki
```

Create and activate a virtual environment:

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
python manage.py runserver
```

Then open `http://127.0.0.1:8000` in your browser.

---

## Project structure

```
wiki/
├── encyclopedia/
│   ├── entries/        # Markdown files stored here
│   ├── static/
│   ├── templates/
│   ├── views.py
│   ├── urls.py
│   └── util.py
├── wiki/
│   ├── settings.py
│   └── urls.py
├── requirements.txt
├── manage.py
└── README.md
```

---

## Notes

- Entries are saved as .md files on disk
- Files are read as raw bytes and decoded as UTF-8, with a fallback to CP1252 for older Windows-encoded files
- The sidebar uses position sticky so it stays visible while scrolling

---

Built by Ismail M. Adam as part of CS50W — https://cs50.harvard.edu/web/