from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='Index'),
    path('/details/<int:id>', views.details, name='details')
]