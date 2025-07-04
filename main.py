from stats import count_words
from stats import count_chars

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_string = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_string)
    print(f"{word_count} words found in the document")
    char_count = count_chars(book_string)
    print(char_count)

main()