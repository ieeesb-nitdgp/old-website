"""register URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from thereg import views
# SET THE NAMESPACE!
app_name = 'thereg'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^feedback_form/$', views.feedback_form, name='feedback'),
    url(r'^members/$', views.members, name='members'),
    url(r'^alumni/$', views.alumni, name='alumni'),
    url(r'^varification/$', views.varification, name='varification'),
    path('', views.PostList.as_view(), name='events'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='event_detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
