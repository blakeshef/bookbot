def count_words(input_string):
    return len(input_string.split())

def count_chars(input_string):
    count_dict = {}
    for character in input_string:
        count_dict.setdefault(character.lower(), 0)
        count_dict[character.lower()] += 1
    return count_dict

def sort_count(input_dict):
    sorted_dict = []
    for character, count in input_dict.items():
        if character.isalpha():
            sorted_dict.append({"char": character, "num": count})
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict

def sort_on(items):
    return items["num"]