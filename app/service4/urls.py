from django.urls import path

from service4 import views


app_name = 'service4'

urlpatterns = [
    path('', views.Service4View.as_view(), name='service4')
]
