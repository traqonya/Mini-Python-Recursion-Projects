s1 = input()
s2 = input()
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def is_reverse(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    if len(s1)==0 or len(s2)==0:
        return True
    elif len(s1) != len(s2):
        return False
    elif s1[0] == s2[-1]:
        return is_reverse(s1[1:],s2[:len(s2)-1])
    elif s1[0] != s2[-1]:
        return False
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
print(is_reverse(s1, s2))