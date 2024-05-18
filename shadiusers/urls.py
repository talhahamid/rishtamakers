from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.loginuser,name="loginuser"),
    path("logout/",views.logout,name="logout"), 
    path("register/",views.register,name="register"), 
    path("profile/<int:id>/",views.profile,name="profile"), 
    path("personaldetails/",views.personaldetails,name="personaldetails"), 
    path("editpersonaldetails/",views.editpersonaldetails,name="editpersonaldetails"),

    path("pics/",views.pics,name="pics"), 
    path("addpics/",views.addpics,name="addpics"),

    path("profileslist/",views.profileslist,name="profileslist"),
    path("userprofile/<int:id>/",views.userprofile,name="userprofile"),

    path("subscribe/<int:id>/",views.subscribe,name="subscribe"),
    path("freeplan/<int:id>/",views.freeplan,name="freeplan"),

    path("myplans/<int:id>/",views.myplans,name="myplans"),

    path("profiles_list/",views.profiles_list,name="profiles_list"),
]
