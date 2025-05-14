num1 = int(input("Enter 1st number.... "))
num2 = int(input("Enter 2nd number.... "))
operator =  input("Choose an operator according to your operation(+, -, *, /, %, **, //).... ")

#-----------Using if-elif-else-----------

if( operator == '+'):
    print(f"Result of {num1} {operator} {num2} = {num1 + num2} ")
elif( operator == '-'):
    print(f"Result of {num1} {operator} {num2} = {num1 - num2} ")
elif( operator == '*'):
    print(f"Result of {num1} {operator} {num2} = {num1 * num2} ")
elif( operator == '/'):
    print(f"Result of {num1} {operator} {num2} = {num1 / num2} ")
elif( operator == '%'):
    print(f"Result of {num1} {operator} {num2} = {num1 % num2} ")
elif( operator == '**'):
    print(f"Result of {num1} {operator} {num2} = {num1 ** num2} ")
elif( operator == '//'):
    print(f"Result of {num1} {operator} {num2} = {num1 // num2} ")
else:
    print("Invalid Operator...")


# --------- Using Switch Case----------

match operator:
    case "+":
        print(f"Result of {num1} {operator} {num2} = {num1 + num2} ")
    case "-":
        print(f"Result of {num1} {operator} {num2} = {num1 - num2} ")
    case "*":
        print(f"Result of {num1} {operator} {num2} = {num1 * num2} ")
    case "/":
        print(f"Result of {num1} {operator} {num2} = {num1 / num2} ")
    case "%":
        print(f"Result of {num1} {operator} {num2} = {num1 % num2} ")
    case "**":
        print(f"Result of {num1} {operator} {num2} = {num1 ** num2} ")
    case "//":
        print(f"Result of {num1} {operator} {num2} = {num1 // num2} ")
    case _:
        print("Invalid Operator...")
