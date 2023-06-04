from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash
import datetime

class Recipe:
    db = "recipes_ajax_schema" 
    
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.dated_at = data['dated_at']
        self.minute_at = data['minute_at']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.chef = None


# crud method: create 
    @classmethod 
    def save_recipe(cls, data):
        query = """ 
            INSERT INTO recipes
            (name, description, instruction, dated_at, minute_at, user_id)
            VALUES (%(name)s, %(description)s, %(instruction)s, %(dated_at)s, %(minute_at)s, %(user_id)s);
        """
        return connectToMySQL(cls.db).query_db(query, data)


# read
# combine get all recipes with get user with recipes
    @classmethod 
    def get_all_recipes(cls):
        query = """ 
            SELECT * FROM recipes
            JOIN users ON recipes.user_id = users.id;
        """
        results = connectToMySQL(cls.db).query_db(query)

        all_recipes = [] # appending inside the list

        for row in results:
            one_recipe = cls(row)

            user_data = {
                'id': row['users.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'password' : row['password'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.updated_at'],
            }
            one_recipe.chef = user.User(user_data) # storing the data of user in chef var
            all_recipes.append(one_recipe) # passing one recipe through the list
        return all_recipes

# get one recipe 
# list in user will now have one recipe 
    @classmethod 
    def get_one_recipe(cls, data):
        query = """ 
            SELECT * FROM recipes
            JOIN users ON recipes.user_id = users.id
            WHERE recipes.id = %(id)s;
        """

        results = connectToMySQL(cls.db).query_db(query, data)

        one_recipe = cls(results[0])

        user_data = {
                'id': results[0]['users.id'],
                'first_name' : results[0]['first_name'],
                'last_name' : results[0]['last_name'],
                'email' : results[0]['email'],
                'password' : results[0]['password'],
                'created_at' : results[0]['users.created_at'],
                'updated_at' : results[0]['users.updated_at'],
            }
        one_recipe.chef = user.User(user_data)

        return one_recipe


# update
    @classmethod 
    def update_recipe(cls, data):
        query = """ 
            UPDATE recipes
            SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, dated_at = %(dated_at)s, minute_at = %(minute_at)s
            WHERE id = %(id)s;
        """

        return connectToMySQL(cls.db).query_db(query, data) 


# delete
    @classmethod 
    def delete_recipe(cls, data):
        query = """ 
            DELETE FROM recipes
            WHERE id = %(id)s;
        """

        return connectToMySQL(cls.db).query_db(query, data) 


# validation
    @staticmethod 
    def validate_recipe(data):
        is_valid = True

# validate_name ->
        if len(data['name']) == 0:
            is_valid = False
            flash('Name can not be left empty', 'recipe')
# validate_description ->
        if len(data['description']) == 0:
            is_valid = False
            flash('Descriptions can not be left empty', 'recipe')
# validate_instruction ->
        if len(data['instruction']) == 0:
            is_valid = False
            flash('Instructions can not be left empty', 'recipe')
# validate_dated_at ->
        if len(data['dated_at']) == 0:
            is_valid = False
            flash('Date option can not be left empty', 'recipe')
# validate_minute_at ->
        if 'minute_at' not in data:
            is_valid = False
            flash('Minute option must be selected', 'recipe')
        return is_valid


