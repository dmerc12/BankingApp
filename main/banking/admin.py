from django.utils.html import format_html
from django.contrib import admin
from .models import *

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'account_number', 'bank_name', 'location', 'balance', 'notes', 'created', 'last_modified']
    list_filter = ['user', 'account_number', 'bank_name', 'location', 'created', 'last_modified']
    search_fields = ['user', 'account_number', 'bank_name', 'location', 'created', 'last_modified']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'account', 'type', 'timestamp']
