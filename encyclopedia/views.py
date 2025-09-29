from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
import markdown2
from random import choice
from . import util


class EntryForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea(), label="content")

class EditEntry(forms.Form):
    content = forms.CharField(widget=forms.Textarea(), label="content")


def index(request):
    try:
        entries = util.list_entries()
        
    except FileNotFoundError:
        entries = [] 
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })


# def entry(request, title):
#     content = util.load_page(title)
#     if content is None:
#         return render(request, "encyclopedia/error.html", {
#             "message": "The requested page was not found."
#         })
#     else:
#         html_content = markdown2.markdown(content)
#         return render(request, "encyclopedia/entry.html", {
#             "title": title,
#             "content": html_content
#         })

def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return HttpResponse("<h1>Page does not exist. </h1>", status=404)
    html_content = markdown2.markdown(content)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })       