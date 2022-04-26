Fahrenheit to Celsius
Send Feedback
Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.


code answe-
def printTable(s, e, w):
    # Implement Your Code Here
    while True:
        c = 0
        if s <= e:
            c = (s - 32) * 5 / 9
            print(s, int(c))
            s = s + w

        else:
            break

s = int(input())
e = int(input())
step = int(input())
printTable(s, e, step)



calculator_:
  
  Write a program that performs the tasks of a simple calculator. The program should first take an integer as input and then based on that integer perform the task as given below.
  
  
  while True:
    choice = int(input())
    if (choice>=1 and choice<=5):
        num1 = int(input())
        num2 = int(input())
        if choice == 1: 
            res = num1 + num2
            print(res)
        elif choice == 2: 
            res = num1 - num2
            print(res)
        elif choice == 3: 
            res = num1 * num2
            print(res)
        elif choice == 4: 
            res = num1 // num2
            print(res)
        elif choice == 5:
            res = num1 % num2
            print(res)
    elif choice == 6:
        exit()
    else:
        print("Invalid Operation")
   
  
  
  reverse of a number:-
    
    Write a program to generate the reverse of a given number N. Print the corresponding reverse number.
Note : If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.
  
  
  n =int(input())
rev=0
while n>0:
    a = n%10
    rev =rev*10+a
    n=n//10
    
print(rev)

Palindrome number:_
  
  Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121


n=int(input())
temp=n
rev=0

while n>0:
    a =n%10
    rev=rev*10+a
    n=n//10
if temp==rev:
    print("true")
else:
	print("false")
  
  
Sum of even & odd:-
  
  Write a program to input an integer N and print the sum of all its even digits and sum of all its odd digits separately.
Digits mean numbers, not the places! That is, if the given integer is "13245", even digits are 2 & 4 and odd digits are 1, 3 & 5.
Input format :
  
  
n=input()
even=0
total=0
for c in n:
    c=int(c)
    total+=c
    if c%2==0:
        even+=c
    else:
        odds=total-even
print('{} {}'.format(even,odds))  


Nth Fibonacci Number:_
  Nth term of Fibonacci series F(n), where F(n) is a function, is calculated using the following formula -
    F(n) = F(n-1) + F(n-2), 
    Where, F(1) = F(2) = 1
    
 n=int(input())
def fibonacci_num(n):
    u=0
    v=1
if n<=0:
    print('0')
elif n==1:
    print('1')
else:
    for i in range(2,n):
        c=u+v
        u=v
        v=c
    print(v)   
  
  
  
  Sum of even & odd
