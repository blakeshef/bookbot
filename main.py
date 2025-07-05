from stats import count_words
from stats import count_chars
from stats import sort_count

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_string = get_book_text(book_path)
    word_count = count_words(book_string)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    char_count = count_chars(book_string)
    sorted_dict = sort_count(char_count)
    print("--------- Character Count -------")
    for dict in sorted_dict:
        print(f"{dict["char"]}: {dict["num"]}")

main()