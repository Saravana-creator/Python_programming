num = int(input("Enter a number: "))

sign = (num >> 31) & 1 
if num == 0:
    print("The number is Zero.")
elif sign:
    print("The number is Negative.")
else:
    print("The number is Positive.")