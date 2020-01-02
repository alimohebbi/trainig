from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/update/', views.PlanUpdate.as_view(), name='plan_update'),
    path('<int:pk>/delete/', views.PlanDelete.as_view(), name='plan_delete'),
    path('create/', views.PlanCreate.as_view(), name='plan_create'),
    path('<int:pk>/', views.PlanView.as_view(), name='plan_detail'),
    path('list/', views.PlanListView.as_view(), name='plan_list'),
    path('ajax/load-workouts/', views.load_workouts, name='ajax_load_workouts'),

]
