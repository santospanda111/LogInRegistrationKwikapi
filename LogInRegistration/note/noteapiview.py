from kwikapi import API
from note.views import NotesAPI

note_api=API()
note_api.register(NotesAPI(),'crud')