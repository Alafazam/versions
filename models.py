from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()




class logz(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True)
    systems = db.Column(db.String(50))
    components = db.Column(db.String(220))
    version = db.Column(db.String(220))
    timestamp = db.Column(db.String(220),unique=True)
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

