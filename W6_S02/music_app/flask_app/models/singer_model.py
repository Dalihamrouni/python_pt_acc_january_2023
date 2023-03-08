from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import song_model # modules than models
class Singer:

    #constructor 
    def __init__(self, data_dict) :
        self.id = data_dict['id']
        self.image = data_dict['image']
        self.name = data_dict['name']
        self.nationality = data_dict['nationality']
        self.rate = data_dict['rate']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        # self.songs = song_model.Song.get_by_singer({'id':self.id})

        # CRUD Queries ==  CREATE READ UPDATE DELETE

        # ! All Queries Are CLASS METHODS

        #  - READ ALL
    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM singers ;
        """
        results  = connectToMySQL(DATABASE).query_db(query)
        # print(results)
        all_singers = []
        for row in results :
            all_singers.append(cls(row))
        return all_singers
    
    # CREATE
    @classmethod
    def create(cls,data):
        query = """
            INSERT INTO singers (name, image,nationality, rate) 
            VALUES (%(name)s, %(image)s,%(nationality)s, %(rate)s) ;
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(f" this is the return after INSERT one Singer == {result} ******** ")
        return result
    
    #  Read One 
    @classmethod
    def get_by_id(cls, data):
        query = """
            SELECT * FROM singers LEFT JOIN songs ON songs.singer_id = singers.id  WHERE singers.id  = %(id)s;
        """

        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) == 0:
            return None
        this_singer = cls(results[0])
        for row in results:
            song_data = {
                'id': row['songs.id'],
                'singer_id': row['singer_id'],
                'title': row['title'],
                'created_at': row['songs.created_at'],
                'updated_at': row['songs.updated_at']
            }
            this_song = song_model.Song(song_data)
            this_singer.songs.append(this_song)
        print("🎈"*20, "One Singer With **** ==  ", results, "🎈"*20)
        # ! init 
        # return this_singer
        return cls(results[0])
    

    # Update 
    @classmethod
    def update(cls, data):

        query = """
            UPDATE singers SET name = %(name)s, nationality = %(nationality)s, rate = %(rate)s, WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = """
            DELETE FROM singers WHERE id  = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)