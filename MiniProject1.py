class Library:
    def __init__(self, list_of_books, _library_name):
        self.book_list = list_of_books
        self.library = _library_name
        self.lend_dict = {}

    def display_book(self):
        print('\nWe have the following books:-')
        num = 1
        for book in self.book_list:
            print(f'{num}.{book}')
            num=num+1
    def lend_book(self, user, book):
        if book not in self.lend_dict:
            self.lend_dict.update({book:user})
            self.book_list.remove(book)
            print(f"\nNote:-'{book.title()}' is given to '{user.title()}'.")
        else:
            print(f"Note:-Dear {user.title()}, the book you are searching for is already given to '{self.lend_dict[book]}'.")
    def add_book(self, book):
        self.book_list.append(book)
        print(f"Note:-'{book.title()}' has been added to our library.")
        
    def return_book(self, book):
        if book in self.lend_dict:
            del self.lend_dict[book]
            self.book_list.append(book)
            print(f"Note:-'{book.title()}' has been returned.")
        else:
            print("This book doesn't belong to us.")

if __name__== '__main__':
    my_library = Library(['A Brief History of Time', 'Olympiad', 'Physics', 'Bio', 'Fault In Our Stars',
                            'Story Book', 'Mahabharat', 'Ramayan', 'Bhagwath Geeta', 'Quran', 'Bible',
                            'Discovery Of India'], 'Library Of Shashank')
    print(f'Welcome to {my_library.library}')
    while True:
        user_input = input(
        "\nWhat do you want:-\n'D' for 'Display'\n'L' for 'Lend'\n'A' for 'Add'\n'R' for 'Return'\nEnter 'q' to Quit.\n\nYour Input = ")
        if user_input == 'q':
            quit()
        elif user_input.lower() == 'd':
            my_library.display_book()
        elif user_input.lower() == 'l':
            user_name = input('\nEnter your name = ')
            book_name = input('Enter book name = ')
            my_library.lend_book(user_name, book_name)
        elif user_input.lower() == 'a':
            book_name = input('\nEnter book name = ')
            my_library.add_book(book_name)
        elif user_input.lower() == 'r':
            book_name = input('\nEnter book name = ')
            my_library.return_book(book_name)