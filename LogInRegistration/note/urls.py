from django.conf.urls import url
from note import noteapiview
from kwikapi.django import RequestHandler

urlpatterns = [
    url(r'^noteapp/', RequestHandler(noteapiview.note_api).handle_request),
]