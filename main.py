import services.book_ops as book_ops
import services.member_ops as member_ops
import services.transaction as transaction

def main():
    print("Loading data...")
    book_ops.load_books()
    member_ops.load_members()
    
    while True:
        print("\n" + "="*30)
        print(" LIBRARY MANAGEMENT SYSTEM ")
        print("="*30)
        print("1. Add New Book")
        print("2. Show All Books")
        print("3. Add New Member")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            bid = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            auth = input("Enter Author Name: ")
            qty = input("Enter Quantity: ")
            
            if qty.isdigit():
                book_ops.add_new_book(bid, title, auth, qty)
            else:
                print("Error: Quantity must be a number.")

        elif choice == '2':
            book_ops.show_books()

        elif choice == '3':
            mid = input("Enter Member ID: ")
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            member_ops.add_new_member(mid, name, email)

        elif choice == '4':
            mid = input("Enter Member ID: ")
            bid = input("Enter Book ID: ")
            transaction.issue_book(mid, bid)

        elif choice == '5':
            mid = input("Enter Member ID: ")
            bid = input("Enter Book ID: ")
            transaction.return_book(mid, bid)

        elif choice == '6':
            print("Exiting... Data has been saved.")
            break
        
        else:
            print("Invalid Option! Please try again.")

if __name__ == "__main__":
    main()