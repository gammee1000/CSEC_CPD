# Read input and split into four integers
s1, s2, s3, s4 = map(int, input().split())

# Use a set to find the unique colors
unique_colors = {s1, s2, s3, s4}

# The number of horseshoes to buy is 4 minus the number of unique colors
print(4 - len(unique_colors))
