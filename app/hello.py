from flask import Flask, request, send_from_directory
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from flask.ext.login import LoginManager
 

import os, datetime

_basedir = os.path.abspath(os.path.dirname(__file__))
print datetime.datetime.now()


try:
    username = os.environ['user']
    password = os.environ['pass']
except KeyError as e:
    username = 'bogie'
    password = 'bogie'


app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(_basedir, 'bogie.db')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


class Logz(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True)
    systems = db.Column(db.String(50))
    components = db.Column(db.String(220))
    version = db.Column(db.String(220))
    timestamp = db.Column(db.DateTime, unique=True)
    source = db.Column(db.String(220))

    def __init__(self, systems=None, components=None, version=None, timestamp=None, source=None):
        self.systems = systems
        self.components = components
        self.version = version
        self.timestamp = timestamp
        self.source = source

    def __repr__(self):
        return "<'systems': %r, 'components': %r, 'version': %r, 'time': %r, 'source': %r>" % (
        self.systems, self.components, self.version, self.timestamp, self.source)

        # def __repr__(self):
        #     return {"systems": self.systems, "components": self.components, "version": self.version, "time": self.timestamp, "source": self.source}

class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id',db.Integer , primary_key=True)
    username = db.Column('username', db.String(20), unique=True , index=True)
    password = db.Column('password' , db.String(10))
    # email = db.Column('email',db.String(50),unique=True , index=True)
    registered_on = db.Column('registered_on' , db.DateTime)
 
    def __init__(self , username ,password , email):
        self.username = username
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()
 
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)
 
    def __repr__(self):
        return '<User %r>' % (self.username)




# later on
# db.init_app(app)


# db.drop_all()                                                                                                                               
# db.create_all()
# dummy = logz('dev', 'dummy',"2.0",datetime.datetime.now(),"dummySource")
# db.session.add(dummy)
# db.session.commit()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/current', methods=['GET'])
def current():
    query = db.session.query(Logz.components.distinct()).all()
    systms = db.session.query(Logz.systems.distinct()).all()
    print systms

    log = []
    for x in query:
        for y in systms:
            qs = Logz.query.filter_by(components=x[0], systems=y[0]).order_by(Logz.timestamp.desc(), Logz.systems).first()
            if qs is not None:
                log.append(qs)
            # print x[0]
            # log.append(Logz.query.filter_by(components=x[0]).order_by(Logz.timestamp.desc()).first())
    return render_template('current.html', list_of_items=log)


@app.route('/current/components/<string:components>', methods=['GET'])
def current_comp(components):
    query = db.session.query(Logz.systems.distinct()).filter_by(components=components).all()
    log = []
    for x in query:
        qs = Logz.query.filter_by(systems=x[0], components=components).order_by(Logz.timestamp.desc()).first()
        if qs is not None:
            log.append(qs)
        
    return render_template('current.html', list_of_items=log)


@app.route('/current/systems/<string:systems>', methods=['GET'])
def current_sys(systems):
    query = db.session.query(Logz.components.distinct()).filter_by(systems=systems).all()
    log = []
    for x in query:
        # print x[0]
        qs =Logz.query.filter_by(components=x[0], systems=systems).order_by(Logz.timestamp.desc()).first()
        if qs is not None:
            log.append(qs)

    return render_template('current.html', list_of_items=log)


# @app.route('/get',methods = ['GET'])
@app.route('/logs', methods=['GET'])
def get_logs():
    log = Logz.query.order_by(Logz.timestamp.desc()).all()
    return render_template('hello.html', list_of_items=log)


@app.route('/logs/<string:components>', methods=['GET'])
def get__component_logs(components):
    list_of_items = Logz.query.filter_by(components=components).order_by(Logz.timestamp.desc())
    return render_template('hello.html', list_of_items=list_of_items)


@app.route('/syslogs/<string:systems>', methods=['GET'])
def get__system_logs(systems):
    list_of_items = Logz.query.filter_by(systems=systems).order_by(Logz.timestamp.desc())
    return render_template('hello.html', list_of_items=list_of_items)



@app.route('/test', methods=['GET'])
def test():
    val = username + " " + password
    return render_template('test.html', value=val)


class TodoSimple(Resource):
    def put(self, ):
        systems = request.form['systems']
        components = request.form['components']
        version = request.form['version']
        timestamp = datetime.datetime.utcnow()
        source = request.form['source']
        u = Logz(systems, components, version, timestamp, source)
        db.session.add(u)
        db.session.commit()
        return {'done': True}
        # return "{'systems': %s, 'components': %s, 'version': %s, 'time': %s, 'source': %s}"% systems,components,version,time,source

    def post(self):
        components = request.form['components']
        version = request.form['version']
        systems = request.form['systems']
        timestamp = request.form['timestamp']
        source = request.form['source']
        nextz = request.form['next']
        u = Logz.query.filter_by(systems=systems, components=components, version=version, timestamp=timestamp,
                                 source=source).first()
        if u is not None:
            db.session.delete(u)
            db.session.commit()
            # return {'status':True}
            return redirect('/' + nextz)
        return {'status': False}


# @app.route('/delete', methods=['POST'])
# def deleting():



api.add_resource(TodoSimple, '/update')

if __name__ == '__main__':
    if not os.path.exists('bogie.db'):
        db.create_all()
    app.run(debug=True)



    # from database import db_session
    # from models import log
    # u = User('admin', 'admin@localhost')
    # db_session.add(u)
    # db_session.commit()


    # put('http://localhost:5000/update', data={'systems':'systems', 'components': 'components', 'version': 'version', 'source': 'source'})

    # get('http://localhost:5000/get')
