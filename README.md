University Library Management System

1. Project Overview

The University Library Management System is a console-based application designed to streamline the day-to-day operations of a university library. It allows librarians to manage the book inventory and tracks the borrowing history of students and faculty members. The system uses Object-Oriented Programming (OOP) principles and File Handling to ensure data persists between sessions.

2. Key Features

Book Management: Add new books, update stock, and view the complete catalog.

Member Management: Register new students/faculty members.

Circulation System: Issue books to members and handle returns.

Stock Validation: Automatically prevents issuing books if stock is zero.

Data Persistence: All records (books, members, transactions) are saved in text files, so no data is lost when the program closes.

3. Technologies Used

Language: Python 3.x

Core Concepts:

Object-Oriented Programming (Classes & Objects)

File I/O (Reading/Writing .txt files)

Exception Handling (Try/Except blocks)

Modular Architecture (Separation of concerns)

4. Project Structure

The project follows a modular design with 5-10 meaningful files:

main.py: The entry point of the application (Menu-driven interface).

models/: Contains the class definitions (Book, Member).

services/: Contains the business logic (book_ops, member_ops, transaction).

data/: Stores the text files (books.txt, members.txt).

5. How to Run

Clone the repository:

git clone <your-repo-link>


Navigate to the project directory:

cd "University Library Management System"


Run the application:

python main.py


6. Testing Instructions

To Test Adding a Book: Choose Option 1, enter details, and check data/books.txt to see the new entry.

To Test Issuing: Choose Option 4, enter a valid Member ID and Book ID. The book quantity will decrease by 1.
