from django.urls import path
from . import views
urlpatterns = [
    path('myproject/', views.myproject1, name='myproject1'),
]