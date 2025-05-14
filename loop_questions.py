# 1. Print numbers from 1 to 100 using a for loop.

"""
for number in range(1, 101):
    print(number)
"""

# 2. Print even numbers from 1 to 50.

"""
for number in range(1, 51):
    if number % 2 == 0:
        print(f"{number} is even")
"""

# 3. Print the sum of first 10 natural numbers.

"""
sum = 0
for number in range(1, 11):
    sum += number

print(sum)
"""

# 4. Print multiplication table of a given number.

"""
number = int(input("Enter a number... "))

for i in range(1, 11):
    print(f"{number} X {i} = {number*i}")
"""

# 5. Reverse a number using while loop.

"""
number = int(input("Enter a number... "))
rev = 0
while(number != 0):
    rem = number % 10
    rev = rev*10 + rem
    number //= 10
print(rev)
"""

# 6. Check if a number is prime.

"""
number = int(input("Enter a number... "))
is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False

if is_prime:
    print(f"{number} is prime")
else:
    print(f"{number} is non-prime")
"""

# 7. Print all prime numbers between 1 and 100.

"""
print("Prime numbers are : ", end=" ")

for number in range(2, 101):
    is_prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} ", end=" ")
"""

# 8. Print Fibonacci series up to n terms.

"""
number = int(input("Enter a nth term... "))

first = 0
second = 1
print("Fibonacci sequences are : ", end=" ")
for i in range(1, number+1):
    third = first + second
    print(first, end=" ")
    first = second
    second = third
"""

# 9. Find the factorial of a number.

"""
number = int(input("Enter a nth term... "))

factorial = 1
for number in  range(number, 0, -1):
    factorial *= number
print(f"Factorial of {number} is : {factorial}")
"""

# 10. Count the number of digits in a number.

"""
number = int(input("Enter a number... "))
count = 0

while number != 0:
    rem = number % 10
    count += 1
    number //= 10

print(f"Count of digits in number are : {count}")
"""

# 11. Calculate the sum of digits of a number.

"""
number = int(input("Enter a number... "))
sum = 0

while number != 0:
    rem = number % 10
    sum += rem
    number //= 10

print(f"Sum of digits are : {sum}")
"""

# 12. Check if a number is a palindrome.

'''
number = int(input("Enter a number... "))
copy_num = number
rev = 0

while copy_num != 0:
    rem = copy_num % 10
    rev = rev * 10 + rem
    copy_num //= 10

if number == rev:
    print(f"{number} is palindrome...") 
else:
    print(f"{number} is not palindrome...")
'''

# 13. Find the largest number in a list.

'''
numbers = [12, 780, 900, 670,555]
greatest = numbers[0]

for number in numbers:
    if number > greatest:
        greatest = number

print(f"Greatest number is : {greatest}")
'''

# 14. Find the second largest number in a list.

"""
numbers = [12, 780, 900, 670,555]
greatest = max(numbers)
numbers.remove(greatest)
second_greatest = max(numbers)

print(f"Second greatest number is : {second_greatest}")
"""

# 15. Count the number of vowels in a string.

"""
words = input("Enter a word... ").lower()
vowel_count = 0
for character in words:
    if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
        vowel_count += 1

print(f"Count of vowel is : {vowel_count}")
"""

# 16. Find the frequency of each character in a string.

"""
words = input("Enter a word... ").lower()
unique_chars = set(words)
for char in unique_chars:
    count = words.count(char)
    print(f"{char}: {count}") 
"""

# 17. Print a triangle star pattern. 

"""
n = int(input("Enter a number... "))

for i in range(1, n+1):
    print("*"*i)
"""

# 18. Print an inverted triangle pattern.

"""
n = int(input("Enter a number... "))

for i in range(n, 0, -1):
    print("*"*i)
"""

# 19. Print a pyramid number pattern.

"""
n = int(input("Enter a number... "))

for i in range(1, n+1):
    print((n-i)*" ", end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print("")
"""
# 20. Print a diamond star pattern.

"""
n = int(input("Enter a number... "))

for i in range(1, n+1):
    print((n-i)*" ", end="")
    print("*"*((i*2)-1), end="")
    print("")

for j in range(n-1, 0, -1):
    print((n-j)*" ", end="")
    print(((j*2)-1)*"*", end="")
    print("")
"""

# 21. Find duplicates in a list.

"""
lists = [ 1, 3, 9, 8, 7, 1, 9, 7]
unique_number = set(lists)

for number in unique_number:
    if lists.count(number) > 1:
        print(f"{number} is duplicate...")
"""

# 22. Find the GCD of two numbers using loop. greatest common divisor 

"""
num1 = int(input("Enter 1st number... "))
num2 = int(input("Enter 2nd number... "))
divisors = []

if num1 > num2:
    greater = num1
else:
    greater = num2
for i in range(1, greater+1):
    if(num1 % i == 0 and num2 % i == 0):
        divisors.append(i)

print(f"Common divisors are : {divisors}")
print(f"Greatest Common Divisor is : {max(divisors)}")
"""

# 23. Find the LCM of two numbers using loop. least common multiple

"""
num1 = int(input("Enter 1st number... "))
num2 = int(input("Enter 2nd number... "))

if num1 > num2:
    greater = num1
else:
    greater = num2

while True:
    if greater % num1 == 0 and greater % num2 == 0:
        lcm = greater
        break
    greater += 1

print(f"LCM of two number is : {lcm}")
"""

# 24- a. check a number is  Armstrong numbers or not.

"""
An Armstrong number (also called a narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
9⁴ + 4⁴ + 7⁴ + 4⁴ = 6561 + 256 + 2401 + 256 = 9474
"""

"""
num = int(input("Enter a number... "))
copy_num = num
check_num = num

digit = 0
armstrong_sum = 0

while num != 0:
    rem = num % 10
    digit += 1
    num //= 10

while copy_num != 0:
    rem = copy_num % 10
    armstrong_sum += rem**digit
    copy_num //= 10

if armstrong_sum == check_num:
    print(f"{check_num} is Armstrong number...")
else:
    print(f"{check_num} is not Armstrong number...")
"""

# 24- b. Print all Armstrong numbers between 1 and 500.

"""
for num in range(1, 501):
    copy_num = num
    temp = num
    
    digit = 0
    armstrong_sum = 0

    while temp != 0:
        rem = temp % 10
        digit += 1
        temp //= 10

    while copy_num != 0:
        rem = copy_num % 10
        armstrong_sum += rem**digit
        copy_num //= 10

    if armstrong_sum == num:
        print(f"\033[92m{num} is Armstrong number...\033[0m")
    else:
        print(f"{num} is not Armstrong number...")
"""

# 25. Count how many times a digit appears in a number.

"""
number = int(input("Enter a number... "))
count_digit = int(input("Enter the digit... "))
original_number = number
count = 0

while number != 0:
    rem = number % 10
    digit = rem
    if(digit == count_digit):
        count += 1
    number //= 10

print(f"{count_digit} appears {count} time(s) in {original_number}")
"""

# 26. Check if a string is a palindrome using loop.

"""
word = input("Enter a word... ").lower()
# reverse_word = word[::-1]
reverse_word = ""
for char in word:
    reverse_word = char + reverse_word

if word == reverse_word:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is a not palindrome")
"""

# 27. Generate all the factors of a number.

"""
number = int(input("Enter a number... "))

print(f"Factors of {number} are : ", end=" ")
for factor in range(1, number+1):
    if number % factor == 0:
        print(factor, end=" ")
"""
# 28. Check if a number is perfect (sum of divisors equals the number).

"""
number = int(input("Enter a number... "))
sum_of_divisor = 0

for divisor in range(1, number):
    if number % divisor == 0:
        sum_of_divisor += divisor


if number == sum_of_divisor:
    print(f"{number} is a perfect number... ")
else:
    print(f"{number} is not a perfect number... ")
"""



