import asyncio

from library import BorrowRequest, ReturnRequest, add_book_copies, borrow_book, get_books, return_book


async def demo():

    print(" LIMKOKWING UNIVERSITY LIBRARY MANAGEMENT DEMO")


    # Step 1: Show initial books
    print("\n🔹 Step 1: Initial Books")
    books_list = await get_books()
    for b in books_list:
        print(b)

    # Step 2: Add copies
    print("\n Step 2: Adding 2 copies to 'OOP'")
    result = await add_book_copies(1, 2)
    print(result)

    print("\n Updated Books:")
    for b in await get_books():
        print(b)

    # Step 3: Multiple users borrowing
    print("\n🔹 Step 3: Multiple Users Borrowing Same Book")

    tasks = [
        borrow_book(BorrowRequest(1, 1)),
        borrow_book(BorrowRequest(2, 1)),
        borrow_book(BorrowRequest(3, 1)),
        borrow_book(BorrowRequest(4, 1)),
    ]

    results = await asyncio.gather(*tasks)

    print("\n Borrow Results:")
    for i, r in enumerate(results, start=1):
        print(f"User {i}: {r}")

    print("\n Books After Borrowing:")
    for b in await get_books():
        print(b)

    # Step 4: Returning books
    print("\n Step 4: Returning Book (User 1)")
    result = await return_book(ReturnRequest(1, 1))
    print(result)

    print("\n Books After Return:")
    for b in await get_books():
        print(b)

    # Step 5: Overdue simulation (optional explanation)
    print("\n Step 5: System Ready for Overdue Tracking")
    print("✔ Fine is calculated automatically if overdue")

    print("DEMO COMPLETE")
    