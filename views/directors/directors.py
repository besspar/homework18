
from models import DirectorSchema, Director
from flask_restx import Resource, Namespace

from setup_db import db

directors_ns = Namespace("directors")

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        all_directors = Director.query.all()
        return directors_schema.dump(all_directors)
    # В этом задании не нужно, так что просто закомментирую
    # def post(self):
    #     req_json = request.json
    #     new_director = Director(**req_json)
    #
    #     with db.session.begin():
    #         db.session.add(new_director)
    #
    #     return "", 201


@directors_ns.route("/<int:did>")
class DirectorsView(Resource):
    def get(self, did):
        data = Director.query.get(did)

        if not data:
            return "", 404

        return director_schema.dump(data), 200
    # В этом задании не нужно, так что просто закомментирую
    # def put(self, did):
    #     data = Director.query.get(did)
    #     req_json = request.json
    #     data.name = req_json.get("name")
    #     db.session.add(data)
    #     db.session.commit()
    #     return "", 204
    #
    # def delete(self, did):
    #     data = Director.query.get(did)
    #
    #     if not data:
    #         return "", 404

        db.session.delete(data)
        db.session.commit()
