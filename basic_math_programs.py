# ---------------- AREA PROGRAMS ----------------

# Area of Square
side = 5
area_square = side * side
print("Area of square is:", area_square)
# Sample Output:
# Area of square is: 25


# Area of Rectangle
length = 6
breadth = 4
area_rectangle = length * breadth
print("Area of rectangle is:", area_rectangle)
# Sample Output:
# Area of rectangle is: 24


# Area of Triangle
base = 8
height = 5
area_triangle = 0.5 * base * height
print("Area of triangle is:", area_triangle)
# Sample Output:
# Area of triangle is: 20.0



# ---------------- PERIMETER PROGRAMS ----------------

# Perimeter of Square
side = 6
perimeter_square = 4 * side
print("Perimeter of square is:", perimeter_square)
# Sample Output:
# Perimeter of square is: 24


# Perimeter of Rectangle
length = 5
breadth = 3
perimeter_rectangle = 2 * (length + breadth)
print("Perimeter of rectangle is:", perimeter_rectangle)
# Sample Output:
# Perimeter of rectangle is: 16


# Perimeter of Triangle
side1 = 5
side2 = 6
side3 = 7
perimeter_triangle = side1 + side2 + side3
print("Perimeter of triangle is:", perimeter_triangle)
# Sample Output:
# Perimeter of triangle is: 18



# ---------------- LOGIC PROGRAMS ----------------

# Break Amount into 1000s, 500s, Remaining
amount = 3700
thousands = amount // 1000
remaining = amount % 1000
fivehundreds = remaining // 500
remaining = remaining % 500

print("1000s:", thousands)
print("500s:", fivehundreds)
print("Remaining:", remaining)
# Sample Output:
# 1000s: 3
# 500s: 1
# Remaining: 200


# Convert Seconds into Hours, Minutes, Seconds
total_seconds = 3672
hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
# Sample Output:
# Hours: 1
# Minutes: 1
# Seconds: 12


# Sum of Marks
maths = 85
physics = 90
chemistry = 88
total = maths + physics + chemistry
print("Total marks:", total)
# Sample Output:
# Total marks: 263


# Average of Marks
average = (maths + physics + chemistry) / 3
print("Average marks:", round(average, 2))
# Sample Output:
# Average marks: 87.67
