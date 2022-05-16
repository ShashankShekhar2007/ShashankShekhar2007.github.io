class Library:
    def __init__(self, books_present, library_name):
        self.books_present = books_present
        self.library_name = library_name
        self.books_lent = {}

    def display_books(self):
        book_number = 1
        print('\nWe have rhe following books:-')
        for book in self.books_present:
            print(f" {book_number}.{book}")
            book_number += 1
        print('')

    def lend_book(self):
        user_name = input('\nWhat is your name = ')
        book_name = input('Which book you want to lend = ')

        if book_name in self.books_present:
            print(f'Okay !! We gave you the book "{book_name}".\n')
            self.books_present.remove(book_name)
            self.books_lent[book_name] = user_name

        else:
            print(f"\nWe don't have the book'{book_name}'.")
            print(f"It is currently lent by {self.books_lent[book_name]}.\n")

    def add_book(self):
        book_name = input('\nWhich book you want to add = ')
        print(f"Okay !! We'll add the book '{book_name}'.\n")
        self.books_present.append(book_name)

    def return_book(self):
        user_name = input('\nWhat is your name = ')
        book_name = input('Which book you want to return = ')
        if self.books_lent[book_name] == user_name:
            print(f"Okay !! We'll return {book_name.title()}.\n")
            self.books_present.append(book_name)
        else:
            print(f"We don't have any record about {book_name.title()}.\nTry to add this book.\n")
            for book, user in self.books_lent.items():
                print(f"Information Of Books:-\n{book} : {user}\n")


shashank_library = Library(['A Brief History of Time', 'Olympiad', 'Physics', 'Bio', 'Fault In Our Stars',
                            'Story Book', 'Mahabharat', 'Ramayan', 'Bhagwath Geeta', 'Quran', 'Bible',
                            'Discovery Of India'], 'Library Of Shashank')
while True:
    user_input = input(
        "What do you want:-\n'D' for 'Display', 'L' for 'Lend', 'A' for 'Add', 'R' for 'Return'\nEnter = ")
    if user_input.lower() == 'd':
        shashank_library.display_books()
    elif user_input.lower() == 'l':
        shashank_library.lend_book()
    elif user_input.lower() == 'a':
        shashank_library.add_book()
    elif user_input.lower() == 'r':
        shashank_library.return_book()
