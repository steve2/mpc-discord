import json
import os

from .oauth2 import DiscordOAuth2Session
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView

# Allow insecure transport (HTTP) for development.
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

class DiscordBotInfo(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        discord = DiscordOAuth2Session('127671174648823808')
        members = json.loads(discord.members(limit=20).text)
        roles = json.loads(discord.roles().text)
        return { 'members': members, 'roles': roles }
