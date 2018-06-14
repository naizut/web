"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import HomePageView
from django.conf.urls.static import static
from myblog import settings
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="nav.html"), name="nav"),
    url(r'^admin/', admin.site.urls),
    # url(r'^home/', TemplateView.as_view(template_name="home.html"), name="home"),
    url(r'^home/', HomePageView.as_view(), name="home"),
    url(r'^dev_log/', include('dev_log.urls', namespace='dev_log', app_name='dev_log')),
    url(r'^music/', include('music.urls', namespace='music', app_name='music')),
    url(r'^games/', include('games.urls', namespace='games', app_name='games')),
    url(r'^news/', include('news.urls', namespace='news', app_name='news')),

    url(r'^chat_board/', include('chat.urls', namespace='chat', app_name='chat_board')),
    url(r'^download/', TemplateView.as_view(template_name="download.html"), name="download"),
    url(r'^account/', include('account.urls', namespace='account', app_name='account')),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += staticfiles_urlpatterns()