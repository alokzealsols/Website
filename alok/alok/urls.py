"""alok URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app.models import Profile
from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index_Page,name="Index"),
    path('register',register,name='register'),
    path('login_page',login_page,name='login_page'),
    path('token' , token_send , name="token_send"),
    path('success' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error"),
    path('Index',Index_Page,name='index'),
    path('Bicyclelist',Bicyclelist,name='Bicyclelist'),
    path('Booking',Booking,name='Booking'),
    path('Detail',Detail,name='Detail'),
    path('Team',Team,name='Team'),
    path('Testimonial',Testimonial,name='Testimonial'),
    path('Contact',Contact,name='Contact'),
    path('sendmail',sendmail,name='sendmail'),
]


