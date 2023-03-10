from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app import DATABASE
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User :
    def __init__(self, data) :
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        # --                CRUD QUERIES                        

        # CREATE
    @classmethod
    def create_user(cls,data):
        query = """
            INSERT INTO users (first_name, last_name,email, password) 
            VALUES  (%(first_name)s, %(last_name)s,%(email)s, %(password)s) ;
        """
        # !!!! This query will return the ID of the new inserted user
        return connectToMySQL(DATABASE).query_db(query,data)
        
        # READ ONE  =  get one user by email
    @classmethod
    def get_by_email(cls, data):
        query = """
            SELECT * FROM users WHERE email = %(email)s;
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results)<1:
            return False
        return cls(results[0])
        
        # READ ONE  =  get one user by id
    @classmethod
    def get_by_id(cls, data):
        query = """
                SELECT * FROM users WHERE id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results)<1:
            return False
        return cls(results[0])

    # * VALIDATIONS
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['first_name'])<2:
            flash("First Name must be at least 2 characters","register")
            is_valid = False
        if len(data['last_name'])<2:
            flash("Last Name must be at least 2 characters" ,"register")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!" ,"register")
            is_valid = False
        elif User.get_by_email({'email':data['email']}):
            flash("Email already exist","register")
            is_valid = False
        if len(data['password'])<6:
            is_valid = False
            flash("Password must be more than 6" ,"register")
        elif data["confirm_password"] != data["password"]:
            is_valid = False
            flash("Password and Confirm Password must match","register")
        return is_valid
