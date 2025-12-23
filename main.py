def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def Main():
    print(get_book_text("books/frankenstein.txt"))
    

Main()