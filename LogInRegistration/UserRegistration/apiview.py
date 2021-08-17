from UserRegistration.views import Index,LogIn,Register
from kwikapi import API

"""
    Here i have created an Api named user_api and registered Index with namespace = home,
    Register with namespace = register,LogIn with namespace = login
"""

user_api=API()
user_api.register(Index(),'home')
user_api.register(Register(),'register')
user_api.register(LogIn(),'login')