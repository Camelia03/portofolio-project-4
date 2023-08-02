from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_post, name='add'),
    path('signup', views.SignUpView.as_view(), name='signup')
]
