from django.urls import path
from appbasic import views
app_name = 'appbasic'
urlpatterns = [
    path('', views.registrationView, name='register'),
    path('login/', views.loginView, name='user_login'),
]
