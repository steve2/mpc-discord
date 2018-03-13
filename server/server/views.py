from django.views import View
from django.http import HttpResponseRedirect

class BaseView(View):
    def get(self, request):
        return HttpResponseRedirect('/discord/')