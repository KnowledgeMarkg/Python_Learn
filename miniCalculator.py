num1 = input("Enter Num1 : ")
num2 = input("Enter Num2 : ")

num1 = int(num1)
num2 = int(num2)

operator = input("Enter Operator In (+, -, *, /, %) : " )

if operator=="+":
    print(num1+num2)
elif operator =="*":
    print(num1*num2)
elif operator =="-":
    print(num1-num2)
elif operator == "/":
    print(num1/num2)
elif operator =="%":
    print(num1%num2)
else:
    print("Enter Valid Operator : " )