import pytest
import sys
import os 

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from atividade07_db import User, Database, UserService

class MockDatabase(Database):
    def __init__(self):
        self.saved_user = None

    def save_user(self, user):
        self.saved_user = user

def test_save_user_valid():
    db = MockDatabase()
    service = UserService(db)
    user = User("John Doe", "john.doe@example.com")

    service.save_user(user)

    assert db.saved_user == user

def test_save_user_without_name():
    db = MockDatabase()
    service = UserService(db)
    user = User("", "john.doe@example.com")

    with pytest.raises(ValueError, match="User must have a name and email"):
        service.save_user(user)

def test_save_user_without_email():
    db = MockDatabase()
    service = UserService(db)
    user = User("John Doe", "")

    with pytest.raises(ValueError, match="User must have a name and email"):
        service.save_user(user)
