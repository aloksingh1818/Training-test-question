def access_string(string):
    i = 0
    print("Forward order:")
    while i < len(string):
        print(string[i], end=' ')
        i += 1

    i = len(string) - 1
    print("\nReverse order:")
    while i >= 0:
        print(string[i], end=' ')
        i -= 1


string = "Python"
access_string(string)
