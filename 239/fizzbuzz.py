def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "Fizz Buzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


out_str = ""

for i in range(0, 21, 1):
    fizz_out = fizzbuzz(i)

    if type(fizz_out) is str:
        fizz_out = f'"{fizz_out}"'

    out_str += f"({i},{fizz_out}),"

print(out_str, end="")
