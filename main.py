import sys
from stats import get_total_words, count_chars, sort_dict
def get_book_text(file_path):
    with open(file_path, encoding='utf-8') as f:
        return f.read()
    
def print_report(book, word_count, ch_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for d in ch_count:
        print(f"{d['char']}: {d['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) == 2:
        content = get_book_text(sys.argv[1])
        total_count = get_total_words(sys.argv[1])
        char_count = count_chars(content)
        char_list = sort_dict(char_count)
        print_report(sys.argv[1], total_count, char_list)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    
if __name__ == "__main__":
    main()