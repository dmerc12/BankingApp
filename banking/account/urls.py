from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create_account, name='create-account'),
    path('', account_list, name='account-list'),
]
