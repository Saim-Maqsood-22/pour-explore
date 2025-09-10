from django.urls import path
from . import views
urlpatterns = [
    path("", views.contactSubmit, name="contact"),
    path("Thanks/", views.Thanks, name="Thanks")
]