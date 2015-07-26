from flask import Flask, request,send_from_directory
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for


import os,datetime
_basedir = os.path.abspath(os.path.dirname(__file__))
print datetime.datetime.now()

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(_basedir, 'bogie.db')

db = SQLAlchemy(app)

class Logz(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True)
    systems = db.Column(db.String(50))
    components = db.Column(db.String(220))
    version = db.Column(db.String(220))
    timestamp = db.Column(db.DateTime,unique=True)
    source = db.Column(db.String(220))

    def __init__(self,systems=None,components=None,version=None,timestamp=None,source=None):
        self.systems = systems
        self.components = components
        self.version = version
        self.timestamp = timestamp
        self.source = source

    def __repr__(self):
        return "<'systems': %s, 'components': %s, 'version': %s, 'time': %s, 'source': %s>" % self.systems,self.components,self.version,self.timestamp,self.source
    
    def __str__(self):
        return "{'systems': %s, 'components': %s, 'version': %s, 'time': %s, 'source': %s}" % self.systems,self.components,self.version,self.timestamp,self.source
    
    # def __repr__(self):
    #     return {"systems": self.systems, "components": self.components, "version": self.version, "time": self.timestamp, "source": self.source}



class Current(db.Model):
    __tablename__ = 'current'
    id = db.Column(db.Integer, primary_key=True)
    systems = db.Column(db.String(50))
    components = db.Column(db.String(220),unique=True)
    version = db.Column(db.String(220))
    timestamp = db.Column(db.String(220),unique=True)
    source = db.Column(db.String(220))

    def __init__(self,id=None,systems=None,components=None,version=None,timestamp=None,source=None):
        self.id = id
        self.systems = systems
        self.components = components
        self.version = version
        self.timestamp = timestamp
        self.source = source

    def __repr__(self):
        return {"systems": self.systems, "components": self.components, "version": self.version, "time": self.timestamp, "source": self.source}



# later on
# db.init_app(app)


# db.drop_all()                                                                                                                               
# db.create_all()
# dummy = logz('dev', 'dummy',"2.0",datetime.datetime.now(),"dummySource")
# db.session.add(dummy)
# db.session.commit()

# @app.route('/get',methods = ['GET'])
@app.route('/logs', methods=['GET'])
def get_logs():
    log = Logz.query.order_by(Logz.timestamp.desc()).all()
    return render_template('hello.html',list_of_items=log)

@app.route('/logs/<string:components>', methods=['GET'])
def get__component_logs(components):
    list_of_items = Logz.query.filter_by(components=components).order_by(Logz.timestamp.desc())
    return render_template('hello.html',list_of_items=list_of_items)

@app.route('/syslogs/<string:systems>', methods=['GET'])
def get__system_logs(systems):
    list_of_items = Logz.query.filter_by(systems=systems).order_by(Logz.timestamp.desc())
    return render_template('hello.html',list_of_items=list_of_items)


class TodoSimple(Resource):
    def put(self, param):
        systems = request.form['systems']
        components = request.form['components']
        version = request.form['version']
        timestamp = datetime.datetime.utcnow()
        source = request.form['source']
        u = Logz(systems, components, version, timestamp, source)
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
        u = Logz.query.filter_by(systems=systems, components=components, version=version, timestamp=timestamp,source=source).first()
        if u is not None:
            db.session.delete(u)
            db.session.commit()
            # return {'status':True}
            return redirect('/logs')
        return {'status':False}



    
# @app.route('/delete', methods=['POST'])
# def deleting():



api.add_resource(TodoSimple, '/<string:param>')


if __name__ == '__main__':
    app.run(debug=True)



    # from database import db_session
    # from models import log
    # u = User('admin', 'admin@localhost')
    # db_session.add(u)
    # db_session.commit()


# put('http://localhost:5000/put', data={'systems':'systems', 'components': 'components', 'version': 'version', 'source': 'source'})

# get('http://localhost:5000/get')