# maps/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-feature/', views.CreateFeature.as_view(), name='create-feature'),
]
