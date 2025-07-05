from stats import count_words
from stats import count_chars
from stats import sort_count
import sys

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
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