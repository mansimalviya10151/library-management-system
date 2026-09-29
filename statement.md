# Statement of Purpose & Scope

## Problem Statement
Keeping library records manually using paper registers leads to mistakes—it makes tracking available books, active borrowers, and overdue dates inefficient. I created this Library Management System as a lightweight CLI application to automate inventory management, track checkouts, and calculate late fines automatically.

## Scope of Project
- Complete CRUD operations for book inventory and student/user accounts.
- Automated calculation of 14-day return due dates and late penalties (₹5/day).
- Persistent state management using standard JSON files.

## Target Users
- Library Administrators / Staff: Managing stock, adding books, and monitoring records.
- Students / Members: Browsing available books, checking out items, and making returns.

## Key Features
- Add new titles and display the full book catalog.
- Register user accounts with distinct roles (Admin vs. Member).
- Borrow and return books with real-time fine calculation.