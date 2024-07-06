''''def rotate(string, n):
    """Rotate characters in a string.
    Expects string and n (int) for number of characters to move.
    """

    return string[n:] + string[:n]


string = "1234567891"

print("string:" + str(len(string)))
print(str(-2 % len(string)))

print(rotate(string, 2))
print(rotate(string, -2))'''

# initializing list
test_list = [1, 4, 6, 7, 2]

# printing original list
print("Original list : " + str(test_list))


def rotate_by_lcomp(string, n):
    return [string[(i + n) % len(string)] for i, x in enumerate(string)]


print(rotate_by_lcomp("123456", 2))
print(rotate_by_lcomp("123456", -2))
