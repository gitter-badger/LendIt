"""lendit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from website import views
from django.views.generic import ListView

from website.models import LenditUser

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', views.home, name='home'),
    url(r'^lend$', views.lend, name='lend'),
    url(r'^book/(?P<pk>\S+)/$', views.book, name='book'),
    url(r'^book/(?P<user_pk>\S+)/(?P<book_pk>\S+)$', views.user_book, name='user_book'),
    url(r'^profile/(?P<pk>\S+)/$', views.profile, name='profile'),
    url(r'^request_book/(?P<user_pk>\S+)/(?P<book_pk>\S+)$', views.request_book, name='request_book'),
    url(r'^return_book/(?P<user_pk>\S+)/(?P<book_pk>\S+)$', views.return_book, name='return_book'),
    url(r'^notifications/$', views.notifications, name='notifications'),
    url(r'^request-handle$', views.request_handle, name='request_handle'),
    url(r'^update_location$', views.update_location, name='update_location')
]
