def num_gen(num):
    while True:
        num += 1
        yield num


gen = num_gen(0)

for _ in range(3):
    print(next(gen))
