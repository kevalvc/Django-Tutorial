from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('malaria',views.malaria),
    # path('register',views.register, name='register'),
    # path('logout',views.user_logout, name='logout'),
    # path('user_login',views.user_login, name='user_login'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/new', views.post_new, name='post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]

# https://www.geeksforgeeks.org/python-uploading-images-in-django/
