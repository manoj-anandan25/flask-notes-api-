import requests

class NotesAPI:
    def __init__(self, base_url="http://127.0.0.1:5000"):
        self.base_url = base_url.rstrip('/')

    def get_all_notes(self):
        r = requests.get(f"{self.base_url}/notes")
        return r.json()

    def get_note(self, note_id):
        r = requests.get(f"{self.base_url}/notes/{note_id}")
        return r.json()

    def add_note(self, title, content):
        data = {"title": title, "content": content}
        r = requests.post(f"{self.base_url}/notes", json=data)
        return r.json()

    def update_note(self, note_id, title, content):
        data = {"title": title, "content": content}
        r = requests.put(f"{self.base_url}/notes/{note_id}", json=data)
        return r.json()

    def patch_note(self, note_id, title=None, content=None):
        data = {}
        if title is not None:
            data["title"] = title
        if content is not None:
            data["content"] = content
        r = requests.patch(f"{self.base_url}/notes/{note_id}", json=data)
        return r.json()

    def delete_note(self, note_id):
        r = requests.delete(f"{self.base_url}/notes/{note_id}")
        return r.json()

    def search_notes(self, query):
        r = requests.get(f"{self.base_url}/notes/search", params={"q": query})
        return r.json()


# Example usage:
if __name__ == "__main__":
    api = NotesAPI()

    # Add a note
    print("Adding note...")
    response = api.add_note("Test Title", "Test Content")
    print(response)

    # Get all notes
    print("Fetching all notes...")
    notes = api.get_all_notes()
    print(notes)
