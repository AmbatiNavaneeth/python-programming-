# 1. Smart Traffic Signal
# You are given the current signal color ("red", "yellow", "green") and a boolean value indicating whether an emergency vehicle is approaching.
# Decide what action should be taken:
# Stop
# Slow down
# Go
# Or override the signal for emergency vehicles.

signal = input("Enter signal color (red/yellow/green): ").lower()
emergency = input("Is emergency vehicle approaching? (yes/no): ").lower()
if emergency == "yes":
    print("Override signal")
else:
    if signal == "red":
        print("Stop")
    elif signal == "yellow":
        print("Slow down")
    elif signal == "green":
        print("Go")
    else:
        print("Invalid signal input")
        
# Loan Eligibility Checker
# 2. Loan Eligibility Checker
# A bank provides a loan based on the following conditions:
# Age must be between 21 and 60
# Monthly salary ≥ 25,000
# Credit score ≥ 700
# Given age, salary, and credit score, determine whether the person is:
# Fully eligible
# Partially eligible
# Not eligible
age = int(input("Enter age: "))
salary = int(input("Enter monthly salary: "))
credit = int(input("Enter credit score: "))
count = 0
if 21 <= age <= 60:
    count += 1
if salary >= 25000:
    count += 1
if credit >= 700:
    count += 1
if count == 3:
    print("Fully Eligible")
elif count == 2:
    print("Partially Eligible")
else:
    print("Not Eligible")

# 3. Triangle Type Identifier
# Given three integer values representing the sides of a triangle, determine:
# If a triangle is possible
# If possible, identify whether it is Equilateral, Isosceles, or Scalene
# Also handle invalid inputs logically.

#Triangle Type Identifier
a,b,c= map(int,input("sides:").split())
if a <= 0 or b <= 0 or c <= 0:
    print("Invalid input. Sides must be positive.")
elif a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Triangle not possible")
 

# 4. Electricity Bill Slab Logic
# Electricity charges depend on units consumed:
# First 100 units → free
# 101–300 units → ₹5 per unit
# Above 300 units → ₹10 per unit
# Given the number of units consumed, calculate the total bill amount using proper conditional logic.

# Electricity Bill Code
units = int(input("Enter units consumed: "))
if units <= 100:
    bill = 0
elif units <= 300:
    bill = (units - 100) * 5
else:
    bill = (200 * 5) + (units - 300) * 10
print("Total Bill:", bill)
# Sample Input:
# Enter units consumed: 475
# Sample Output:
# Total Bill: 2750

# 5. Exam Result Analyzer
# A student has marks in three subjects.
# Rules:
# If any subject < 35 → Fail
# If average ≥ 75 → Distinction
# If average ≥ 60 → First Class
# If average ≥ 50 → Second Class
# Else → Pass
# Determine the student’s final result.

m1,m2,m3 = map(int,input("Enter marks: ").split(","))
if m1 < 35 or m2 < 35 or m3 < 35:
    print("Fail")
else:
    avg = (m1 + m2 + m3) / 3
    if avg >= 75:
        print("Distinction")
    elif avg >= 60:
        print("First Class")
    elif avg >= 50:
        print("Second Class")
    else:
        print("Pass")
