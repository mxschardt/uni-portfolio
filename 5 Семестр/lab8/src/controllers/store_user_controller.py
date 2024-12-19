import json


class StoreUserController:

    def __init__(self, model):
        self.model = model

    def get_user_data(self):
        return json.dumps(self.model.__dict__)