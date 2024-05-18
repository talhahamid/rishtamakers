from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("index",views.index,name="index"),
    path("insert",views.insert,name="insert"),
    path("edit/<int:id>",views.edit,name="edit"),
    path("edit/update/<int:id>",views.update,name="update"),
    path("delete",views.delete,name="delete"),    

    path("home",views.home,name="home"),

    path("login",views.login,name="login"),

# signin/signup
    #path("signup",views.signup,name="signup"),
    path("signin",views.signin,name="signin"),

    path("userview",views.userview,name="userview"),

# USERS
    path("Usersindex",views.Usersindex,name="Usersindex"),
    path("Usersinsert",views.Usersinsert,name="Usersinsert"),
    path("Usersedit/<int:id>",views.Usersedit,name="Usersedit"),
    path("Usersedit/Usersupdate/<int:id>",views.Usersupdate,name="Usersupdate"),
    path("Usersdelete/<int:id>",views.Usersdelete,name="Usersdelete"),
# Religion
    path("Religionindex",views.Religionindex,name="Religionindex"),
    path("Religioninsert",views.Religioninsert,name="Religioninsert"),
    path("Religionedit/<int:id>",views.Religionedit,name="Religionedit"),
    path("Religionedit/Religionupdate/<int:id>",views.Religionupdate,name="Religionupdate"),
    path("Religiondelete/<int:id>",views.Religiondelete,name="Religiondelete"),
# ReligionCategory
    path("Religion_categoryindex",views.Religion_categoryindex,name="Religion_categoryindex"),
    path("Religion_categoryinsert",views.Religion_categoryinsert,name="Religion_categoryinsert"),
    path("Religion_categoryedit/<int:id>",views.Religion_categoryedit,name="Religion_categoryedit"),
    path("Religion_categoryedit/Religion_categoryupdate/<int:id>",views.Religion_categoryupdate,name="Religion_categoryupdate"),
    path("Religion_categorydelete/<int:id>",views.Religion_categorydelete,name="Religion_categorydelete"),
# Status
    path("Statusindex",views.Statusindex,name="Statusindex"),
    path("Statusinsert",views.Statusinsert,name="Statusinsert"),
    path("Statusedit/<int:id>",views.Statusedit,name="Statusedit"),
    path("Statusedit/Statusupdate/<int:id>",views.Statusupdate,name="Statusupdate"),
    path("Statusdelete/<int:id>",views.Statusdelete,name="Statusdelete"),
# Education
    path("Educationindex",views.Educationindex,name="Educationindex"),
    path("Educationinsert",views.Educationinsert,name="Educationinsert"),
    path("Educationedit/<int:id>",views.Educationedit,name="Educationedit"),
    path("Educationedit/Educationupdate/<int:id>",views.Educationupdate,name="Educationupdate"),
    path("Educationdelete/<int:id>",views.Educationdelete,name="Educationdelete"),
# Occuptation
    path("Occupationindex",views.Occupationindex,name="Occupationindex"),
    path("Occupationinsert",views.Occupationinsert,name="Occupationinsert"),
    path("Occupationedit/<int:id>",views.Occupationedit,name="Occupationedit"),
    path("Occupationedit/Occupationupdate/<int:id>",views.Occupationupdate,name="Occupationupdate"),
    path("Occupationdelete/<int:id>",views.Occupationdelete,name="Occupationdelete"),
# MotherTongue   
    path("Mothertongueindex",views.Mothertongueindex,name="Mothertongueindex"),
    path("Mothertongueinsert",views.Mothertongueinsert,name="Mothertongueinsert"),
    path("Mothertongueedit/<int:id>",views.Mothertongueedit,name="Mothertongueedit"),
    path("Mothertongueedit/Mothertongueupdate/<int:id>",views.Mothertongueupdate,name="Mothertongueupdate"),
    path("Mothertonguedelete/<int:id>",views.Mothertonguedelete,name="Mothertonguedelete"),

]