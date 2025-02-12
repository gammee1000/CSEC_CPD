# Read the 5x5 matrix and find the position of '1'
for i in range(5):
    row = list(map(int, input().split()))
    if 1 in row:
        x, y = i, row.index(1)  # Get the row and column of '1'
        break

# Calculate the number of moves to reach the center (2,2) (0-based index)
moves = abs(x - 2) + abs(y - 2)

# Output result
print(moves)
