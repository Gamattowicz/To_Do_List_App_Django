from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'base'

urlpatterns = [
    path('login/', views.TaskLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='base:login'), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('', views.HomeView.as_view(), name='home'),
    path('task/', views.TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='detail'),
    path('task-create/', views.TaskCreate.as_view(), name='create'),
    path('task-update/<int:pk>', views.TaskUpdate.as_view(), name='update'),
    path('task-delete/<int:pk>', views.TaskDelete.as_view(), name='delete'),
    path('task-complete/<int:task_id>', views.change_complete_status, name='change_complete'),
    path('category-create/', views.CategoryCreate.as_view(), name='create_category'),
]
