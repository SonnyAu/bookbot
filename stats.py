
def get_total_words(file_path):
    with open(file_path, encoding='utf-8') as f:
        book = f.read()
        return len(book.split())
    
def count_chars(book):

    chars = {}
    for c in book:
        char = c.lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1


    return chars

def sort_on(items):
    return items['num']

def sort_dict(char_dict):
    ch_dicts = []
    for ch, count in char_dict.items():
        if ch.isalpha():
            ch_dicts.append({"char": ch, "num": count})
        else:
            continue
    ch_dicts.sort(reverse=True, key=sort_on)
    return ch_dicts