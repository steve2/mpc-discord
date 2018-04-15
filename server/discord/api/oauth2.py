"""Discord OAuth2 communication class.

This module provides class `DiscordOAuth2Session` that wraps a `requests`
session with Discord-specific OAuth2 authentication.
"""

import requests

MPC_SERVER_ID = '127671174648823808'
OAUTH2_CLIENT_ID = '421896176082616330'
OAUTH2_CLIENT_SECRET = 'WnmljxCmCTir_0PmDwrIDf9gYmfze1i9'
API_BASE_URL = 'https://discordapp.com/api'
BOT_TOKEN = 'NDIxODk2MTc2MDgyNjE2MzMw.DYdx6Q.ZSSXBSLwxOIXbFXvUPiz4apkPxg'

# These aren't needed with the Discord bot user.
# OAUTH2_REDIRECT_URI = 'http://localhost:5000/callback'
# AUTHORIZATION_BASE_URL = API_BASE_URL + '/oauth2/authorize'
# TOKEN_URL = API_BASE_URL + '/oauth2/token'


class DiscordOAuth2:
    """Provides methods that correspond with Discord OAuth2 API endpoints."""\

    def __init__(self, server=MPC_SERVER_ID):
        self.server = server
        self.session = requests.Session()
        self.session.headers.update({'Authorization': 'Bot %s' % BOT_TOKEN})

    def get(self, url):
        """Makes an HTTP GET request to a Discord API endpoint."""
        return self.session.get('%s%s' % (API_BASE_URL, url))

    def myself(self):
        """Gets Discord bot user information."""
        return self.get('/users/@me')

    def user(self, id):
        """Gets the user with the specified ID."""
        return self.get('/users/%s' % id)

    def guilds(self):
        """Gets list of guilds."""
        return self.get('/users/@me/guilds')

    def member(self, id):
        return self.get('/guilds/%s/members/%s' % (self.server, id))

    def guild(self):
        """Gets guild information."""
        return self.get('/guilds/%s' % self.server)

    def roles(self):
        """Gets guild roles."""
        return self.get('/guilds/%s/roles' % self.server)

    def members(self, limit=10, after=0):
        """Gets members of a guild."""
        url = '/guilds/%s/members?limit=%s&after=%s'
        return self.get(url % (self.server, limit, after))
