class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Database:
    def save_user(self, user):
        pass

class UserService:
    def __init__(self, db):
        self.db = db

    def save_user(self, user: User):
        if not user.name or not user.email:
            raise ValueError("User must have a name and email")
        self.db.save_user(user)
