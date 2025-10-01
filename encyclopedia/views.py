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



def get_entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return HttpResponse("<h1>Page does not exist. </h1>", status=404)
    html_content = markdown2.markdown(content)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })

def search_entry(request):
    search_query = request.GET.get('q', '').lower()
    all_entries = util.list_entries()

    for entry in all_entries:
        if entry.lower() == search_query:
            return redirect('encyclopedia:get_entry', title=entry)

    matching_result = [entry for entry in all_entries if search_query in entry.lower()]
    return render(request, "encyclopedia/search.html", {
        "results": matching_result,
        "search_query": search_query
    })

def create_entry(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title) is not None:
                return render(request, "encyclopedia/create.html", {
                    "form": form,
                    "error": "An entry with this title already exists."
                })
            util.save_entry(title, content)
            return redirect('encyclopedia:get_entry', title=title)
    else:
        form = EntryForm()
    return render(request, "encyclopedia/create.html", {
        "form": form
    })