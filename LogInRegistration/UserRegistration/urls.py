from django.conf.urls import url
from UserRegistration import apiview
from kwikapi.django import RequestHandler

urlpatterns = [
    url(r'^api/', RequestHandler(apiview.user_api).handle_request),
]