scores = []
i = 0

while True:
    score = int(input("Enter the score: "))
    if score < 0:
        break
    scores[i] = score
    i += 1

total = 0

for n in scores:
    total += scores

av = total / i

scores.sort()
print()