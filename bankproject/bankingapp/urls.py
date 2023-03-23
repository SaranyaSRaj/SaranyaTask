from django.urls import path, include
from.import views
app_name= 'bankingapp'
urlpatterns = [
       path('', views.index, name='index'),
       path('signup',views.signup,name="signup"),
       path('signin',views.signin,name="signin"),
       path('registration',views.registration, name="registration"),
       path('forms',views.forms, name='forms'),
       path('logout',views.logout,name="logout"),
]
