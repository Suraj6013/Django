from django.urls import path
from . import views

# url configuration for the playground app
urlpatterns = [
    path('hello/', views.say_hello)
] 