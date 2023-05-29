from django.urls import path
from GT.views import *
app_name='anything'
urlpatterns=[
    path('hardik/',hardik,name='hardik')
]