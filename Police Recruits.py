# Read input
n = int(input())
events = list(map(int, input().split()))

# Initialize variables
officers = 0
untreated_crimes = 0

# Process events
for event in events:
    if event == -1:  # A crime occurs
        if officers > 0:
            officers -= 1  # An officer handles the crime
        else:
            untreated_crimes += 1  # No officer available
    else:
        officers += event  # Recruit new officers

# Output the number of untreated crimes
print(untreated_crimes)
