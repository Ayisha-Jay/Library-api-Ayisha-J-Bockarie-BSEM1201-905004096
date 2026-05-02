import asyncio
from typing import List, Optional
from datetime import datetime, timedelta


# Models

class Book:
    def __init__(self, id: int, title: str, author: str, category: str,
                 total_copies: int, available_copies: int):
        self.id = id
        self.title = title
        self.author = author
        self.category = category
        self.total_copies = total_copies
        self.available_copies = available_copies

    def __repr__(self):
        return f"{self.title} (Available: {self.available_copies}/{self.total_copies})"


class BorrowRequest:
    def __init__(self, user_id: int, book_id: int, days: int = 7):
        self.user_id = user_id
        self.book_id = book_id
        self.days = days


class ReturnRequest:
    def __init__(self, user_id: int, book_id: int):
        self.user_id = user_id
        self.book_id = book_id


class BorrowRecord:
    def __init__(self, user_id: int, book_id: int,
                 borrowed_on: datetime, due_date: datetime):
        self.user_id = user_id
        self.book_id = book_id
        self.borrowed_on = borrowed_on
        self.due_date = due_date
        self.returned = False
        self.fine = 0.0


class ExtendRequest:
    def __init__(self, user_id: int, book_id: int, extra_days: int = 3):
        self.user_id = user_id
        self.book_id = book_id
        self.extra_days = extra_days


# In-memory database

books: List[Book] = [
    Book(1, "OOP", "A. Bockarie", "Programming", 3, 3),
    Book(2, "Data Communication", "Jane Conteh", "Networking", 2, 2),
    Book(3, "Sound Production", "I. Muhammad", "Multimedia", 1, 1)
]

borrowed_records: List[BorrowRecord] = []

# Global lock for concurrency
lock = asyncio.Lock()


# Core Functions

async def get_books():
    await asyncio.sleep(0.1)
    return books


async def borrow_book(request: BorrowRequest):
    await asyncio.sleep(0.2)

    async with lock:
        for book in books:
            if book.id == request.book_id:

                if book.available_copies < 1:
                    return {"error": "No available copies"}

                for record in borrowed_records:
                    if (
                        record.user_id == request.user_id and
                        record.book_id == request.book_id and
                        not record.returned
                    ):
                        return {"error": "Already borrowed"}

                book.available_copies -= 1

                record = BorrowRecord(
                    request.user_id,
                    request.book_id,
                    datetime.now(),
                    datetime.now() + timedelta(days=request.days)
                )

                borrowed_records.append(record)

                return {
                    "message": "Borrowed successfully",
                    "due_date": record.due_date
                }

    return {"error": "Book not found"}


async def return_book(request: ReturnRequest):
    await asyncio.sleep(0.2)

    async with lock:
        for record in borrowed_records:
            if (
                record.user_id == request.user_id and
                record.book_id == request.book_id and
                not record.returned
            ):

                overdue_days = max((datetime.now() - record.due_date).days, 0)
                record.fine = overdue_days * 1000
                record.returned = True

                for book in books:
                    if book.id == request.book_id:
                        book.available_copies += 1

                return {"message": "Returned", "fine": record.fine}

    return {"error": "Record not found"}


async def add_book_copies(book_id: int, extra_copies: int):
    await asyncio.sleep(0.1)

    async with lock:
        for book in books:
            if book.id == book_id:

                if extra_copies <= 0:
                    return {"error": "Invalid number"}

                book.total_copies += extra_copies
                book.available_copies += extra_copies

                return {
                    "message": f"{extra_copies} copies added",
                    "total": book.total_copies,
                    "available": book.available_copies
                }

    return {"error": "Book not found"}


# TEST (Run this)

async def main():

    print("\n Initial Books:")
    print(await get_books())

    # Add copies
    print("\n Adding copies...")
    print(await add_book_copies(1, 2))

    # Multiple users borrowing at same time
    print("\n Multiple users borrowing...")

    tasks = [
        borrow_book(BorrowRequest(1, 1)),
        borrow_book(BorrowRequest(2, 1)),
        borrow_book(BorrowRequest(3, 1)),
        borrow_book(BorrowRequest(4, 1)),
    ]

    results = await asyncio.gather(*tasks)

    for r in results:
        print(r)

    print("\n Books after borrowing:")
    print(await get_books())

    # Returning
    print("\n Returning books...")
    print(await return_book(ReturnRequest(1, 1)))

    print("\n Final state:")
    print(await get_books())


# Run program
if __name__ == "__main__":
    asyncio.run(main())