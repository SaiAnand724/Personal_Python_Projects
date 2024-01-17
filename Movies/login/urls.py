from django.urls import path
from . import views

# URL Configuration in app
urlpatterns = [
    # Always end routes with a "/"
    path('login/', views.show_login)
]
