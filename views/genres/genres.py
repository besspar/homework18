from models import GenreSchema, Genre
from flask_restx import Resource, Namespace


genres_ns = Namespace("genres")

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route("/")
class GenresView(Resource):
    def get(self):
        all_genres = Genre.query.all()
        return genres_schema.dump(all_genres), 200

    # В этом задании не нужно, так что просто закомментирую
    # def post(self):
    #     req_json = request.json
    #     new_genre = Genre(**req_json)  # Можно было бы еще добавить проверку, что такого жанра нет
    #
    #     with db.session.begin():
    #         db.session.add(new_genre)
    #     return "", 201


@genres_ns.route("/<int:gid>")
class GenresView(Resource):
    def get(self, gid):
        data = Genre.query.get(gid)

        if not data:
            return "", 404

        return genre_schema.dump(data), 200
    # В этом задании не нужно, так что просто закомментирую
    # def put(self, gid):
    #     data = Genre.query.get(gid)
    #     req_json = request.json
    #     data.name = req_json.get("name")
    #     db.session.add(data)
    #     db.session.commit()
    #     return "", 204
    #
    # def delete(self, gid):
    #     data = Genre.query.get(gid)
    #
    #     if not data:
    #         return "", 404
    #
    #     db.session.delete(data)
    #     db.session.commit()
    #     return "", 204
