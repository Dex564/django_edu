
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')), # namespace - есть в base.html потом понадобится для обращений, чтобы вести редиректы, делать ссылки в шаблонах
]
