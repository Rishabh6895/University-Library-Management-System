from models.book import Book

filename = "data/books.txt"
all_books = []

def load_books():
    all_books.clear()
    try:
        f = open(filename, "r")
        lines = f.readlines()
        f.close()
        
        for line in lines:
            line = line.strip()
            if line != "":
                parts = line.split(",") 
                b = Book(parts[0], parts[1], parts[2], parts[3])
                all_books.append(b)
                
    except FileNotFoundError:
        print("Book file not found. Starting with empty library.")

def save_books():
    f = open(filename, "w")
    for book in all_books:
        f.write(str(book) + "\n")
    f.close()

def add_new_book(b_id, title, author, qty):
    new_b = Book(b_id, title, author, qty)
    all_books.append(new_b)
    save_books()
    print(">> Success: Book added to library!")

def show_books():
    print("\n--- List of Books ---")
    print(f"{'ID':<10} {'Title':<20} {'Author':<20} {'Qty'}")
    print("-" * 60)
    for b in all_books:
        print(f"{b.book_id:<10} {b.title:<20} {b.author:<20} {b.quantity}")
    print("-" * 60)

def get_book_by_id(b_id):
    for b in all_books:
        if b.book_id == b_id:
            return b
    return None