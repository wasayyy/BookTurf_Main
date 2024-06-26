"""
URL configuration for BookTurfProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('BookTurfMain/index/',views.index,name="index"),
    path('BookTurfMain/sign_up/',views.sign_up,name="sign_up"),
    path('BookTurfMain/sign_up/authenticate/',views.sign_up_authenticate,name="sign_up_authenticate"),
    path('BookTurfMain/login_page/',views.login_page,name="login_page"),
    path('BookTurfMain/login_page/authenticate/',views.login_page_authenticate,name="login_page_authenticate"),
    path('BookTurfMain/host_login/authenticate/',views.host_login_authenticate,name="host_login_authenticate"),
    path('BookTurfMain/host_login/',views.host_login,name="host_login"),
    path('BookTurfMain/turf_profile/<int:id>/',views.turf_profile,name="turf_profile"),
    path('BookTurfMain/add_turf_profile/',views.add_turf_profile,name="add_turf_profile"),
    path('BookTurfMain/add_turf_profile/createTurf_Profile/',views.createTurf_Profile,name="createTurf_Profile"),
    path('BookTurfMain/turf_profile/<int:id>/populate_timeslot',views.ajax_date_and_timeslot_update,name="ajax_date_and_timeslot_update"),
    path('BookTurfMain/date-view/', views.date_view, name='date_view'),
    path('BookTurfMain/submit_booking/', views.submit_booking, name='submit_booking'),
    path('BookTurfMain/reserve/', views.reserve, name='reserve'),
    path('BookTurfMain/check_out/', views.check_out, name='check_out'),
    path('BookTurfMain/delete_booking/', views.delete_booking, name='delete_booking'),
    # path('BookTurfMain/turf_page/', views.turf_page, name='turf_page'),

]
