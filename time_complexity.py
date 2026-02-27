Time Complexity Notes
What is Time Complexity?
Time complexity measures how an algorithm grows with input size (n).
It does NOT measure actual execution time.
It helps compare efficiency between algorithms.

Big-O Notation
Big-O represents worst-case growth rate.
We ignore:
Constants
Lower order terms
  
1️⃣ O(1) — Constant Time
🔹 What is it?
Execution does NOT depend on input size.
No matter how big n is → same number of steps.
🔹 When it happens?
Accessing array element by index
Simple assignment
Single if condition
🔹 Example
arr = [10, 20, 30, 40]
print(arr[2])
Even if array has 1 element or 1 million → still one access.
✔ Best possible complexity.

2️⃣ O(log n) — Logarithmic Time
🔹 What is it?
Input size reduces by half each step.
🔹 When it happens?
Binary Search
Divide and conquer algorithms
🔹 Example Idea
If you search in sorted array:
Each step:
Remove half of the elements
If n = 16
Steps: 16 → 8 → 4 → 2 → 1
Only 4 steps!
Very efficient.

3️⃣  Linear Time — O(n)
Example:
for i in range(n):
    print(i)
When it happens?
Single loop
Traversing array
Breakdown:
n condition checks
n increments
n executions
constant checks:fail states 1-to break loop another 1-to check false condition
Total operations ≈ 3n + 2
Big-O → O(n)

4️⃣ O(n log n)
🔹 What is it?
Combination of linear growth and logarithmic reduction.
🔹 When it happens?
Efficient sorting algorithms
Merge Sort
Quick Sort (average case)

🔹 Example Idea
If for every element (n),
you do a log n operation,
Total becomes:
n × log n
Better than O(n²).
  
5️⃣ O(n²) — Quadratic Time
🔹 What is it?
Work grows as square of input.
If input doubles → work becomes 4 times.
🔹 When it happens?
Nested loops
Comparing every element with every other element
🔹 Example
for i in range(n):
    for j in range(n):
        print(i, j)
If n = 5 → 25 steps
If n = 100 → 10,000 steps
That’s why it becomes slow quickly.

>>>>>>Why TC It Matters<<<<<<<
Lower time complexity → better performance for large inputs.

