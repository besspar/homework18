from models import MovieSchema, Movie
from flask_restx import Resource, Namespace
from flask import request
from setup_db import db

movies_ns = Namespace("movies")

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route("/")
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        data = Movie.query
        if director_id is not None:
            data = data.filter(Movie.director_id == director_id)
        if genre_id is not None:
            data = data.filter(Movie.genre_id == genre_id)
        if year is not None:
            data = data.filter(Movie.year == year)
        result = data.all()
        return movies_schema.dump(result), 200

    def post(self):
        req_json = request.json
        new_movie = Movie(**req_json)
        with db.session.begin():
            db.session.add(new_movie)
        return "", 201


@movies_ns.route("/<int:mid>")
class MovieView(Resource):
    def get(self, mid):
        data = Movie.query.get(mid)

        if not data:
            return "", 404

        return movie_schema.dump(data), 200

    def put(self, mid):

        data = Movie.query.get(mid)
        req_json = request.json
        data.title = req_json.get("title")
        data.description = req_json.get("description")
        data.trailer = req_json.get("trailer")
        data.year = req_json.get("year")
        data.rating = req_json.get("rating")
        data.genre_id = req_json.get("genre_id")
        data.director_id = req_json.get("director_id")
        db.session.add(data)
        db.session.commit()
        return "", 204

    def delete(self, mid):
        data = Movie.query.get(mid)

        if not data:
            return "", 404

        db.session.delete(data)
        db.session.commit()
        return "", 204
