from django.urls import path
from .views import *
urlpatterns =[
    path('',home,name = "home"),
    path('profile/<str:username>/',profileDetail,name = "profiledetail"),
    path('post/<int:id>/',postdetail,name ="postdetail"),
    path('delete/<int:id>/',Postdelete,name ="postdelete"),
        path('update/<int:id>/',update,name ="postupdate")


]