from django.urls import path
from .views import app_page_view

urlpatterns = [
    path("", app_page_view),       # add the path to the app_page_view
]
