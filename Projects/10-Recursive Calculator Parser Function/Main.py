inp_str = input()
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
# Input is given as a string, so no need for predefined variables

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
# Input is given as a string, so no need for predefined variables

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def calc_parser(calc_str):
    calc_str = calc_str.replace(" ", "")
    if calc_str.isdigit() or (calc_str[0] == '-' and calc_str[1:].isdigit()):
        return int(calc_str)
    count = 0
    for i in range(len(calc_str) - 1, -1, -1):
        if calc_str[i] == ')':
            count += 1
        elif calc_str[i] == '(':
            count -= 1
        elif (calc_str[i] in {'+', '-'}) and (count == 0):
            right = calc_parser(calc_str[i + 1:])
            left = calc_parser(calc_str[:i])
            return left + right if calc_str[i] == '+' else left - right
    if calc_str[0] == '(' and calc_str[-1] == ')':
        return calc_parser(calc_str[1:-1])
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
print(calc_parser(inp_str))