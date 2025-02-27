num = int(input("Enter a starting number: "))

# Keep doubling until it reaches or exceeds 1000
while num < 1000:
    num *= 2
    print("Doubled:", num)