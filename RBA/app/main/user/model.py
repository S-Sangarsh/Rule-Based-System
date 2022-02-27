from .. import db, flask_bcrypt
import datetime
from app.main import db
from sqlalchemy.exc import SQLAlchemyError




class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email_id = db.Column(db.String(255),unique=True, nullable=False)
    mobile_number = db.Column(db.String(255),unique=True)
    role_id = db.Column(db.Integer, nullable=False)
    password_hash=db.Column(db.String(255))
    created_on  = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    user_status = db.Column(db.String(100),default="Active")


    @staticmethod   # get a particular user_id
    def getByUserID(email_id):
        try:
            return User.query.filter_by(email_id=email_id.strip()).first()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            raise Exception(error)
            return False
     
    
    @staticmethod   # commit and add to the database
    def saveUser(data):
        try:
            db.session.add(data)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            raise Exception(error)
            return False
     
            
    
    @staticmethod   # commit the change only
    def commitUser():
        try:
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            raise Exception(error)
            return False
     
    
    
    @staticmethod
    def getalluser():
        try:
            return User.query.all()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            raise Exception(error)
            return False
        
    @staticmethod
    def pagination(page):
        try:
            page = int(page)
            user = db.session.query(User).paginate(page=page,per_page=3)
            return user.items
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            raise Exception(error)
            return False
            
    
    
    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter   # this setter for generate hashed password
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    #def check_password(self, password):
        #return flask_bcrypt.check_password_hash(self.password_hash, password)