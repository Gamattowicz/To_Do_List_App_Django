from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'base'

urlpatterns = [
    path('login/', views.TaskLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='base:login'), name='logout'),
    path('', views.home, name='home'),
    path('task/', views.TaskList.as_view(), name='tasks'),
    path('task/<int:task_id>/', views.task_detail, name='detail'),
    path('task-create/', views.task_create, name='create'),
    path('task-update/<int:task_id>', views.task_update, name='update'),
    path('task-delete/<int:task_id>', views.task_delete, name='delete'),
]
