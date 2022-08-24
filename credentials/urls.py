
from django.urls import path

from .import views
app_name="credentials"

urlpatterns = [

    path('',views.home,name="home"),
    path('login',views.login,name='login'),
    path('register', views.register, name='register'),
    path('newpage',views.newpage,name="newpage"),
    path('formpage',views.formpage,name="formpage"),
    path('messages/',views.messages_form,name="messages_form"),
    path('logout/',views.logout,name="logout"),

    path('ajax/load-branches/',views.load_branches,name='ajax_load_branches'),

]
