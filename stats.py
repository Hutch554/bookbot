def get_word_count(book_text):
    words = book_text.split()
    num_words = len(words)
    return f"Found {num_words} total words"

def get_char_count(book_text):
    letter_instances = {}
    lc_book_text = book_text.lower()
    lc_char_text = list(lc_book_text)
    for char in lc_char_text:
        if letter_instances.get(char) == None:
            letter_instances[char] = 1
        else:
            letter_instances[char] += 1
    return letter_instances