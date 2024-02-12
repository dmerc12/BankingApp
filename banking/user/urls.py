from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('delete/', delete_user, name='delete-user'),
    path('update/', update_user, name='update-user'),
    path('change-password', change_password, name='change-password'),
]
