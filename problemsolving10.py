Check if a Matrix is Square
l=[[1, 2], [3, 4]]
if len(l)!=2:
    print(False)
else:
    for i in l:
        if len(i)!=2:
            print(False)
            break
    else:
        print(True)
