def get_num_words(text):
    num_words = 0
    for word in text.split():
        num_words += 1
    return num_words

def sort_on(text):
    return text['num']

def get_num_letters(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    char_dict = []
    for char, num in chars.items():
        char_dict.append({'char': char, 'num': num})
    char_dict.sort(reverse=True, key = sort_on)
    return char_dict




    
