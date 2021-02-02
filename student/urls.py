"""student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""

from django.contrib import admin
from django.urls import include, path
from first import views

"""urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.index,name="index"),
    
    path('login',views.login,name="login"),
    path('registration',views.registration,name="registration"),
    path('welcome',views.welcome,name="welcome")
]"""

from django.contrib import admin  
from django.urls import path  
from first import views  
urlpatterns = [  
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),  
    path('new', views.new,name="new"),  
    path('show',views.show,name="show"),  
    path('edit/<int:id>', views.edit,name="edit"),  
    path('update/<int:id>', views.update,name="update"),  
    path('delete/<int:id>', views.destroy,name="destroy")  
] 

"""from django.urls import path
from first import views 



app_name = 'first'  # here for namespacing of urls.

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.registration, name="registration"),
    path("logout_request", views.logout_request, name="logout_request"),
    path("login_request", views.login_request, name="login_request")
] """
