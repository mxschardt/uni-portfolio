from src.views.user_view import IndexView


class DefaultController:
    
    def __init__(self):
        self.view = IndexView()

    def get_user_data(self):
        return self.view.render_page()