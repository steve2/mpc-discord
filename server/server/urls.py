"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.urls import path
from server import settings
from server.views import BaseView, NotFoundView
from discord.views import Discord, DiscordRole, DiscordMember

urlpatterns = [
    path('admin/', admin.site.urls),
    path('discord/', Discord.as_view()),
    path('discord/roles/<name>', DiscordRole.as_view()),
    path('discord/users/<id>', DiscordMember.as_view()),
    path('', BaseView.as_view()),
]

handler404 = NotFoundView.as_view()
