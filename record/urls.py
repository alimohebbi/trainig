from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/update/', views.update, name='record_update'),
    path('<int:pk>/delete/', views.delete, name='record_delete'),
    path('create/', views.post, name='record_create'),
    path('records/', views.retrieve_records, name='retrieve_records'),
    path('list/', views.RecordListView.as_view(), name='record_list'),
]
