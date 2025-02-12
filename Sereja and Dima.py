# Read input
n = int(input())
cards = list(map(int, input().split()))

# Initialize scores
sereja_score, dima_score = 0, 0
turn_sereja = True  # Sereja starts first

# Play the game
left, right = 0, n - 1
while left <= right:
    if cards[left] > cards[right]:
        chosen_card = cards[left]
        left += 1
    else:
        chosen_card = cards[right]
        right -= 1

    if turn_sereja:
        sereja_score += chosen_card
    else:
        dima_score += chosen_card

    turn_sereja = not turn_sereja  # Alternate turns

# Output the final scores
print(sereja_score, dima_score)
