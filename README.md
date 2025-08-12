A simple **Notes Management** REST API built with **Flask** and **SQLite**.  
This API lets you create, read, update, delete, and search notes.

---

## What is this?

Imagine a digital notebook where you can save notes with titles and content.  
This project lets you manage those notes programmatically via simple web requests.

---

## How to Use This API

- **View all notes**  
- **Add new notes**  
- **Update or delete existing notes**  
- **Search notes by keyword**

---

## How to Run the Project

### Requirements

- Python 3.7 or newer  
- Internet browser or API testing tool like [Postman](https://www.postman.com/) (optional)

### Setup Steps

1. Clone this repository.  
2. Install dependencies:
   ```bash
   pip install flask flask_sqlalchemy
````

3. Initialize the database:

   Open Python shell or create a script and run:

   ```python
   from app import db
   db.create_all()
   ```

4. Run the server:

   ```bash
   flask run
   ```

   The API will be available at `http://127.0.0.1:5000/`

---

## API Endpoints Overview

| Endpoint              | Method | Description                      |
| --------------------- | ------ | -------------------------------- |
| `/`                   | GET    | Welcome message                  |
| `/notes`              | GET    | Get all notes                    |
| `/notes`              | POST   | Add a new note                   |
| `/notes/<id>`         | GET    | Get a note by ID                 |
| `/notes/<id>`         | PUT    | Fully update a note              |
| `/notes/<id>`         | PATCH  | Partially update a note          |
| `/notes/<id>`         | DELETE | Delete a note                    |
| `/notes/search?q=...` | GET    | Search notes by title or content |

---

## Example: Add a Note (POST `/notes`)

Send a JSON request like:

```json
{
  "title": "Shopping list",
  "content": "Milk, Eggs, Bread"
}
```

---

## Example: Search Notes

Request:

```
GET /notes/search?q=milk
```

Response:

```json
{
  "results": [
    {
      "id": 1,
      "title": "Shopping list",
      "content": "Milk, Eggs, Bread",
      "created_at": "...",
      "updated_at": "..."
    }
  ]
}
```




To make it easy for other Python projects or users to call your API (like a mini SDK), here’s a simple Python class you can provide as `notes_sdk.py`:

```python
import requests

class NotesAPI:
    def __init__(self, base_url="http://127.0.0.1:5000"):
        self.base_url = base_url.rstrip('/')

    def get_all_notes(self):
        response = requests.get(f"{self.base_url}/notes")
        return response.json()

    def get_note(self, note_id):
        response = requests.get(f"{self.base_url}/notes/{note_id}")
        return response.json()

    def add_note(self, title, content):
        data = {"title": title, "content": content}
        response = requests.post(f"{self.base_url}/notes", json=data)
        return response.json()

    def update_note(self, note_id, title, content):
        data = {"title": title, "content": content}
        response = requests.put(f"{self.base_url}/notes/{note_id}", json=data)
        return response.json()

    def patch_note(self, note_id, title=None, content=None):
        data = {}
        if title is not None:
            data["title"] = title
        if content is not None:
            data["content"] = content
        response = requests.patch(f"{self.base_url}/notes/{note_id}", json=data)
        return response.json()

    def delete_note(self, note_id):
        response = requests.delete(f"{self.base_url}/notes/{note_id}")
        return response.json()

    def search_notes(self, query):
        response = requests.get(f"{self.base_url}/notes/search", params={"q": query})
        return response.json()
```

