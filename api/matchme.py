from django.http import HttpResponse, StreamingHttpResponse
from django.conf.urls import patterns, include, url
from framework import WeberView, matchme_algorithm
from django.http.response import Http404, HttpResponseBadRequest
import json
from django.views.decorators.csrf import csrf_exempt
from framework.matchme_algorithm import parse_sentence
from domainmodel.postmodel import Post
from domainmodel.usermodel import User


class MatchmeView(WeberView):
    def get(self, *args, **kwargs):
        query = kwargs['query']
        posts = Post.getAllDocumentsByFieldValue("keywords", query)
        resultset = [{'username':i['object']['username'],
                      'posttext':i['object']['text'],
                      'thumbnail':User.getByFieldValue("username", i['object']['username'])} for i in posts]
        response=HttpResponse(json.dumps(resultset))
        return response

    def post(self, *args, **kwargs):
        username = self.request.POST.get('username')
        posttext = self.request.POST.get('posttext')
        if not username:
            return HttpResponseBadRequest("No username")
        if not posttext:
            return HttpResponseBadRequest("No post text")
        
        words = parse_sentence(posttext)
        post_document = {
            "username":username,
            "text":posttext,
            "keywords":list(words)+posttext.split(),
        }
        
        post = Post()
        post.attrs=post_document
        post.save()
        
        response = HttpResponse(json.dumps(post_document))
        response["Access-Control-Allow-Origin"] = "*"
        return response


urlpatterns = patterns('',
url(r'^matchme/?(?P<query>[A-Za-z0-9]*)$',csrf_exempt(MatchmeView.as_view),name='matchme'),
)
