words = input().split()
k = int(input())
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def permutations_of_size(my_list, k):
    if k == 0:
        return ['']
    result = []
    for i in range(len(my_list)):
        current_char = my_list[i]
        remaining_chars = my_list[:i] + my_list[i+1:]
        sub_permutations = permutations_of_size(remaining_chars, k-1)
        for perm in sub_permutations:
            result.append(current_char + perm)

    return result
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
perms = permutations_of_size(words, k)
perms.sort()
for perm in perms:
    print(perm)