def generate_odd_series(n: int):
    result = [2 * i + 1 for i in range(n)]
    return result

a = int(input("Enter a number: "))

output = generate_odd_series(a)
print("Output:", ", ".join(map(str, output)))
