from UserRegistration.views import Index,LogIn,Register
from kwikapi import API

user_api=API()
user_api.register(Index(),'home')
user_api.register(Register(),'register')
user_api.register(LogIn(),'login')