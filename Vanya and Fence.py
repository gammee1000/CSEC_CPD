# Read inputs
n, h = map(int, input().split())
heights = list(map(int, input().split()))

# Calculate total width
total_width = 0
for ai in heights:
    if ai > h:
        total_width += 2  # Bends down
    else:
        total_width += 1  # Walks normally

# Output the result
print(total_width)

