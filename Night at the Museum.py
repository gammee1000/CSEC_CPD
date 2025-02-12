s = input().strip()  # Read the input string
current = 'a'  # The initial position of the pointer is at 'a'
rotations = 0  # Counter for the number of rotations

for char in s:
    distance = abs(ord(char) - ord(current))  # Calculate direct distance
    rotations += min(distance, 26 - distance)  # Choose the shortest path (clockwise or counterclockwise)
    current = char  # Move the pointer to the current character

print(rotations)  # Output the minimum number of rotations
