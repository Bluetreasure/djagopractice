"""djangotest URL Configuration

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
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from hanktest.views import index
from hanktest.views import login
from hanktest.views import userinfo
from hanktest.views import logout
from hanktest.views import poll
from hanktest.views import vote

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^poll/(\d+)$', poll, name='poll-url'),
    url(r'^vote/(\d+)/(\d+)$', vote, name='vote-url'),
    url(r'^userinfo/$', userinfo),
    url(r'^logout/$', logout),
    url(r'^login/$', login),
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
]
