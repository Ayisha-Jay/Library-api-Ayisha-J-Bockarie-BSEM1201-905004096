
An asynchronous Python-based Library Management System that simulates real-world library operations such as borrowing, returning books, inventory management, and concurrent user handling.

Library Management System (Async Python)
📌 Project Overview

This project is a Library Management System built using asynchronous Python programming.
It simulates real-world library operations such as borrowing, returning books, managing inventory, and handling multiple users concurrently.

The system uses:

asyncio for concurrency
In-memory data structures (no database)
Locking mechanism to prevent race conditions
🚀 Features
📖 Book Management
View all books
Add extra copies to existing books
Track total and available copies
👥 User Operations
Borrow books
Return books
Prevent double borrowing by same user
⚡ Concurrency Support
Multiple users can borrow books at the same time
Safe data handling using asyncio.Lock
💰 Fine System
Automatic fine calculation for overdue books
Fine = overdue days × 1000

🏗️ Project Structure
library-system/
│
├── library_async.py   # Main program (all logic + demo)
├── README.md          # Project documentation
└── demo_output.txt    # (optional) output file from demo
🧠 How It Works

The system uses:

🔹 Async Functions

All operations are asynchronous:

borrow_book()
return_book()
add_book_copies()
🔹 Concurrency Control

A global lock ensures safe updates:

lock = asyncio.Lock()

This prevents:

Double borrowing
Incorrect book counts
Race conditions
▶️ How to Run
1. Install Python

Make sure Python 3.8+ is installed.

2. Run the program
python library_async.py
🎬 Demo Output

The program includes a built-in demo that:

Displays initial books
Adds extra copies
Simulates multiple users borrowing at the same time
Processes returns
Shows final system state
📊 Example Output
Initial Books:
OOP (Available: 3/3)

Adding copies...
{'message': '2 copies added', 'total': 5, 'available': 5}

Multiple users borrowing...
User 1: Borrowed successfully
User 2: Borrowed successfully
User 3: Borrowed successfully
User 4: No available copies

Final state:
OOP (Available: 1/5)
🧪 Technologies Used
Python 3
asyncio (asynchronous programming)
datetime module
OOP (Object-Oriented Programming)
📌 Key Concepts Demonstrated
Asynchronous programming
Concurrency handling
Shared resource protection (locks)
Object-oriented design
In-memory data systems
🔒 Safety Mechanism

To ensure data integrity:

All modifications to books and records are protected using asyncio.Lock
Prevents race conditions during simultaneous user actions. 

