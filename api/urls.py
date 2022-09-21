from django.urls import path
from api import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('registerapi',views.registerapi.as_view(),name='register'),
    path('loginapi/',obtain_auth_token,name="login"),
    path('welcome',views.welcome.as_view(),name='welcome'),
    path('userdetails/<int:pk>/',views.userdetails.as_view(),name='userdetails'),

]