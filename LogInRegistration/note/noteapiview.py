from kwikapi import API
from note.views import NotesAPI

noteapi=API()
noteapi.register(NotesAPI(),'crud')