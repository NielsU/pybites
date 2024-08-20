import itertools

x = [None] * 20
y = ["x"] * 10

grid = itertools.zip_longest(x, y)

print(list(grid))
