def shift_characters(input_string):
    result = ""
    for character in input_string:
        if character == 'z':
            result = result + 'a'
        else:
            next_character = chr(ord(character) + 1)
            result = result + next_character
    return result