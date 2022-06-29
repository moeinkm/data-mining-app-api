from django.urls import path

from service3 import views


app_name = 'service3'

urlpatterns = [
    path('', views.Service3View.as_view(), name='service3')
]
