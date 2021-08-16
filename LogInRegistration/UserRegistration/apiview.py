from UserRegistration.views import Index,LogInAPI,RegisterAPI
from kwikapi import API

apis=API()
apis.register(Index(),'home')
apis.register(RegisterAPI(),'register')
apis.register(LogInAPI(),'login')