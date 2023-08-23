from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('signup', views.SignUpView.as_view(), name='signup'),

    path('channels/<str:name>', views.Index.as_view(),
         name='channel_threads'),

    path(
        'thread/<int:pk>/', views.ThreadDetail.as_view(), name="thread_detail"
    ),
    path('thread/add', views.ThreadAdd.as_view(), name='thread_add'),
    path('thread/search', views.ThreadSearch.as_view(), name='thread_search'),
    path(
        'thread/<int:pk>/edit', views.ThreadEdit.as_view(), name='thread_edit'
    ),
    path('thread/<int:pk>/upvote', views.upvote_thread, name='upvote_thread'),
    path(
        'thread/<int:pk>/downvote', views.downvote_thread,
        name='downvote_thread'
    ),

    path('user/profile', views.profile, name='user_profile'),
    path(
        'user/profile/edit', views.EditProfile.as_view(), name='edit_profile'
    ),
    path('user/<str:username>/profile',
         views.view_profile, name='public_profile'),

    path('user/threads', views.UserThreads.as_view(), name='user_threads'),
    path('user/threads/delete', views.ThreadDelete.as_view(),
         name='thread_delete'),
]
