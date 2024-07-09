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
test_list = "julian and bob!"

# printing original list
print("Original list : " + str(test_list))
print(test_list[0:-1])


def rotate_all(string, n):

    direction = "Left"

    if n < 0:
        direction = "Right"
        n = 0 - n

    for _ in range(n):
        if direction == "Left":
            string = string[1:] + string[0]
        else:
            string = string[-1] + string[0:-1]

    return string


def rotate_by_lcomp(string, n):
    return str().join([string[(i + n) % len(string)] for i, x in enumerate(string)])


def rotate_by_slice(string, n):
    # effective rotations = number of desired rotations % length of string.
    n_eff = n % len(string)
    # print(n_eff)
    return string[n_eff:] + string[:n_eff]


print("listcomprehension enumerate")
print(rotate_by_lcomp(test_list, -100))


print("slice")
print(rotate_by_slice(test_list, -100))


print("rotate_all")
print(rotate_all(test_list, -100))
