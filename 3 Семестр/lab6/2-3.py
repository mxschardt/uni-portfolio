import os
from pymongo import MongoClient


class MongoDBConnectionContextManager:
    def __init__(self, username, password, host, port):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(
            self.host, self.port,
            username=self.username, password=self.password,
            authMechanism='SCRAM-SHA-1'
        )
        return self

    def __exit__(self, *args):
        self.connection.close()


def init_db():
    username = os.environ.get('DB_USERNAME')
    password = os.environ.get('DB_PASSWORD') 
    host = os.environ.get('DB_HOST') or 'localhost'
    port = os.environ.get('DB_PORT') or 27017
    return MongoDBConnectionContextManager(username, password, host, port)


if __name__ == '__main__':
    db = init_db()
    with db:
        collection = db.connection['myshinynewdb']['user']
        user = collection.find_one({'age': 205})
        print(user)
