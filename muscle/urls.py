from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/update/', views.MuscleUpdate.as_view(), name='muscle_update'),
    path('<int:pk>/delete/', views.MuscleDelete.as_view(), name='muscle_delete'),
    path('create/', views.MuscleCreate.as_view(), name='muscle_create'),
    path('<int:pk>/', views.MuscleView.as_view(), name='muscle_detail'),
    path('list/', views.MuscleListView.as_view(), name='muscle_list'),

]
