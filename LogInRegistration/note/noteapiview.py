from kwikapi import API
from note.views import Notes

"""
    Here i have created an Api named note_api and registered Notes with namespace = crud
"""
note_api=API()
note_api.register(Notes(),'crud')