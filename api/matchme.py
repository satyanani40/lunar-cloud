from django.http import HttpResponse, StreamingHttpResponse
from django.conf.urls import patterns, include, url
from framework import WeberView
from django.http.response import Http404

class MatchmeView(WeberView):
    def get(self, *args, **kwargs):
        pass
        return HttpResponse("")
    def post(self, *args, **kwargs):
        return HttpResponse("")


urlpatterns = patterns('',
url(r'^matchme/?(?P<username>[A-Za-z0-9]*)$',MatchmeView.as_view,name='matchme'),
)
