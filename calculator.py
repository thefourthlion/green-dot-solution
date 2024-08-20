Sure, here is a simple example of a text-based calculator application. Please note that there is no exception handling in this one. This script takes two numbers and an operator then performs the operation.

```python
def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   if y != 0:
       return x / y
   else:
       print("Error! Dividing by zero is not allowed.")

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 

while True:
   choice = input("Enter choice(1/2/3/4): ")

   if choice in ('1', '2', '3', '4'):
       num1 = int(input("Enter first number: "))
       num2 = int(input("Enter second number: "))

       if choice == '1':
           print(num1, "+", num2, "=", add(num1, num2))

       elif choice == '2':
           print(num1, "-", num2, "=", subtract(num1, num2))

       elif choice == '3':
           print(num1, "*", num2, "=", multiply(num1, num2))

       elif choice == '4':
           print(num1, "/", num2, "=", divide(num1, num2))
       
       break
   else:
       print("Invalid Input")
```

Just copy and paste this code into a new Python file (like `calculator.py`), run it from your terminal, and follow the instructions it gives. It will ask you to enter an operation number (1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division) and two numbers, and then it will print the result.

Please remember that this a rudimentary example and a lot of improvements can be made including handling special cases, invalid input and incorporating a GUI.
