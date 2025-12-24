import sys
from stats import get_word_count, get_char_count, dic_to_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def sort_on(items):
    return items["num"]

def Main():
    book_text = get_book_text(sys.argv[1])
    char_dic = get_char_count(book_text)
    char_count = dic_to_list(char_dic)
    char_count.sort(key=sort_on, reverse=True)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(get_word_count(book_text))
    print("--------- Character Count -------")
    for i in range(len(char_count)-1):
        print(f"{char_count[i]["char"]}: {char_count[i]["num"]}")
    print("============= END ===============")
    
Main()