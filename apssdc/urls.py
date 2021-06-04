from django.urls import path
from .import views
from django.contrib.auth import views as v

urlpatterns = [
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('journy/',views.journy,name='journy'),
    # path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('dashbord/',views.dashbord,name='dashbord'),
    #3rd line page views as aliad v 
    path('login/',v.LoginView.as_view(template_name='skills/login.html'),name='login'),
    # path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('uppro/',views.up,name='uppro'),

  



    path('logout/',v.LogoutView.as_view(template_name='skills/logout.html'),name='logout'),


    path('mail/',views.mail,name='mail'),
]
