from collections import deque

strength = list(map(int, input().split()))
accuracy = deque(map(int, input().split()))
points = 100
strength_decrease = 10
hat_trick = 3
scores = 0

while strength and accuracy:
    current_strength = strength.pop()
    current_accuracy = accuracy.popleft()
    value = current_strength + current_accuracy

    if value == points:
        scores += 1

    elif value < points:
        if current_strength == current_accuracy:
            strength.append(value)

        elif current_strength < current_accuracy:
            accuracy.appendleft(current_accuracy)

        elif current_strength > current_accuracy:
            strength.append(current_strength)
    elif value > points:
        strength.append(current_strength - strength_decrease)
        accuracy.append(current_accuracy)

if scores == hat_trick:
    print('Paul scored a hat-trick!')
elif scores == 0:
    print('Paul failed to score a single goal.')
elif scores > 3:
    print('Paul performed remarkably well!')
elif scores < 3:
    print('Paul failed to make a hat-trick.')

if scores:
    print(f'Goals scored: {scores}')


if strength:
    print(f"Strength values left: {', '.join(str(s) for s in strength)}")
elif accuracy:
    print(f"Accuracy values left: {', '.join(str(s) for s in accuracy)}")
