from django.urls import path

from service1 import views


app_name = 'service1'

urlpatterns = [
    path('', views.Service1View.as_view(), name='service1')
]
