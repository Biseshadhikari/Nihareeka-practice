from django.urls import path
from .views import *
urlpatterns =[
    path('',home,name = "home"),
    path('profile/<str:username>/',profileDetail,name = "profiledetail"),
    path('post/<int:id>/',postdetail,name ="postdetail")

]