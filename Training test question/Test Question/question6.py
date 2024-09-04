def substring_exists(main_string, sub_string):
    return sub_string in main_string


main_string = "Hello, how are you?"
sub_string = "how"
exists = substring_exists(main_string, sub_string)
print(f"Does the sub_string '{sub_string}' exist in the main string? \n {exists}")
