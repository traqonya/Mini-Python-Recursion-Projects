# mini-python-projects
A collection of simple python mini projects

1-Recursive Digit Match Function

Implement a recursive function `digit_match(number1, number2)` to count matching digits from right to left in two positive integers.

### Task
- **Function**: `digit_match(number1, number2)`
- **Input**: Two positive integers `number1` (n1) and `number2` (n2)
- **Output**: Count of matching digits

### Details
- Compare last digits of both numbers
- Recursively process remaining digits
- Base case: when one or both numbers are zero

### Example
For `12345` and `54321`, the matching digits count is `2`.

### Usage
Useful for digit-wise comparison tasks.

-----------------------------------------------------------

2-Recursive Reverse Check Function

Implement a recursive function `is_reverse(string1, string2)` to check if `string1` is the reverse of `string2`, ignoring case differences.

### Task
- **Function**: `is_reverse(string1, string2)`
- **Input**: Two non-empty strings `string1` (s1) and `string2` (s2)
- **Output**: `True` if `string1` is the reverse of `string2`, `False` otherwise

### Details
- **Case-Insensitive**: Convert both strings to the same case for comparison
- **Recursive Logic**:
  - Base Case: If both strings are empty, return `True`
  - If the first character of `string1` matches the last character of `string2`, recursively check the remaining characters
  - Otherwise, return `False`

### Example
For `string1 = "hELLo 123"` and `string2 = "321 olleH"`, the function returns `True`.

### Usage
Useful for tasks requiring case-insensitive reverse string comparison.

-----------------------------------------------------------


3-Recursive Permutations Function

Implement a recursive function `permutations(my_list)` that returns all concatenated permutations of a list of strings.

### Task
- **Function**: `permutations(my_list)`
- **Input**: A non-empty list of non-empty strings `my_list`
- **Output**: A list of all concatenated permutations of the strings

### Details
- **Recursive Logic**:
  - Base Case: If `my_list` is empty, return a list with an empty string
  - For each string in `my_list`, recursively find permutations of the remaining list and concatenate the string to each permutation

### Example
For `my_list = ["1", "2", "3"]`, the function returns `["123", "132", "213", "231", "312", "321"]`.

### Usage
Useful for generating all possible concatenated permutations of a list of strings.

-----------------------------------------------------------


4-Recursive Size-K Permutations Function

Implement a recursive function `permutations_of_size(my_list, k)` that returns all concatenated permutations of size `k` from a list of strings.

### Task
- **Function**: `permutations_of_size(my_list, k)`
- **Input**: 
  - A non-empty list of non-empty strings `my_list`
  - A positive integer `k` (where `k` is less than or equal to the length of `my_list`)
- **Output**: A list of all concatenated permutations of the strings of size `k`

### Details
- **Recursive Logic**:
  - Base Case: If `k` is 0, return a list with an empty string
  - For each string in `my_list`, recursively find permutations of size `k-1` from the remaining list and concatenate the string to each permutation

### Example
For `my_list = ["1", "2", "3"]` and `k = 2`, the function returns `["12", "13", "21", "23", "31", "32"]`.

-----------------------------------------------------------


5-Recursive Sum of Integers Function

Implement a recursive function `sum_of_integers(number)` that finds all the ways a given number can be written as a sum of positive integers.

### Task
- **Function**: `sum_of_integers(number)`
- **Input**: A positive integer `number`
- **Output**: A list of lists, where each sublist is a permutation of integers that sum to `number`

### Details
- **Recursive Logic**:
  - Base Case: If `number` is 0, return a list with an empty list.
  - Iterate through all possible integers from 1 to `number`.
  - For each integer, recursively find the sum combinations for the remaining value (`number - i`).
  - Append the current integer to each of these combinations and add them to the result list.

### Example
For `number = 3`, the function returns `[[1, 1, 1], [1, 2], [2, 1], [3]]`.

### Usage
Useful for generating all possible ways to represent a number as a sum of positive integers.

-----------------------------------------------------------


6-Recursive Check for Any Empty List Function

Implement a recursive function `any_empty(my_list)` that checks if any list within a potentially nested list is empty.

### Task
- **Function**: `any_empty(my_list)`
- **Input**: A list `my_list`, which may contain nested lists
- **Output**: `True` if any list (including nested ones) is empty; otherwise, `False`

### Details
- **Recursive Logic**:
  - Base Case: If `my_list` is an empty list, return `True`.
  - Iterate through each element in `my_list`:
    - If an element is also a list, recursively call `any_empty` on that element.
    - If any recursive call returns `True`, return `True`.
  - If no empty lists are found, return `False`.

### Example
For `my_list = [1, 2, [3, 4], [[5, 7, 8], []]]`, the function returns `True`.

### Usage
Useful for determining if any level of a nested list contains an empty list.

-----------------------------------------------------------


7-Recursive Reverse List Function

Implement a recursive function `reverse_list(my_list)` that returns a reversed version of the input list.

### Task
- **Function**: `reverse_list(my_list)`
- **Input**: A list `my_list`
- **Output**: A new list that is the reverse of `my_list`

### Details
- **Recursive Logic**:
  - Base Case: If `my_list` is empty, return an empty list.
  - Recursive Case: Take the first element of `my_list`, reverse the rest of the list recursively, and append the first element to the end of the reversed list.

### Example
For `my_list = [1, 2, 3]`, the function returns `[3, 2, 1]`.

### Usage
This function is useful for reversing lists in various applications.

-----------------------------------------------------------


8-Recursive GCD Function

Implement a recursive function `gcd(number1, number2)` that returns the greatest common divisor (GCD) of two positive integers using Euclid's Algorithm.

### Task
- **Function**: `gcd(number1, number2)`
- **Input**: 
  - `number1`: A positive integer
  - `number2`: A positive integer
- **Output**: The greatest common divisor of `number1` and `number2`

### Details
- **Recursive Logic** (Euclid's Algorithm):
  - Base Case: If `number2` is 0, return `number1` (since the GCD of any number and 0 is the number itself).
  - Recursive Case: Call `gcd` with `number2` and `number1 % number2`.

### Example
For `number1 = 48` and `number2 = 18`, the function returns `6`.

### Usage
This function is useful for calculating the GCD in mathematical computations.

-----------------------------------------------------------


9-Recursive Fibonacci Modulo Function

Implement a recursive function `fib_mod(num, mod)` that returns the remainder of the `num`th Fibonacci number when divided by `mod`.

### Task
- **Function**: `fib_mod(num, mod)`
- **Input**:
  - `num`: A non-negative integer representing the index of the desired Fibonacci number.
  - `mod`: A positive integer to take the remainder from.
- **Output**: The remainder of the `num`th Fibonacci number divided by `mod`.

### Details
- **Fibonacci Sequence**:
  - 0th Fibonacci number is `0`
  - 1st Fibonacci number is `1`
  - For `n >= 2`: `F(n) = F(n-1) + F(n-2)`

- **Recursive Logic**:
  - Base Case: If `num` is `0`, return `0`. If `num` is `1`, return `1`.
  - Recursive Case: Return `(fib_mod(num - 1, mod) + fib_mod(num - 2, mod)) % mod` to get the Fibonacci number and apply the modulo operation.

### Example
For `num = 5` and `mod = 3`, the function returns `2`, since the 5th Fibonacci number is `5` and `5 % 3 = 2`.

### Usage
This function can be useful for calculating Fibonacci numbers under a modulo in various applications.

-----------------------------------------------------------


10-Recursive Calculator Parser Function

Implement a recursive function `calc_parser(calc_str)` that evaluates a mathematical expression represented as a string.

### Task
- **Function**: `calc_parser(calc_str)`
- **Input**: A non-empty string `calc_str` that follows the specified format.
- **Output**: The result of the evaluated expression as an integer.

### Details
- **Expression Format**:
  - Contains either `+` or `-` operations.
  - Each operator has a single whitespace on both sides.
  - Operands can be positive integers or nested expressions enclosed in parentheses.
  - The outermost expression is not enclosed in parentheses.

### Recursive Logic
1. **Base Case**: If the expression is a single positive integer, convert and return it as an integer.
2. **Handle Nested Expressions**: 
   - Iterate through the string to identify operators (`+` or `-`).
   - For each operator, split the string into left and right parts. If a part contains parentheses, recursively evaluate that part.
3. **Calculate Result**: Combine the results of the left and right parts using the identified operator.

### Example
For `calc_str = "1 + (2 - 3)"`, the function returns `0` because `1 + (2 - 3) = 1 + (-1) = 0`.

### Usage
This function can be used to evaluate mathematical expressions represented as strings.
