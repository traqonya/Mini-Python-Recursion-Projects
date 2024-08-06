n1 = int(input())
n2 = int(input())
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def digit_match(n1, n2):
    if n1 == 0 or n2==0:
        return 0
    last_n1 = n1 % 10
    last_n2 = n2 % 10
    if last_n1 == last_n2:
        return 1+digit_match(n1//10, n2//10)
    else:
        return digit_match(n1 // 10, n2 // 10)



# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
print(digit_match(n1, n2))