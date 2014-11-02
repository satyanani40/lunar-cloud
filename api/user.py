from django.http import HttpResponse, StreamingHttpResponse
from django.conf.urls import patterns, include, url
from framework import WeberView
from django.http.response import Http404
from domainmodel.usermodel import User
import json



class UserView(WeberView):
    def get(self, *args, **kwargs):
        print kwargs
        if 'username' in kwargs:
            if 'attr' in kwargs:
                pass
            else:
                username = kwargs.get('username','')
                user = User.getByFieldValue("user.username",username)
                if not user:
                    user = User.getByFieldValue("seed", username)
                response = HttpResponse(json.dumps({'object':user.attrs['object']}), content_type="application/json")
                response["Access-Control-Allow-Origin"] = "*"
                return response
        else:
            usernames = User.listUsers()
            response = HttpResponse(json.dumps({'users':[{'username':i} for i in usernames]}), content_type="application/json")
            response["Access-Control-Allow-Origin"] = "*"            
            return response

urlpatterns = patterns('',
url(r'^users$',UserView.as_view,name='userinfo'),
url(r'^users/?(?P<username>[A-Za-z0-9]*)$',UserView.as_view,name='userinfo'),
url(r'^users/(?P<username>[A-Za-z0-9]*)/?(?P<attr>[A-Za-z0-9]*)$',UserView.as_view,name='userinfo'),
)
