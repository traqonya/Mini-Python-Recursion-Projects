words = input().split()
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def permutations(my_list):
    if len(my_list) == 0:
        return []
    elif len(my_list) == 1:
        return my_list
    else:
        result = []
        for i in range(len(my_list)):
            x = my_list[i]
            rest_list = list(my_list[:i] + my_list[i + 1:])
            for perm in permutations(rest_list):
                result.append(x + str(perm))
    return result


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
perms = permutations(words)
perms.sort()
for perm in perms:
    print(perm)