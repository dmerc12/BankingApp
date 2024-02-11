from django.urls import path
from .views import *

urlpatterns = [
    path('', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('home/', index, name='home'),
    path('register/', register, name='register'),
    path('update/', update_user, name='update-user'),
    path('change-password', change_password, name='change-password'),
]
