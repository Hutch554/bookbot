from stats import get_word_count, get_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def Main():
    book_text = get_book_text("books/frankenstein.txt")
    char_count = get_char_count(book_text)
    print(get_word_count(book_text))
    for char in char_count:
        print(f"'{char}': {char_count[char]}")
        
    
Main()