from stats import get_word_count, get_char_count, dic_to_list

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def sort_on(items):
    return items["num"]

def Main():
    book_text = get_book_text("books/frankenstein.txt")
    char_dic = get_char_count(book_text)
    char_count = dic_to_list(char_dic)
    char_count.sort(key=sort_on, reverse=True)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(get_word_count(book_text))
    print("--------- Character Count -------")
    for i in range(len(char_count)-1):
        print(f"{char_count[i]["char"]}: {char_count[i]["num"]}")
    print("============= END ===============")
    
Main()