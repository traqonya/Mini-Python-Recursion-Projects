import json
ls = json.loads(input())
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def reverse_list(my_list):
    new_list =list()
    if not my_list:
        return new_list
    return reverse_list(my_list[1:]) + [my_list[0]]
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
print(reverse_list(ls))