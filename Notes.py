from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Database model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Note {self.title}>"

# Welcome route
@app.route('/')
def home():
    return 'MY NOTES'

# Get all notes
@app.route('/notes')
def get_notes():
    notes = Note.query.all()
    output = []
    for note in notes:
        note_data = {
            "id": note.id,
            "title": note.title,
            "content": note.content,
            "created_at": note.created_at,
            "updated_at": note.updated_at
        }
        output.append(note_data)
    return {"notes": output}

# Get a single note by id
@app.route('/notes/<id>')
def get_note(id):
    note = Note.query.get(id)
    if note is None:
        return {"error": "Note not found"}
    return {
        "id": note.id,
        "title": note.title,
        "content": note.content,
        "created_at": note.created_at,
        "updated_at": note.updated_at
    }

# Add a new note
@app.route('/notes', methods=['POST'])
def add_note():
    note = Note(
        title=request.json['title'],
        content=request.json['content']
    )
    db.session.add(note)
    db.session.commit()
    return {"id": note.id}

# Update an existing note fully (PUT)
@app.route('/notes/<id>', methods=['PUT'])
def update_note(id):
    note = Note.query.get(id)
    if note is None:
        return {"error": "Note not found"}
    note.title = request.json['title']
    note.content = request.json['content']
    db.session.commit()
    return {"message": "Note updated successfully"}

# Update a note partially (PATCH)
@app.route('/notes/<id>', methods=['PATCH'])
def patch_note(id):
    note = Note.query.get(id)
    if note is None:
        return {"error": "Note not found"}
    if 'title' in request.json:
        note.title = request.json['title']
    if 'content' in request.json:
        note.content = request.json['content']
    db.session.commit()
    return {"message": "Note patched successfully"}

# Delete a note
@app.route('/notes/<id>', methods=['DELETE'])
def delete_note(id):
    note = Note.query.get(id)
    if note is None:
        return {"error": "Note not found"}
    db.session.delete(note)
    db.session.commit()
    return {"message": "Note deleted"}


@app.route('/notes/search', methods = ['GET'])
def search_notes():
    query = request.args.get('q')
    if not query:
        return {"error":"No search query provided"}
    notes = Note.query.filter(Note.title.contains(query) | Note.content.contains(query)).all()
    output = []
    for note in notes:
        note_data = {"id":note.id, "title":note.title, "content":note.content, "created_at":note.created_at, "updated_at":note.updated_at}
        output.append(note_data)
    return {"results":output}



