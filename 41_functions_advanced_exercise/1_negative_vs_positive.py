def numbs(*args):
    negative = sum(filter(lambda n : n < 0, *args))
    positive = sum(filter(lambda n : n > 0, *args))

    return negative, positive


numbers = list(map(int, input().split()))
negative_sum, positive_sum = numbs(numbers)

print(negative_sum)
print(positive_sum)

if abs(negative_sum) < positive_sum:
    print('The positives are stronger than the negatives')
else:
    print('The negatives are stronger than the positives')