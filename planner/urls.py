from django.urls import path

from . import views

urlpatterns = [
    path('muscle/<int:pk>/edit/', views.muscle_edit, name='muscle_edit'),
    path('muscle/new/', views.muscle_new, name='muscle_new'),
    path('muscle/<int:pk>/', views.MuscleView.as_view(), name='muscle_detail'),
    path('muscle/', views.MuscleListView.as_view(), name='muscle'),

]
