# Read input
a, b = map(int, input().split())

# Count years
years = 0
while a <= b:
    a *= 3
    b *= 2
    years += 1

# Output result
print(years)
