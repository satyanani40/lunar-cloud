from domainmodel import Model
from weber.settings import weber_db

class User(Model):
    collection_name = "weber_user"
    _kind = "domainmodel.usermodel.User"
    _version = 1

    @classmethod
    def listUsers(self):
        users = weber_db.find_all_documents(self.collection_name)
        return [i['object']['user']['username'] for i in users]
