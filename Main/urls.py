from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('register/', registerpage, name='register'),
    path('register2/', frontend_register, name='register2'),
    path('login2/', frontend_login, name='login2'),
    path('logout2/', frontend_logout, name='logout2')
]