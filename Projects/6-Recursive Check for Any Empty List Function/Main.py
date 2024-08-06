import json
ls = json.loads(input())
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def any_empty(my_list):
    if my_list== []:
        return True
    for i in my_list:
        if type(i)==list:
            if any_empty(i):
                return True
        else:
            if i == []:
                return True
    return False

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
print(any_empty(ls))