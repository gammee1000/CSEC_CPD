# Read input
a1, a2, a3, a4 = map(int, input().split())
s = input().strip()

# Create a list of calories corresponding to each strip
calories = [a1, a2, a3, a4]

# Calculate the total calories based on the game events
total_calories = sum(calories[int(c) - 1] for c in s)

# Output the total number of calories
print(total_calories)
