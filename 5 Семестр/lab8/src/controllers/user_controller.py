class UserController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_user_data(self):
        user_data = self.model.get_fullname()
        return self.view.render_page(user_data)