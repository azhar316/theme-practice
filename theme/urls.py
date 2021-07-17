
from django.urls import path

from theme import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('detail/', views.DetailView.as_view(), name='detail'),
    path('people/', views.PeopleView.as_view(), name='people'),
    path('task/', views.TaskView.as_view(), name='task'),
    path('task/detail/', views.TaskDetailView.as_view(), name='task-detail'),
    path('settings/', views.SettingsView.as_view(), name='settings')
]
