#%%task 1
name = input("Your name: ")
age = input("Your age: ")
print(f"Hello, {name}! You are {age} years old.")
#%%task 2
a=int(input())
b=int(input())
print(f"sum:{a+b}")
print(f"difference:{a-b}")
print(f"multiplication:{a*b}")
#%%task 3
a = int(input("temperature in Celsius: "))
print(f"temp in Fahrenheit : {a * 9/5 + 32}")

#%%task 4
a = 5
b = 10
a, b = b, a
print(f"a = {a}, b = {b}")

#%%task 5
a = int(input("enter number: "))
if a % 2==0:
    print("even")
else:
    print("odd")

#%%task 6
age = int(input("Enter your age: "))
if age <= 12:
    print("Child")
elif age <= 17:
    print("Teenager")
else:
    print("Adult")

#%%task 7
a=int(input("enter number: "))
b=int(input("enter number: "))
c=int(input("enter number: "))
if a>b and a>c:
    print(f"Largest:{a}")
elif b>a and b>c:
    print(f"Largest:{b}")
elif c>a and c>b:
    print(f"Largest:{c}")

#%%task 8
a=int(input("enter number: "))
b=int(input("enter number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == "+":
    result = a + b
    print(f"Result: {a} + {b} = {result}")

elif operation == "-":
    result = b- a
    print(f"Result: {a} - {b} = {result}")

elif operation == "*":
    result = a * b
    print(f"Result: {a} * {b} = {result}")
elif operation == "/":
    if b != 0:
        result = a / b
        print(f"Result: {a} / {b} = {result}")
    else:
        print("Error")
else:
    print("Error")

#%%task 9
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#%%task 10
score = int(input("Enter your score (0-100): "))
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
elif score >= 0:
    print("Grade: F")

#%%task 11
balance = 1000
withdrawal = int(input("Enter withdrawal amount: "))
if withdrawal <= balance:
    balance -= withdrawal
    print(f" You withdrew {withdrawal}.")
    print(f"Current balance: {balance}")
else:
    print("Error: Insufficient funds.")
    print(f"Your balance is only {balance}.")

#%%task 12
correct_login = "admin"
correct_password = "1234"
user_login = input("Enter login: ")
user_password = input("Enter password: ")
if user_login == correct_login and user_password == correct_password:
    print("Welcome!")
else:
    print("Error: Invalid login or password.")

#%%task 13
amount = int(input("Enter your amount: "))
if amount >= 10000:
    discount = 0.10
    print("Your discount: 10%")
elif amount >= 5000:
    discount = 0.05
    print("Your discount: 5%")
total = amount * (1 - discount)
print(f"Сумма к оплате: {total}")

#%%task 14
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("The triangle exists.")
    if a == b == c:
        print("Type: Equilateral")
    elif a == b or b == c or a == c:
        print("Type: Isosceles")
    else:
        print("Type: Scalene")

#%%task 15
color = input("Enter traffic light color (red, yellow, green): ")
if color == "red":
    print("Action: Stop")
elif color == "yellow":
    print("Action: Wait")
elif color == "green":
    print("Action: Go")
else:
    print("Error: Unknown color! Please enter red, yellow, or green.")

#%%task 16
number = int(input("Enter a number: "))
print("--- Analysis Results ---")
if number > 0:
    print("Status: Positive")
elif number < 0:
    print("Status: Negative")
else:
    print("Status: Zero")
if number % 2 == 0:
    print("Parity: Even")
else:
    print("Parity: Odd")
if 1 <= number <= 100:
    print("Range: Within 1-100")
else:
    print("Range: Outside 1-100")

#%%task 17
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /, **, %): ")
if operation == "+":
    print(f"Result: {num1 + num2}")
elif operation == "-":
    print(f"Result: {num1 - num2}")
elif operation == "*":
    print(f"Result: {num1 * num2}")
elif operation == "/":
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed!")
elif operation == "**":
    print(f"Result: {num1 ** num2}")
elif operation == "%":
    if num2 != 0:
        print(f"Result: {num1 % num2}")
    else:
        print("Error: Cannot find modulo by zero!")
else:
    print(f"Error: '{operation}' is an invalid operation!")

#%%task 18
password = input("Enter password: ")
has_digit = False
has_upper = False
for char in password:
    if char.isdigit():
        has_digit = True
    if char.isupper():
        has_upper = True
all = 0
if len(password) >= 8:
    all += 1
if has_digit:
    all += 1
if has_upper:
    all += 1
if all == 3:
    print("Strength: Strong")
elif all == 2:
    print("Strength: Medium")
else:
    print("Strength: Weak")

#%%task 19
balance = 5000
print("--- Welcome to the Bank ---")
print("1. Check balance")
print("2. Deposit")
print("3. Withdraw")
choice = input("Select an option (1-3): ")
if choice == "1":
    print(f"Current balance: {balance}")
elif choice == "2":
    amount = int(input("Enter deposit amount: "))
    if amount > 0:
        balance += amount
        print(f"Successfully deposited {amount}. New balance: {balance}")
    else:
        print("Error: Deposit must be positive!")
elif choice == "3":
    amount = int(input("Enter withdrawal amount: "))
    if amount <= 0:
        print("Error: Amount must be positive!")
    elif amount <= balance:
        balance -= amount  # Вычитаем из баланса
        print(f"Successfully withdrew {amount}. New balance: {balance}")
    else:
        print("Error: Insufficient funds!")

#%%task 20
print("Quess the number")
a=18
b=int(input())
if(b==a):
    print("Correct")
elif(b<a):
    print("Too low")
elif(b>a):
    print("Too high")

#%%task 21
a=int(input("exam score:"))
b=int(input("Attendance:"))
if a < 50 or b < 60:
    print("Fail")
else:
    if a >= 85:
        print("Your grade is A");
    elif a >= 65:
        print("Your grade is B");
    elif a >= 50:
        print("Your grade is C");

#%%task 22
a = int(input("Order amount:"))
b = int(input("Distance:"))
base_delivery = 1000
if a > 15000:
    print("Free delivery");
if b <= 5:
    print("1000 for delivery");
if b > 5:
    print(f"Price for delivery: {b * 200}")

#%%task 23
salary = int(input("Enter your salary: "))
b = str(input("Credit history: "))
if salary > 200000 and b == "good":
    print("Your credit is Approved")
else:
    print("Your credit is Rejected")

#%%task 24
login = str(input("Enter your login: "))
password = str(input("Enter your password: "))
a = "QWERTY"
b = "12345"
if a == login and b == password:
    print("Access granted!")
else:
    if a != login or b != password:
        print("Wrong!!,You have 1 more attempt!")
        login = str(input("Enter your login: "))
        password = str(input("Enter your password: "))
        if a == login and b == password:
            print("Access granted!")
        else:
            print("Wrong!!,You Blocked for 30 minutes!")
    else:
        print("Access granted!")

#%%task 25
print("----Menu----")
print("1. Add")
print("2. Subtract")
print("3. Multiple")
print("4. Exite")

choice = input("Select an option (1-4): ")
if choice == "1" or choice == "2" or choice == "3" :
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if choice == "1":
        print(a + b)
    elif choice == "2":
        print(a - b)
    elif choice == "3":
        print(a * b)
elif choice == "4":
    print("Exiting program. Goodbye!")
