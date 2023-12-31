from django.urls import path
from .views import TaskList, TaskDetails, TaskCreate, TaskUpdate, TaskDelete, LoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns  = [
    path('', TaskList.as_view(), name='task'),
    path('task-create', TaskCreate.as_view(), name='task-create'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('task/<int:pk>/',TaskDetails.as_view(), name='tasks-detail'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(), name='task-delete')
]