from django.urls import path

from .views import index_page, form_page

urlpatterns = [
    path('', index_page, name='index_page'),
    path('form-create', form_page, name='form_page')
]
