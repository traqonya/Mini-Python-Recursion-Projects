n = int(input())
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def sum_of_integers(number):
    if number == 0:
        return [[]]
    result = []
    for i in range(1, number + 1):
        remaining_sum = sum_of_integers(number - i)
        for way in remaining_sum:
            result.append([i] + way)

    return result
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
sums = sum_of_integers(n)
sums = [" + ".join(list(map(str, a_sum))) for a_sum in sums]
sums.sort()
for a_sum in sums:
    print(a_sum)