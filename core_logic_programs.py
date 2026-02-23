>>>>#PRIME NUMBER CHECK<<<<<<<<<
#USING FOR LOOP

n = int(input("enter n value: "))
if n <= 1:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
n = int(input("enter a number: "))

#USING WHILE LOOP

if n <= 1:
    print("Not Prime")
else:
    i = 2
    while i < n:
        if n % i == 0:
            print("Not Prime")
            break
        i += 1
    else:
        print("Prime")

#USIng Sqrt approach

n = int(input("Enter number: "))
if n <= 1:
    print("Not Prime")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

>>>>>#FACTORAL OF A NUMBER<<<<<<<<<<

n = int(input("Enter n val: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)

>>>>>#Reverse String<<<<<<<<<
#Method 1 – Using Loop

s = input()
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

#Method 2 – Using While

s = input()
rev = ""
i = len(s) - 1
while i >= 0:
    rev += s[i]
    i -= 1
print(rev)

>>>>>#Palindrome (String)<<<<<<
s = input("Enter string: ")
rev = ""
for ch in s:
    rev = ch + rev
if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

>>>>>#Palindrome (Number)<<<<<<<

n = int(input("Enter number: "))
original = n
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10
if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

>>>>>>>>Armstrong Number<<<<<<
n = int(input("Enter number: "))
original = n
power = len(str(n))
total = 0
while n > 0:
    digit = n % 10
    total += digit ** power
    n //= 10
if original == total:
    print("Armstrong")
else:
    print("Not Armstrong")

>>>>>>Harshad Number<<<<<<<

n = int(input("Enter number: "))
original = n
digit_sum = 0
while n > 0:
    digit_sum += n % 10
    n //= 10
if original % digit_sum == 0:
    print("Harshad Number")
else:
    print("Not Harshad Number")

>>>>>Factorial (Using Loop)<<<<<<<

n = int(input("Enter number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)

>>>>>Fibonacci Series<<<<<<<

n = int(input("Enter number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b


