from typing import List, Optional, Dict

class AuthenticationError(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code

def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class ResourceManager:
    def __init__(self, resource_name: str):
        self.resource_name = resource_name
        self.is_active = False

    def __enter__(self):
        self.is_active = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.is_active = False

    def get_status(self) -> str:
        return "Active" if self.is_active else "Inactive"

@log_execution
def process_transaction(user_id: int, amount: float) -> bool:
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    return True

class UserDatabase:
    def __init__(self):
        self.users: Dict[int, str] = {}

    def add_user(self, user_id: int, username: str) -> None:
        if user_id in self.users:
            raise AuthenticationError("User exists", 409)
        self.users[user_id] = username

    def find_user(self, user_id: int) -> Optional[str]:
        return self.users.get(user_id)