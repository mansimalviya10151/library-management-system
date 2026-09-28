from datetime import datetime, timedelta
from src.models import Book, User
from src.storage import StorageHandler
from src.utils import format_date, calculate_fine

class LibraryService:
    def __init__(self):
        self.storage = StorageHandler()
        self.books = self.storage.load_books()
        self.users = self.storage.load_users()

    def add_book(self, book_id, title, author, category):
        if any(b.book_id == book_id for b in self.books):
            return False, "Book ID already exists!"
        new_book = Book(book_id, title, author, category)
        self.books.append(new_book)
        self.storage.save_books(self.books)
        return True, "Book added successfully!"

    def add_user(self, user_id, name, role="Member"):
        if any(u.user_id == user_id for u in self.users):
            return False, "User ID already exists!"
        new_user = User(user_id, name, role)
        self.users.append(new_user)
        self.storage.save_users(self.users)
        return True, "User registered successfully!"

    def get_all_books(self):
        return self.books

    def borrow_book(self, book_id, user_id, days=14):
        book = next((b for b in self.books if b.book_id == book_id), None)
        user = next((u for u in self.users if u.user_id == user_id), None)

        if not book:
            return False, "Book not found!"
        if not user:
            return False, "User not found!"
        if book.is_borrowed:
            return False, "Book is currently borrowed by someone else!"

        due_date = datetime.now().date() + timedelta(days=days)
        book.is_borrowed = True
        book.borrower_id = user_id
        book.due_date = format_date(due_date)
        self.storage.save_books(self.books)
        return True, f"Book borrowed successfully! Due Date: {book.due_date}"

    def return_book(self, book_id):
        book = next((b for b in self.books if b.book_id == book_id), None)

        if not book or not book.is_borrowed:
            return False, "Book was not borrowed!"

        fine = calculate_fine(book.due_date)
        book.is_borrowed = False
        book.borrower_id = None
        book.due_date = None
        self.storage.save_books(self.books)

        msg = "Book returned successfully!"
        if fine > 0:
            msg += f" Overdue Fine: ₹{fine}"
        return True, msg