from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create_account, name='create-account'),
    path('update/<int:account_id>/', update_account, name='update-account'),
    path('deposit/<int:account_id>/',  deposit, name='deposit'),
    path('withdraw/<int:account_id>/',  withdraw, name='withdraw'),
    path('transfer/<int:account_id>/', transfer, name='transfer'),
    path('transactions/<int:account_id>/', transactions, name='transactions'),
    path('delete/<int:account_id>/', delete_account, name='delete-account'),
    path('transaction/<int:transaction_id>/', update_transaction, name='update-transaction'),
    path('transaction/<int:transaction_id>/delete/', delete_transaction, name='delete-transaction'),
]
