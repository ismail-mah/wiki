import os
import markdown2
from django.shortcuts import render
from django.http import Http404

ENTRIES_DIR = os.path.join(os.path.dirname(__file__), "entries")

# <-- ADD THIS function so "index" exists
def index(request):
    entries = [
        f[:-3] for f in os.listdir(ENTRIES_DIR)
        if f.endswith(".md")
    ]
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

# This one shows a single entry
def entry(request, title):
    filename = os.path.join(ENTRIES_DIR, f"{title}.md")
    if not os.path.exists(filename):
        raise Http404("Entry not found")
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    html_content = markdown2.markdown(content)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })
