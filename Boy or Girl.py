username = input().strip()  # Read the input string and remove any extra spaces
distinct_chars = set(username)  # Use a set to store distinct characters

if len(distinct_chars) % 2 == 0:
    print("CHAT WITH HER!")  # Even number of distinct characters → Female
else:
    print("IGNORE HIM!")  # Odd number of distinct characters → Male
