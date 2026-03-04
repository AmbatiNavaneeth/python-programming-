🚀 Elements Greater Than a Value:
def ElementsGreaterThanAValue(nums, threshold):
    output=[]
    if len(nums)<=0:
        return 0
    for num in nums:
        if num>threshold:
            output.append(num)
            num+=1
        else:
            num+=1    
    return output

🚀 Sum of Two Largest Digits Among Three:
def SumOfTwoLargestDigitsAmongThree(a, b, c):
    arr = sorted([a, b, c])
    return (arr[1] + arr[2])
    # return a + b + c - min(a, b, c)

🚀 First Non-Repeating Character
def firstNonRepeatingChar(s):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    for i in range(len(s)):
        if freq[s[i]]==1:
            return i
    return -1

🚀 Check if a Number is Armstrong:
def check_armstrong(num):
    if num<0:
        return None
    summ=0
    n=len(str(num))
    for digit in str(num):
        check_armstrong=int(digit)**n
        summ+=check_armstrong
    if summ==num:
        return True
    else:
        return False

🚀 Single-Digit or Multi-Digit Number:
def Single_Digit_Or_Multi_Digit_Number(num):
   if -9<=num<=9:
    return "Single-digit number"
   else:
    return "Multi-digit number"
     
🚀 Majority Element:
def MajorityElement(nums):
    freq={}
    for num in nums:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    for key in freq:
        if freq[key]>len(nums)//2:
            return key

🚀 Student Pass if Passed Any Two Subjects:
def Student_Pass_if_Passed_Any_Two_Subjects(maths, physics, chemistry):
    if maths>=35 and physics>=35:
        return "Pass"
    elif chemistry>=35 and physics>=35:
        return "Pass"
    elif chemistry>=35 and maths>=35:
        return "Pass"
    else:
        return "Fail"

🚀 List Rotation (Right Rotation):
def ListRotation(nums, k):
   if nums==[]:
    return []
   n=len(nums)
   k=k%n
   nums.reverse()
   nums[:k]=reversed(nums[:k])
   nums[k:]=reversed(nums[k:])
   return nums

🚀 Find 2nd Largest Number In The List:
def second_max(nums):
    first=float('-inf')
    second=float('-inf')
    for num in nums:
        if num>first:
            second=first
            first=num
        elif num>second and num!=first:
            second=num
    return second if second!=float('-inf') else 1

🚀 Salary Deduction Calculator:
def Salary_Deduction_Calculator(salary):
    tax=(10*salary)/100
    insurance=(5*salary)/100
    net_salary=salary-(tax+insurance)
    if net_salary>50000:
        return "High Income"
    return "Standard Income"






