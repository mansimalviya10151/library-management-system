import json
import os
from src.models import Book, User

class StorageHandler:
    def __init__(self, books_file="data/books.json", users_file="data/users.json"):
        self.books_file = books_file
        self.users_file = users_file
        self._ensure_files()

    def _ensure_files(self):
        os.makedirs(os.path.dirname(self.books_file), exist_ok=True)
        if not os.path.exists(self.books_file):
            with open(self.books_file, 'w') as f:
                json.dump([], f)
        if not os.path.exists(self.users_file):
            with open(self.users_file, 'w') as f:
                json.dump([], f)

    def load_books(self):
        try:
            with open(self.books_file, 'r') as f:
                data = json.load(f)
                return [Book.from_dict(item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_books(self, books):
        with open(self.books_file, 'w') as f:
            json.dump([b.to_dict() for b in books], f, indent=4)

    def load_users(self):
        try:
            with open(self.users_file, 'r') as f:
                data = json.load(f)
                return [User.from_dict(item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_users(self, users):
        with open(self.users_file, 'w') as f:
            json.dump([u.to_dict() for u in users], f, indent=4)