from django.urls import path
from .views import *

app_name = 'core'
urlpatterns = [
    path('', main, name='main'),
    path('screen2/', screen2, name='screen2'),
    path('screen3/',screen3,name='screen3'),
]
