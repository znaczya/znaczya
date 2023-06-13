# taking all inputs
first = input("please enter first number :")
operator = input("please enter respective operator (+,-,*,/,%):")
second = input("please enter second number :")

# declaring as integers
first = int(first)
second = int(second)

# if else conditions applied
if operator == "+" :
    print(first + second)
elif operator == "-" :
    print(first - second)
elif operator == "*" :
    print(first * second)
elif operator == "/" :
    print(first / second)
elif operator == "%" :
    print(first % second)
else:
    print("invalid operation entered")

# code calculator complete