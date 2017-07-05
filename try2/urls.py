"""try2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from booktest import views
import booktest

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^get/$', views.get),
    url(r'^get2/$',views.get2),
    url(r'^get3/$',views.get3),
    url(r'^post1/$',views.post1),
    url(r'^post2/$',views.post2),
    url(r'^index2/$',views.index2),
    url('^',include('booktest.urls'))
    # url(r'^$',views.index),
]









