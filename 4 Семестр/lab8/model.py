from orator import Model


class User(Model):
    __table__ = 'users'
    __timestamps__ = False
