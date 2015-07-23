from flask import Flask, request,send_from_directory
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from models import db

import os,datetime
_basedir = os.path.abspath(os.path.dirname(__file__))
print datetime.datetime.now()

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(_basedir, 'bogie.db')

# db = SQLAlchemy(app)

# later on
db.init_app(app)


from models import logz


# db.drop_all()                                                                                                                               
# db.create_all()
# admin = Logs('dev', 'dummy',"2.0","23.23.22","source")
# db.session.add(admin)
# db.session.commit()

# @app.route('/get',methods = ['GET'])
@app.route('/api/v1.0/logs', methods=['GET'])
def get_logs():
    log = logz.query.all()
    return render_template('hello.html',list_of_items=log)

@app.route('/api/v1.0/logs/<string:components>', methods=['GET'])
def get__component_logs(components):
    list_of_items = logz.query.filter_by(components=components)
    return render_template('hello.html',list_of_items=list_of_items)


class TodoSimple(Resource):
    def put(self, param):
        systems = request.form['systems']
        components = request.form['components']
        version = request.form['version']
        timestamp = datetime.datetime.now()
        source = request.form['source']
        u = logz(systems, components, version, timestamp, source)
        db.session.add(u)
        db.session.commit()
        return {'done':True}
        # return "{'systems': %s, 'components': %s, 'version': %s, 'time': %s, 'source': %s}"% systems,components,version,time,source
    
    def post(self,param):
        components = request.form['components']
        version = request.form['version']
        systems = request.form['systems']
        timestamp = request.form['timestamp']
        source = request.form['source']
        u = logz.query.filter_by(systems=systems, components=components, version=version, timestamp=timestamp,source=source).first()
        if u is not None:
            db.session.delete(u)
            db.session.commit()
            # return {'status':True}
            return redirect('/api/v1.0/logs')
        return {'status':False}



    
# @app.route('/delete', methods=['POST'])
# def deleting():



api.add_resource(TodoSimple, '/api/v1.0/<string:param>')


if __name__ == '__main__':
    app.run(debug=True)



    # from database import db_session
    # from models import log
    # u = User('admin', 'admin@localhost')
    # db_session.add(u)
    # db_session.commit()


# put('http://localhost:5000/put', data={'systems':'systems', 'components': 'components', 'version': 'version', 'time': 'time', 'source': 'source'}).json()

# get('http://localhost:5000/get')