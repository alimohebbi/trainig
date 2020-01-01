from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/update/', views.WorkoutUpdate.as_view(), name='workout_update'),
    path('<int:pk>/delete/', views.WorkoutDelete.as_view(), name='workout_delete'),
    path('create/', views.WorkoutCreate.as_view(), name='workout_create'),
    path('<int:pk>/', views.WorkoutView.as_view(), name='workout_detail'),
    path('list/', views.WorkoutListView.as_view(), name='workout_list'),
    path('ajax/load-exercises/', views.load_exercises, name='ajax_load_exercises'),
]
