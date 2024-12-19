from dataclasses import dataclass
from datetime import date
import uuid


class Movie:
    # id: int
    # title: str
    # description: str
    # genre: str
    # age_rating: str  # G, PG, PG-13, R, R-17
    # release_date: date

    def __init__(self, title, desc, genre, age, release:
        self.id = uuid.uuid5()

class MovieModel:

    def __init__(self, database):
        self.database = database

    def create(self, title, desc, genre, age, release) -> int:
        movie = Movie(title, desc, genre, age, release)
        if self.database.movies.exists(movie):
            raise Exception("Такой фильм уже существует!")
        id = self.database.movies.add(movie)
        return id

    def delete():
        ...  # Удаление фильма

    def update():
        ...  # Обновление информации о фильме

    def get_all(self) -> list:
        return self.database.movies.to_list()

    def get_by_id(self, id) -> Movie:
        return self.database.movies.by_id(id)

    def get_by_title(self, title) -> Movie:
        ...  # Крутой алгоритм поиска фильма по названию

    def recommend(self, age, genre=None) -> Movie:
        ...  # Очень крутой алгоритм рекомендации фильма
        # в зависимости от возрастного рейтинга и жанра


class MovieController:

    def __init__(self, model, logger, validator):
        self.model = model
        self.logger = logger
        self.validator = validator

    def create(self, title, desc, age, release):
        try:
            self.validator.validate_title(title)
            ...  # Остальная валидация
        except ValidationError as e:
            self.logger.log(f"ERROR: Ошибка валидации: {e}")
            raise Exception("Ошибка валидации") from e
        else:
            id = self.model.create(title, desc, age, release)
            self.logger.log(f"INFO: Создан фильм '{title}' с id: {id}")

    def get_by_title(self, title):
        try:
            self.validator.validate_title(title)
        except ValidationError as e:
            self.logger.log(f"ERROR: Ошибка валидации: {e}")
            raise Exception("Ошибка валидации") from e
        else:
            movie = self.model.get_by_title(title)
            self.logger.log(f"INFO: Запрос фильма '{movie.title}'")
            return movie

    ...


class MovieViewPoster:

    def view(self, movie):
        return render_poster(movie)


class MovieViewHTML:

    def view(self, movie):
        return render_template("movie.html", movie)


class MovieListViewTimeline:

    def view(self, movies):
        return create_timeline(movies)


class MovieListJson:

    def view(self, movies):
        return json.dumps(movies)


app = Flask(__name__)


class MovieControllerRest:

    def __init__(self, controller, view):
        self.controller = controller
        self.view = MovieListJson()

    @app.route("/api/", methods=['GET'])
    def get(self, req, res):
        movies = self.controller.get_all()
        return self.view.view(movies)

    @app.route("/api/", methods=['POST'])
    def create(self, req, res):
        try:
            self.controller.create(req.body.title, req.body.desc, ...)
        except:
            res.status = 400
            return
        else:
            res.status = 201
            return

    @app.route("/api/", methods=['DELETE'])
    def delete(self, req, res):
        ...

    @app.route("/api/", methods=['PUT'])
    def update(self, req, res):
        ...


class MovieControllerHTML:

    def __init__(self, controller):
        self.controller = controller
        self.view = MovieViewHTML()

    def index(self):
        return render_template("index.html")

    def poster(self, id):
        id = self.model.get_by_id(id)
        return self.view.view(id)
