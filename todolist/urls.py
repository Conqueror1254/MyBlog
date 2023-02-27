from django.urls import path
from .views import todo, category

urlpatterns = [
    path('post/<int:pk>/', category, name ='category'),
    path('', todo, name = 'basa'),
]