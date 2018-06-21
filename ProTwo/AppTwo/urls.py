from django.urls import path
from AppTwo import views

urlpatterns = [
        path(r'^$',views.help,name='help')
        path('/users', views.users,name='users')
        path('/upload', views.upload_files,name='upload_files')
        ]

