def insert_substring(main_string, sub_string, position):
    new_string = main_string[:position] + sub_string + main_string[position:]
    return new_string


main_string = "It is summer"
sub_string = "hot"
position = 7
result = insert_substring(main_string, sub_string, position)
print(f"Result: {result}")
