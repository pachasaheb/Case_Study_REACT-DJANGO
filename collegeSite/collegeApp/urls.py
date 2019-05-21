from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('createUser/', views.createUser, name='createUser'),
    path('retrieveUsers/', views.retrieveUsers, name='retrieveUsers'),
    path('updateUser/', views.updateUser, name='updateUser'),
    path('deleteUser/', views.deleteUser, name='deleteUser'),


    path('createCollege/', views.createCollege, name='createCollege'),
    path('retrieveColleges/', views.retrieveColleges, name='retrieveColleges'),
    path('updateCollege/', views.updateCollege, name='updateCollege'),
    path('deleteCollege/', views.deleteCollege, name='deleteCollege')
   ]