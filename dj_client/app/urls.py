from django.urls import path

from app.views import my_view, add_view

urlpatterns = [
    path('', my_view, name='main'),
    path('add/', add_view, name='add'),
]
