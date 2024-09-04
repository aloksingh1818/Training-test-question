def count_substring(main_string, sub_string):
    count = main_string.count(sub_string)
    return count


main_string = "A B C D C D C"
sub_string = "C D C"
result = count_substring(main_string, sub_string)
print(f"Sub_string '{sub_string}' occurs {result} times in the main string.")
