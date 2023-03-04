from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('', views.PostListApiView.as_view(), name='post_list_api'),
    path('<int:pk>/', views.PostDetailUpdateApiView.as_view(), name='post_detail_update_api'),
    path('users/', views.UserListApiView.as_view(), name='user_list_api'),
    path('users/<int:pk>/', views.UserDetailUpdateApiView.as_view(), name='user_detail_update_api'),
]
