from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect


class BaseView(View):
    def get(self, request):
        return HttpResponseRedirect('/discord/')


class NotFoundView(TemplateView):
    template_name = '404.html'

    def get_context_data(self, **kwargs):
        return {}
