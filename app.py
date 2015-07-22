from flask import Flask, request
from flask_restful import Resource, Api
from database import db_session
from models import Logs

app = Flask(__name__)
api = Api(app)
from database import init_db

#init_db()


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')

todos = {}


class TodoSimple(Resource):
    def get(self, param):
        if param == 'all':
            g = Logs.query.all()
            return g
        else:
            return 'param invalid. use all'

    def put(self, param):
        if param == 'put':
            systems = request.form['systems']
            components = request.form['components']
            version = request.form['version']
            time = request.form['time']
            source = request.form['source']
            u = Logs(systems, components, version, time, source)
            db_session.add(u)
            db_session.commit()
            return {"systems": systems, "components": components, "version": version, "time": time, "source": source}
        else:
            return 'param invalid. use put'

api.add_resource(TodoSimple, '/<string:param>')

if __name__ == '__main__':
    app.run(debug=True)



    # from database import db_session
    # from models import log
    # u = User('admin', 'admin@localhost')
    # db_session.add(u)
    # db_session.commit()


#put('http://localhost:5000/put', data={"systems":"systems", "components": "components", "version": "version", "time": "time", "source": "source"}).json()
