from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('post/add', views.PostAdd.as_view(), name='post_add'),
    path('post/<int:pk>/edit', views.PostEdit.as_view(), name='post_edit'),
    path('post/<int:pk>/like', views.like_post, name='like_post'),
    path('user/profile', views.profile, name='user_profile'),
    path('user/posts', views.UserPosts.as_view(), name='user_posts'),
    path('user/posts/delete', views.PostDelete.as_view(),
         name='post_delete'),
    path('user/profile/edit', views.EditProfile.as_view(), name='edit_profile'),
]
