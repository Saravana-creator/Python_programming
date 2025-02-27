import math

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"The roots are real and different: {root1:.2f} and {root2:.2f}")
elif discriminant == 0:
    root = -b / (2 * a)
    print(f"The roots are real and the same: {root:.2f}")
else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
    print(f"The roots are complex: {real_part:.2f} ± {imaginary_part:.2f}i")
