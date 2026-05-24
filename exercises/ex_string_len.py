str_list = ["asd", "fgsdfafasf", "g", "gsdf", "fdhxcvxcv", "aweafafasf",
            "b", "d", "asd", "sdfgfdg"]

def five_char_list(strings_list):
    result = []
    for string in strings_list:
        if len(string) > 5:
            result.append(string)
    return result

print(five_char_list(str_list))