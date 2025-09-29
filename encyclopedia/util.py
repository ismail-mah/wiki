import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def list_entries():
    print("📁 Attempting to list files in 'entries' folder...")
    try:
        dirs, files = default_storage.listdir("entries")
        print("✅ Files found:", files)
    except Exception as e:
        print("❌ Error accessing entries folder:", e)
        return []

    titles = [
        re.sub(r"\.md$", "", file)
        for file in files
        if file.endswith(".md")
    ]
    print("📄 Filtered titles:", titles)
    return sorted(titles)



def save_entry(name, text):
    """
    Creates or updates a wiki page with the given name and Markdown content.
    """
    path = f"entries/{name}.md"
    if default_storage.exists(path):
        default_storage.delete(path)
    default_storage.save(path, ContentFile(text))


def get_entry(name):
    """
    Loads the content of a wiki page. Returns None if the page doesn't exist.
    """
    file_path = f"entries/{name}.md"
    try:
        with default_storage.open(file_path) as f:
            return f.read().decode("utf-8")
    except FileNotFoundError:
        return None
