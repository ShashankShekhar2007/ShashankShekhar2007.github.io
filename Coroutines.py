import time


def searcher():
    time.sleep(3)
    f = open("Shashank Shekhar.txt", "r")
    book = f.read()
    # A infinite while loop containing keyword "yield" indicates that a function is coroutine.
    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book.")
        else:
            print("Your text is not in the book.")


search = searcher()
print("Search Started...")
next(search)
search.send("Shashank")
search.send("Steve")
# To close the coroutine you've to use "close" .
search.close()
