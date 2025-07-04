def count_words(input_string):
    return len(input_string.split())

def count_chars(input_string):
    count_dict = {}
    for character in input_string:
        count_dict.setdefault(character.lower(), 0)
        count_dict[character.lower()] += 1
    return count_dict