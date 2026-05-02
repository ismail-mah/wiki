import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def list_entries():
    try:
        dirs, files = default_storage.listdir("entries")
    except Exception:
        return []
    return sorted ([
        re.sub(r"\.md$", "", file)
        for file in files
        if file.endswith(".md")
    ])
    



def save_entry(name, text):
    """
    Creates or updates a wiki page with the given name and Markdown content.
    """
    path = f"entries/{name}.md"
    if default_storage.exists(path):
        default_storage.delete(path)
    default_storage.save(path, ContentFile(text.encode("utf-8")))


def get_entry(name):
    """
    Loads the content of a wiki page. Returns None if the page doesn't exist.
    """
    file_path = f"entries/{name}.md"
    try:
        with default_storage.open(file_path, "rb") as f:
            raw = f.read()
            try:
                return raw.decode("utf-8")
            except UnicodeDecodeError:
                return raw.decode("cp1252")
    except FileNotFoundError:
        return None

def delete_entry(name):
    """
    Deletes a wiki page removing is Markdown file.
    Returns True if deleted, False if the file did not exist.
    """
    path = f"entries/{name}.md"
    if default_storage.exists(path):
        default_storage.delete(path)
        return True
    return False