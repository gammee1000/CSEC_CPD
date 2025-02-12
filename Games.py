n = int(input())  # Read the number of teams
teams = [tuple(map(int, input().split())) for _ in range(n)]  # Read home and guest uniform colors

count = 0  # Counter for games where the host team wears guest uniform

# Iterate over all pairs of teams (i, j) where i is host and j is guest
for i in range(n):
    for j in range(n):
        if i != j and teams[i][0] == teams[j][1]:  # Host's home color matches guest's away color
            count += 1

print(count)  # Output the total count of such games
