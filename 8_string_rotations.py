def generate_rotations(input_string):
    result = []
    for index in range(len(input_string)):
        rotation = input_string[index:] + input_string[:index]
        result.append(rotation)
    return " ".join(result)

