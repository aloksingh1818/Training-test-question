def first_occurrence(main_string, sub_string):
    index = main_string.find(sub_string)
    return index


main_string = "Find the first occurrence of a substring."
sub_string = "first"
index = first_occurrence(main_string, sub_string)
print(f"The first occurrence of '{sub_string}' is at index {index}.")
