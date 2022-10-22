from django.urls import path

from .views import index_page, form_page, login_page,register_page

urlpatterns = [
    path('', index_page, name='index'),
    path('form-create', form_page, name='form_page'),
    path('login', login_page, name='login_page'),
    path('register', register_page, name='register_page')
]

# login, register
