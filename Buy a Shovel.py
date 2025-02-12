k, r = map(int, input().split())  # Read input values

for i in range(1, 11):  # Try buying 1 to 10 shovels
    total_cost = i * k
    if total_cost % 10 == 0 or total_cost % 10 == r:  # Check if it can be paid without change
        print(i)
        break
