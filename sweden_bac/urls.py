"""
URL configuration for sweden_bac project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from blog import views as blog
from about import views as about
from contact import views as contact
from events import views as events
from gallery import views as gallery
from routes import views as routes
from shop import views as shop
from videos import views as videos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('about.urls'), name="about"),
    path('blog/', include('blog.urls'), name="blog"),
    path('contact/', include('contact.urls'), name="contact"),
    path('events/', include('events.urls'), name='events'),
    path('gallery/', include('gallery.urls'), name="gallery"),
    path('routes/', include('routes.urls'), name="routes"),
    path('shop/', include('shop.urls'), name="shop"),
    path('videos/', include('videos.urls'), name="video"),
]
