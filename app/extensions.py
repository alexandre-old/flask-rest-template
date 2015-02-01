from flask.ext.mongoengine import MongoEngine
db = MongoEngine()


from flask_jwt import JWT
jwt = JWT()


from flask.ext.restful import Api
api = Api()
