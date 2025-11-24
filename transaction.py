import services.book_ops as book_ops
import services.member_ops as member_ops

def issue_book(member_id, book_id):
    member = member_ops.get_member_by_id(member_id)
    book = book_ops.get_book_by_id(book_id)

    if member == None:
        print("Error: Member not found!")
        return
    
    if book == None:
        print("Error: Book not found!")
        return

    if book.quantity > 0:
        book.quantity = book.quantity - 1
        member.borrowed_books.append(book.book_id)
        
        book_ops.save_books()
        member_ops.save_members()
        print(f">> Book '{book.title}' issued to {member.name}.")
    else:
        print("Sorry, this book is out of stock.")

def return_book(member_id, book_id):
    member = member_ops.get_member_by_id(member_id)
    book = book_ops.get_book_by_id(book_id)

    if member and book:
        if book_id in member.borrowed_books:
            book.quantity = book.quantity + 1
            member.borrowed_books.remove(book_id)
            
            book_ops.save_books()
            member_ops.save_members()
            print(f">> Book '{book.title}' returned. Thank you!")
        else:
            print("Error: This member does not have this book.")
    else:
        print("Error: Invalid Member ID or Book ID.")