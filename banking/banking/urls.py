from django.urls import path, include
from django.contrib import admin
from account.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', index, name='home'),
    path('user', include('user.urls')),
]
