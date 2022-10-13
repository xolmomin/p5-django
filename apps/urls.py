from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import index_page, about_page

urlpatterns = [
    path('', index_page),
    path('about', about_page)
]
