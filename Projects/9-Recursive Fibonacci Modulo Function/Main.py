n = int(input())
k = int(input())
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def fib_mod(num, mod):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return (fib_mod(num-1, mod)+ fib_mod(num-2, mod)) % mod



# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
print(fib_mod(n, k))