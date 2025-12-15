import sys
from stats import get_num_words, get_num_letters

if not len(sys.argv) == 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    print(f'Found {num_words} total words')
    for item in num_letters:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}: {item["num"]}")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()
