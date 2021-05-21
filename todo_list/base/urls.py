from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name='home'),
    path('task/', views.task_list, name='tasks'),
    path('task/<int:task_id>/', views.task_detail, name='detail'),
    path('task-create/', views.task_create, name='create'),
    path('task-update/<int:task_id>', views.task_update, name='update'),
    path('task-delete/<int:task_id>', views.task_delete, name='delete'),
]
