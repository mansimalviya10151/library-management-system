import sys
from src.library_service import LibraryService

def main():
    service = LibraryService()

    while True:
        print("\n========================================")
        print("  LIBRARY MANAGEMENT SYSTEM (CLI)")
        print("========================================")
        print("1. Add New Book")
        print("2. Register New User")
        print("3. View All Books")
        print("4. Borrow a Book")
        print("5. Return a Book")
        print("6. Exit")
        print("========================================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            b_id = input("Enter Book ID: ").strip()
            title = input("Enter Title: ").strip()
            author = input("Enter Author: ").strip()
            category = input("Enter Category: ").strip()
            success, msg = service.add_book(b_id, title, author, category)
            print(f"\nResult: {msg}")

        elif choice == "2":
            u_id = input("Enter User ID: ").strip()
            name = input("Enter Name: ").strip()
            role = input("Enter Role (Admin/Member): ").strip() or "Member"
            success, msg = service.add_user(u_id, name, role)
            print(f"\nResult: {msg}")

        elif choice == "3":
            books = service.get_all_books()
            print("\n---------------- LIST OF BOOKS ----------------")
            if not books:
                print("No books available in the system.")
            for b in books:
                status = f"Borrowed by {b.borrower_id} (Due: {b.due_date})" if b.is_borrowed else "Available"
                print(f"[{b.book_id}] {b.title} by {b.author} | Category: {b.category} | Status: {status}")

        elif choice == "4":
            b_id = input("Enter Book ID to borrow: ").strip()
            u_id = input("Enter User ID: ").strip()
            success, msg = service.borrow_book(b_id, u_id)
            print(f"\nResult: {msg}")

        elif choice == "5":
            b_id = input("Enter Book ID to return: ").strip()
            success, msg = service.return_book(b_id)
            print(f"\nResult: {msg}")

        elif choice == "6":
            print("\nExiting Library Management System. Goodbye!")
            sys.exit(0)

        else:
            print("\nInvalid choice! Please select an option between 1 and 6.")

if __name__ == "__main__":
    main()