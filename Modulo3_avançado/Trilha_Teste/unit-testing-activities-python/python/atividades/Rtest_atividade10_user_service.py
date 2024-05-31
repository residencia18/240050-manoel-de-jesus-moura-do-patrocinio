

# ----- ROTINA DE TESTE -------

# Obter informações de um usuário válido.
# Lidar com a situação quando um usuário não é encontrado.
# Mocking do serviço UserService para controlar o comportamento do método get_user_info.


import pytest
import sys
import os 

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from atividade10_user_service import User, UserService, UserManager

class MockUserService(UserService):
    def __init__(self, users):
        self.users = users

    def get_user_info(self, user_id):
        return self.users.get(user_id, None)

def test_fetch_user_info_valid():
    users = {
        1: User(1, "Alice"),
        2: User(2, "Bob")
    }
    mock_user_service = MockUserService(users)
    user_manager = UserManager(mock_user_service)
    
    user_info = user_manager.fetch_user_info(1)
    assert user_info.user_id == 1
    assert user_info.name == "Alice"
    
    user_info = user_manager.fetch_user_info(2)
    assert user_info.user_id == 2
    assert user_info.name == "Bob"

def test_fetch_user_info_user_not_found():
    users = {
        1: User(1, "Alice"),
        2: User(2, "Bob")
    }
    mock_user_service = MockUserService(users)
    user_manager = UserManager(mock_user_service)
    
    with pytest.raises(ValueError, match="User not found"):
        user_manager.fetch_user_info(3)
