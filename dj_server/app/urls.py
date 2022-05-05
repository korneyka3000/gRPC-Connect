from django.urls import path

from .views import q_view


urlpatterns = [
    path('', q_view, name='question'),
]