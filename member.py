class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def __str__(self):
        if len(self.borrowed_books) > 0:
            books_str = "|".join(self.borrowed_books)
        else:
            books_str = "None"
        
        return f"{self.member_id},{self.name},{self.email},{books_str}"