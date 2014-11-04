from domainmodel import Model
from weber.settings import weber_db

class Post(Model):
    collection_name = "weber_post"
    _kind = "domainmodel.usermodel.Post"
    _version = 1
