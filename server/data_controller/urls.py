from django.urls import path

from . import views

urlpatterns = [
    path('data/', views.data_saver, name='data'),
    path('map/', views.map, name='map')
]
