# encoding:utf-8
import hashlib as hl
import sqlite3 as sql

class User:
    def __init__(self, username="", password="", admin=False):
        self.username = username
        self.password = password
        self.admin = admin
        
    def is_valid(self):
        return self.password!="" and self.username!="" and (self.admin is True or self.admin is False)
    
    def __str__(self):
        return f"User(username={self.username}, admin={self.admin})"

class UserDao:
    connection = sql.connect("../db.sqlite3")    
    @staticmethod
    def add_user(user):
        if not user.is_valid():
            return False
        cursor = UserDao.connection.cursor() 
        user.password = hl.sha256(user.password.encode('utf-8')).hexdigest()
        cursor.execute("insert into users values (?, ?, ?)", (user.username, user.password, user.admin))
        cursor.execute("commit")
        return True
    
    @staticmethod
    def get_user(username, password):
        cursor = UserDao.connection.cursor()
        password = hl.sha256(password.encode('utf-8')).hexdigest()
        user = None
        row = cursor.execute("Select * from users where username=? and password=?", (username, password)).fetchone()
        if row is not None:
            user = User(row[0], row[1])
        return user
