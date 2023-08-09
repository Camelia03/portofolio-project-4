from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('post/add', views.PostAdd.as_view(), name='post_add'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),

]
