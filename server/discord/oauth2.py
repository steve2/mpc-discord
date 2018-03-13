import requests

OAUTH2_CLIENT_ID = '421896176082616330'
OAUTH2_CLIENT_SECRET = 'WnmljxCmCTir_0PmDwrIDf9gYmfze1i9'
API_BASE_URL = 'https://discordapp.com/api'
BOT_TOKEN = 'NDIxODk2MTc2MDgyNjE2MzMw.DYdx6Q.ZSSXBSLwxOIXbFXvUPiz4apkPxg'

# These aren't needed with the Discord Bot user.
# OAUTH2_REDIRECT_URI = 'http://localhost:5000/callback'
# AUTHORIZATION_BASE_URL = API_BASE_URL + '/oauth2/authorize'
# TOKEN_URL = API_BASE_URL + '/oauth2/token'

class DiscordOAuth2Session:
    def __init__(self, guild):
        self.guild = guild
        self.session = requests.Session()
        self.session.headers.update({ 'Authorization': 'Bot %s' % BOT_TOKEN })

    def get(self, url):
        return self.session.get('%s%s' % (API_BASE_URL, url))

    # Common Discord API Endpoints

    def me(self):
        """gets discord bot user information"""
        return self.get('/users/@me')

    def guilds(self):
        """gets list of guilds"""
        return self.get('/users/@me/guilds')

    def guild(self):
        """gets guild information"""
        return self.get('/guilds/%s' % self.guild)

    def roles(self):
        """gets guild roles"""
        return self.get('/guilds/%s/roles' % self.guild)

    def members(self, limit=10):
        """gets members of a guild"""
        return self.get('/guilds/%s/members?limit=%s' % (self.guild, limit))