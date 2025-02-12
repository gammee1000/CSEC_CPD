n = int(input())  # Number of wires
birds = list(map(int, input().split()))  # Number of birds on each wire

m = int(input())  # Number of shots

for _ in range(m):
    x, y = map(int, input().split())  # Shot at x-th wire, y-th bird
    x -= 1  # Convert to 0-based index

    if x > 0:
        birds[x - 1] += y - 1  # Birds on the left jump up
    if x < n - 1:
        birds[x + 1] += birds[x] - y  # Birds on the right jump down

    birds[x] = 0  # The shot wire loses all birds at that position

for bird in birds:
    print(bird)
