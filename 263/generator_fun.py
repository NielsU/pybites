def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


for i in infinite_sequence():
    print(i)
    if i > 10:
        break
