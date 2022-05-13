from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    db = 'EmailValidationDB'

    def __init__( self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.db = 'EmailValidationDB'

    @staticmethod
    def validate_email(email):
        is_valid = True
        if len(email) < 4:
            flash("Email must be >= 4")
            is_valid = False
        if not emailRegex.match(email):
            flash('Invalid email addy')
            is_valid = False
        return is_valid

    @classmethod
    def read_all(cls):
        query = 'select * from email_addresses;'
        results = connectToMySQL('EmailValidationDB').query_db(query)
        return results
    
    @classmethod
    def insert(cls, data):
        query = """insert into email_addresses (email)
                    values(%(email)s)"""
        results = connectToMySQL('EmailValidationDB').query_db(query, data)
        return results
