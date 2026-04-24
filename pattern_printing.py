n=int(input("enter n value:"))  #Right angled triangle
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()

n=int(input("enter n value:"))  #Downward Right angled triangle
for i in range(n):
    for j in range(i,n):
        print('*',end=' ')
    print()

n=int(input("enter n value:"))  #left angled triangle
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()

n=int(input("enter n value:"))  #Downward left angled triangle
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n): print('*',end=' ')
    print()
    
n=int(input("enter n value:"))  #Pyramid
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    for j in range(i):
        print('*',end=' ')
    print()
  
n=int(input("enter n value:"))  #Reverse Pyramid
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    for j in range(i,n-1):
        print('*',end=' ')
    print()
  
n=int(input("enter n value:"))   # Diamond
for i in range(n):
    for j in range(i, n):
        print(' ', end=' ')
    for j in range(i + 1):
        print('*', end=' ')
    for j in range(i):
        print('*', end=' ')
    print()
for i in range(n):
    for j in range(i+2):
        print(' ', end=' ')
    for j in range(i,n-1):
        print('*', end=' ')
    for j in range(i,n-2):
        print('*', end=' ')
    print()
  
n=int(input("enter n value:"))  #Sandglass
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    for j in range(i,n-1):
        print('*',end=' ')
    print()
for i in range(1,n):
    for j in range(n-i):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    for j in range(i):
        print('*',end=' ')
    print()

n=int(input("enter n value:"))  #Left Pascal's traingle
for i in range(n):
     for j in range(i+1):
         print('*',end=' ')
     print()
for i in range(n):
    for j in range(i,n-1):
        print('*',end=' ')
    print()
  
n=int(input("enter n value:"))  #Right Pascal's triangle
for i in range(n):
    for j in range(i,n-1):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n-1): 
        print('*',end=' ')
    print()

n=int(input("enter n value:"))  #Double Hill
for i in range(n):
    for j in range(i, n - 1):
        print("  ", end="")
    for j in range(i + 1):
        print("* ", end="")
    for j in range(i):
        print("* ", end="")
    for j in range(i, n - 1):
        print("    ", end="")
    for j in range(i + 1):
        print("* ", end="")
    for j in range(i):
        print("* ", end="")
    print()

n = int(input("Enter n value: "))  # Butterfly
for i in range(n):
 for j in range(i + 1):
        print("* ", end="")
    for j in range(i, n - 1):
        print("    ", end="")
    for j in range(i + 1):
      print("* ", end="")
    print()
for i in range(n - 1):
    for j in range(i, n - 1):
        print("* ", end="")
    for j in range(i + 1):
        print("    ", end="")
    for j in range(i, n - 1):
        print("* ", end="")
    print()


