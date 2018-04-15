from datetime import datetime
import json
import os

from .api.oauth2 import DiscordOAuth2
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.base import TemplateView

from discord.permissions import translate

# Allow insecure transport (http) for development.
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


class Discord(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        discord = DiscordOAuth2()
        members = json.loads(discord.members(limit=1000).text)
        roles = json.loads(discord.roles().text)
        for role in roles:
            role['permissions'] = translate(role['permissions'])
        for member in members:
            # the discriminator needs to be modded by 5 as per API specification.
            # https://discordapp.com/developers/docs/reference#image-formatting
            member['user']['discriminator'] = str(int(member['user']['discriminator']) % 5)
            modified_roles = []
            for member_role in member['roles']:
                for role in roles:
                    if role['id'] == member_role:
                        modified_roles.append(role)
                        break
            member['roles'] = modified_roles
        return {'members': members, 'roles': roles}


class DiscordMember(TemplateView):
    template_name = 'member.html'

    def get_context_data(self, **kwargs):
        discord = DiscordOAuth2()
        member = json.loads(discord.member(self.kwargs['id']).text)
        roles = json.loads(discord.roles().text)
        if 'user' not in member:
            raise Http404
        member['user']['discriminator'] = str(int(member['user']['discriminator']) % 5)
        modified_roles = []
        for member_role in member['roles']:
            for role in roles:
                if role['id'] == member_role:
                    modified_roles.append(role)
                    break
        member['roles'] = modified_roles
        member['joined_at'] = datetime.strptime(member['joined_at'], '%Y-%m-%dT%H:%M:%S.%f+00:00')
        return {'member': member}


class DiscordRole(TemplateView):
    template_name = 'role.html'

    def get_context_data(self, **kwargs):
        discord = DiscordOAuth2()
        roles = json.loads(discord.roles().text)
        found = None
        for role in roles:
            if role['name'] == self.kwargs['name']:
                found = role
                found['permissions'] = translate(role['permissions'])
                break
        if found is None:
            raise Http404
        else:
            return {'role': found}
