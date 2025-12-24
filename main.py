def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def get_word_count(book_text):
    words = book_text.split()
    num_words = len(words)
    return f"Found {num_words} total words"

def Main():
    print(get_word_count(get_book_text("books/frankenstein.txt")))
    
Main()