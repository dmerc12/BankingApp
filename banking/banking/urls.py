from django.urls import path, include
from django.contrib import admin
from user.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('user.urls')),
]
