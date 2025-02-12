n = int(input())  # Read the number of magnets
magnets = [input().strip() for _ in range(n)]  # Read the magnet orientations

groups = 1  # At least one group exists
for i in range(1, n):
    if magnets[i] != magnets[i - 1]:  # If the current magnet differs from the previous one, a new group starts
        groups += 1

print(groups)  # Output the total number of groups
