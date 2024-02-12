from django.urls import path
from .views import *

urlpatterns = [
    path('', account_list, name='account-list'),
    path('create/', create_account, name='create-account'),
    path('deposit/<int:account_id>/',  deposit, name='deposit'),
    path('withdraw/<int:account_id>/',  withdraw, name='withdraw'),
    path('delete/<int:account_id>/', delete_account, name='delete-account')
]
