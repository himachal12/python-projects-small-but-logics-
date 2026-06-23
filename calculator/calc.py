def calc() :
    n1= float(input("Enter first number: "))
    operation= input("Enter operation (+, -, *, /): ")
    n2= float(input("Enter second number: "))
    if operation == "+":
        return n1 + n2
    if operation == "-":
        return n1 - n2
    if operation == "*":
        return n1 * n2
    if operation == "/":
        return n1 / n2

result = calc()
print("Result:", result)
def calc_with_same_number() :
    n3 = float(input("Enter another number: "))
    operation= input("Enter operation (+, -, *, /): ")
    if operation == "+":
        return result + n3
    if operation == "-":
        return result - n3
    if operation == "*":
        return result * n3
    if operation == "/":
        return result / n3

calculation = True

while calculation == True :
    question = input("Do you want to perform another calculation with the same number then yes and if new calculation  ? (yes/no): ").lower()
    if question == "yes" :
        result = calc_with_same_number()
        print("Result:", result)
    elif question == "no" :
        result = calc()
        print("Result:", result)
    
    
    
