import sys

if len(sys.argv) < 3:
    print("Usage: python arithmetic.py <first_number> <second_number>")
    sys.exit(1)

a = float(sys.argv[1])
b = float(sys.argv[2])

print(f"First Number: {a}")
print(f"Second Number: {b}")
print(f"Sum: {a + b}")
