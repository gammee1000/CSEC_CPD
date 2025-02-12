# Read input
n = int(input())
s = input().strip()

# Count adjacent stones with the same color
removals = sum(1 for i in range(1, n) if s[i] == s[i - 1])

# Output the result
print(removals)
