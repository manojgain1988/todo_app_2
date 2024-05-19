
from django.urls import path
from TodoApp  import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_page, name='logout'),

    path('update/<int:id>/', views.update_task, name='update'),
    path('delete/<int:id>/', views.delete_task, name='delete'),

] 