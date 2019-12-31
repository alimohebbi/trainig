from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/update/', views.ExerciseUpdate.as_view(), name='exercise_update'),
    path('<int:pk>/delete/', views.ExerciseDelete.as_view(), name='exercise_delete'),
    path('create/', views.ExerciseCreate.as_view(), name='exercise_create'),
    path('<int:pk>/', views.ExerciseView.as_view(), name='exercise_detail'),
    path('list/', views.ExerciseListView.as_view(), name='exercise_list'),
]
