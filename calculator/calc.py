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


question = input("Do you want to perform another calculation with the same number then yes and if new calculation  ? (yes/no): ").lower()
while question == "yes":
    result = calc_with_same_number()
    print("Result:", result)
    question = input("Do you want to perform another calculation with the same number then yes and if new calculation  ? (yes/no): ").lower()
    
else :
    result = calc()
print("Result:", result)

    
    
