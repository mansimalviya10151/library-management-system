from datetime import datetime, timedelta

class Book:
    def __init__(self, book_id, title, author, category, is_borrowed=False, borrower_id=None, due_date=None):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.is_borrowed = is_borrowed
        self.borrower_id = borrower_id
        self.due_date = due_date

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "category": self.category,
            "is_borrowed": self.is_borrowed,
            "borrower_id": self.borrower_id,
            "due_date": self.due_date
        }

    @staticmethod
    def from_dict(data):
        return Book(
            data["book_id"],
            data["title"],
            data["author"],
            data["category"],
            data.get("is_borrowed", False),
            data.get("borrower_id"),
            data.get("due_date")
        )

class User:
    def __init__(self, user_id, name, role="Member"):
        self.user_id = user_id
        self.name = name
        self.role = role

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "role": self.role
        }

    @staticmethod
    def from_dict(data):
        return User(data["user_id"], data["name"], data.get("role", "Member"))