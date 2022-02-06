

from flask import Flask
from flask_restx import Api
from config import Config
from models import Movie, Genre, Director
from setup_db import db
from views.directors.directors import directors_ns
from views.genres.genres import genres_ns
from views.movies.movies import movies_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.app_context().push()
    register_extensions(app)
    return app
#
#
# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(directors_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(genres_ns)
    create_data()


def create_data():
    movie_1 = Movie(
        id=1,
        title="First",
        description="Very short",
        trailer="Here",
        year=2021,
        rating=9.3,
        genre_id=1,
        director_id=1
    )
    movie_2 = Movie(
        id=2,
        title="Second",
        description="Very long",
        trailer="Absent",
        year=2022,
        rating=5.6,
        genre_id=2,
        director_id=2
    )

    genre_1 = Genre(id=1, name="Comedy")
    genre_2 = Genre(id=2, name="SciFi")

    director_1 = Director(id=1, name="Miss AppleBerry")
    director_2 = Director(id=2, name="J J")

    db.create_all()

    with db.session.begin():
        db.session.add_all([movie_1, movie_2])
        db.session.add_all([genre_1, genre_2])
        db.session.add_all([director_1, director_2])


if __name__ == '__main__':
    app = create_app(Config())
    app.run(host="localhost", port=10001, debug=True)



