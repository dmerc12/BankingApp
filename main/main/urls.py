from django.urls import path, include
from django.contrib import admin
from banking.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('banking/', include('banking.urls')),
    path('', index, name='home'),
    path('users/', include('users.urls')),
]
