from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('rub/', rub, name='rub'),
    path('restart/', restart, name='restart'),
    path('answer/<str:answer>/', answer, name='answer'),
    path('test/', test, name='test')
]