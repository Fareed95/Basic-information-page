from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('function1',views.function1, name ='function1')
]
