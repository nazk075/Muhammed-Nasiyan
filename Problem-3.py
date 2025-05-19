def generate_conditional_odd_series(n: int):
    count = n if n % 2 != 0 else n - 1  
    result = [2 * i + 1 for i in range(count)]
    return result

a = int(input("Enter a number: "))

output = generate_conditional_odd_series(a)
print("Output:", ", ".join(map(str, output)))