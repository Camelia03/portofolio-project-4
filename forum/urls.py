from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.PostList.as_view(), name='posts'),
    path('add', views.add_post, name='add'),
]
