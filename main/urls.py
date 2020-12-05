from django.urls import path, include
from main import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('post/<int:pk>/', views.PostDetail.as_view()),
]

