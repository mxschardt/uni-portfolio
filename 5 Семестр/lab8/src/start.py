from flask import Flask

from src.controllers import DefaultController, StoreUserController, UserController
from src.models import MaximSchardt
from src.views import UserView

app = Flask(__name__)


@app.route('/')
def index():
    controller = DefaultController()
    return controller.get_user_data()


@app.route('/mx')
def user():
    model = MaximSchardt()
    view = UserView()
    controller = UserController(model, view)
    return controller.get_user_data()


@app.route('/json')
def json():
    model = MaximSchardt()
    controller = StoreUserController(model)
    return controller.get_user_data()