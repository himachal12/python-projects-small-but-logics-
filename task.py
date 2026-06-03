alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def ceaser_cyphere(orignal_text , shift_amount, DIRECTIONALITY) :
    cypher_text = " "
    if DIRECTIONALITY == "decode" :
            shift_amount *= -1
    for char in orignal_text :
       
        if char in alphabet :
            position = alphabet.index(char)
            shifted_position = (position + shift_amount) % 26
            cypher_text += alphabet[shifted_position]
            
        else :
            cypher_text += char
    print(f"the {DIRECTIONALITY}d text is {cypher_text}")
ceaser_cyphere(text , shift, direction)

condition = True
while condition == True :
    question = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if question == "yes" :
        condition = True
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        ceaser_cyphere(text , shift, direction)
    elif question == "no" :
        condition = False
        print("Goodbye!")
        condition = False