from django.urls import path

from service2 import views


app_name = 'service2'

urlpatterns = [
    path('', views.Service2View.as_view(), name='service2')
]
