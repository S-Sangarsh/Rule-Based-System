from .. import db, flask_bcrypt
import datetime
from app.main import db
from sqlalchemy.exc import SQLAlchemyError

class Role(db.Model):
    """ Role Model for storing role related details """
    __tablename__ = "role"
    
    
    role_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    role_name = db.Column(db.String(255),unique=True,nullable=False)
    created_on = db.Column(db.DateTime,default=datetime.datetime.utcnow())
    role_status = db.Column(db.String(100), default="Active")
    
    @staticmethod   # get a particular user_id
    def getByRoleName(role_name):
        try:
            return Role.query.filter_by(role_name=role_name).first()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            raise Exception(error)
            return False
     
     
        
    @staticmethod
    def getallrole():
        try:
           return Role.query.all()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            raise Exception(error)
            return False
     
    @staticmethod   # commit and add to the database
    def saveRole(data):
        try:
            db.session.add(data)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            raise Exception(error)
            return False
        
        
    @staticmethod
    def getByRoleId(role_id):
        try:
            return Role.query.filter_by(role_id = role_id).first()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            raise Exception(error)
            return False
     
    @staticmethod   # commit the change only
    def commitRole():
        try:
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            raise Exception(error)
            return False
