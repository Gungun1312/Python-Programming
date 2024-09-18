


def format_name(name):
    words = name.split()
    formatted_name = ' '.join([word.capitalize()[0] + '.' if i != len(words) - 1 else word.capitalize() for i, word in enumerate(words)])
    return formatted_name

input_name = "moHan dAs kaRAM chAND ganDHI"
output_name = format_name(input_name)
print(output_name)



