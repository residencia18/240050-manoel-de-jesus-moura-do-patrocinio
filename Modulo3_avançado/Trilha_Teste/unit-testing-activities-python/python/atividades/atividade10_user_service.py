class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class UserService:
    def get_user_info(self, user_id):
        pass

class UserManager:
    def __init__(self, user_service):
        self.user_service = user_service

    def fetch_user_info(self, user_id):
        user_info = self.user_service.get_user_info(user_id)
        if not user_info:
            raise ValueError("User not found")
        return user_info
