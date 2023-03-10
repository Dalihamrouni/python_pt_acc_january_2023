from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

from flask_app import DATABASE


class Recipe :
    def __init__(self, data) :
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.owner = user.User.get_by_id({'id':self.user_id}).first_name

        # --                CRUD QUERIES                        

        # CREATE
    @classmethod
    def create_recipe(cls,data):
        query = """
            INSERT INTO recipies (user_id,name, description,instructions, date_made,under_30) 
            VALUES  (%(user_id)s,%(name)s, %(description)s,%(instructions)s, %(date_made)s, %(under_30)s) ;
        """
        # !!!! This query will return the ID of the new inserted user
        return connectToMySQL(DATABASE).query_db(query,data)

    # READ ALL 
    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM recipies ;
        """
        query_1 = """
                SELECT * FROM recipies left Join users on recipies.user_id  = users.id;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        recipes= []
        for row in results:
            # recipe = cls(row)
            # recipe.owner = row['first_name']
            # recipes.append(recipe)
            recipes.append(cls(row))
        return recipes
    

    # READ ONE  =  get one  by id
    @classmethod
    def get_by_id(cls, data):
        query = """
                SELECT * FROM recipies WHERE id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results)<1:
            return False
        return cls(results[0])
    @classmethod
    def update_recipe(cls,data):
        query = """
            UPDATE recipies SET name = %(name)s, description = %(description)s, 
            instructions = %(instructions)s, date_made = %(date_made)s,under_30=%(under_30)s
            WHERE id = %(id)s ;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = """ DELETE FROM recipies WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    

    # * VALIDATIONS
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['name'])<2:
            flash("Name must be at least 3 characters")
            is_valid = False
        if len(data['description'])<2:
            flash("Description must be at least 3 characters")
            is_valid = False
        if len(data['instructions'])<6:
            is_valid = False
            flash("instructions must be more than 6" )
        if data["date_made"] == "":
            is_valid = False
            flash("Made Date must not be blank")
        return is_valid
