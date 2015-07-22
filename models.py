from sqlalchemy import Column, Integer, String , DateTime
from database import Base

class Logs(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True)
    systems = Column(String(50))
    components = Column(String(220))
    version = Column(String(220))
    timestamp = Column(DateTime,unique=True)
    source = Column(String(220))

    def __init__(self,id=None,systems=None,components=None,version=None,timestamp=None,source=None):
        self.id = id
        self.systems = systems
        self.components = components
        self.version = version
        self.timestamp = timestamp
        self.source = source

    def __repr__(self):
        return '<log system:%r components:%r version:%r timestamp:%r source:%r>' % (self.systems),(self.components),(self.version),(self.timestamp),(self.source)



class Current(Base):
    __tablename__ = 'current'
    id = Column(Integer, primary_key=True)
    systems = Column(String(50))
    components = Column(String(220),unique=True)
    version = Column(String(220))
    timestamp = Column(DateTime,unique=True)
    source = Column(String(220))

    def __init__(self,id=None,systems=None,components=None,version=None,timestamp=None,source=None):
        self.id = id
        self.systems = systems
        self.components = components
        self.version = version
        self.timestamp = timestamp
        self.source = source

    def __repr__(self):
        return '<log system:%r components:%r version:%r timestamp:%r source:%r>' % (self.systems),(self.components),(self.version),(self.timestamp),(self.source)

