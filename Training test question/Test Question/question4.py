def check_vowels(string):
    vowels = set('aeiouAEIOU')
    found_vowels = [char for char in string if char in vowels]
    return found_vowels


string = "Hello World"
vowels = check_vowels(string)
print(f"Vowels found in '{string}': {vowels}")
