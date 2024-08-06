n1 = int(input())
n2 = int(input())
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def gcd(n1, n2):

    maxi = max(n1, n2)
    mini = min(n1, n2)
    c = maxi % mini
    if c == 0:
        return mini
    else:
        return gcd(mini, c)
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
print(gcd(n1, n2))