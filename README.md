# tandemloop_test
This repository contains solutions for *4 coding problems* written in Python.  
Each problem demonstrates basic programming concepts such as classes, loops, lists, and dictionaries.


##problem-1: Calculator using Class

Task: Build a calculator class that can do addition, subtraction, multiplication, and division.

Inputs:

a first number

b second number

operation type of operation ("add", "sub", "mul", "div")

Logic:

If operation = "add" return a + b

If operation = "sub" return a b

If operation = "mul" return a b

If operation = "div" check if b!= 0, then a/ b, otherwise return error.

##Example
a = 10, b = 5
operation = "add" ← 15
operation = "sub" 5
operation = "mul" 50
operation = "div" 2.0




##  Problem 2: Print first a odd numbers
Task: Print the first a odd numbers.

Logic:

The formula for the i-th odd number = 2i + 1 (starting from i = 0 ).
So just loop a times and collect numbers.

Example:
a = 1 -> [1]
a = 2 -> [1, 3]
a = 3 -> [1, 3, 5]
a = 4 [1, 3, 5, 7]

so whatever input you give,you always get that many odd numbers
here output length = input number
if input is 10 then , output will be first 10 odd numbers
 




##  Problem 3: Odd number series
Task: Print odd numbers but treat even inputs differently.

Logic:
If input is odd numbers. generate first a odd
If input is even generate same as a-1.

Example:
a = 1 [1]
a = 2 (even → use 1) → [1]
a = 3  [1, 3, 5]
a = 4 (even us) [1, 3, 5]




## Problem 4: Count multiples in a list
task: Given a list of numbers, count how many are divisible by each number in [1,2,3,4,5,6,7,8,9]

Logic:
For each divisor in [1...9], check every number in the list.
If num % divisor == 0, increase count.
Store counts in a dictionary.

### Example
nput = [1,2,8,9,12,46,76,82,15,20,30]

Check each divisor:
divisible by 1 - all 11 numbers
divisible by 2 - 8 numbers
divisible by 3 - 4 numbers
divisible by 4 - 4 numbers
divisible by 5 - 3 numbers
divisible by 6 - 2 numbers
divisible by 7 - 0 number
divisible by 8 - 1 number
divisible by 9 - 1 number

Output:
{1:11, 2:8, 3:4, 4:4, 5:3, 6:2, 7:0, 8:1, 9:1}







