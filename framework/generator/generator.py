import urllib2
import json
import time
import random
from pymongo import MongoClient

randomuser = urllib2.urlopen('http://api.randomuser.me/?results=100')
results = json.loads(randomuser.read())
users=results['results']

uids=[i['seed'] for i in users]

fp=open('interests.txt','r')
interests = []
for i in fp:
    interests.append(i.strip())


db=MongoClient().weber

for user in users:
    friends=set(random.sample(uids,int(random.random()*10)))
    friends-set([user['seed']])

    user['friends']=list(friends)
    user['interests']=random.sample(interests,int(random.random()*20))
    db['weber_user'].insert({'_kind':'user','object':user})


