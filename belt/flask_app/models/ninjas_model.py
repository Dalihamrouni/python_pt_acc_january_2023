from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojos_model
class Ninja:
    def __init__(self,data) :
        self.id=data['id']
        self.dojo_id=data['dojo_id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.age=data['age']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def new_ninja(cls,data):
        query="""insert into ninjas (dojo_id, first_name, last_name, age) values ( %(dojo_id)s , %(first_name)s, %(last_name)s, %(age)s);"""
        results=connectToMySQL("dojos_store").query_db(query,data)
        print(results)
        return results
    
    @classmethod
    def get_by_dojo(cls,data):
        query="""Select * from ninjas where dojo_id= %(id)s"""
        results=connectToMySQL("dojos_store").query_db(query,data)
       
        dojo_ninja=[]
        if results:
            for row in results:
               dojo_ninja.append(cls(row)) 
        return dojo_ninja   