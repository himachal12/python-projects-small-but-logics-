dictinary = {}
def bider () :
    print("welcome to the auction")
    name = input("what is your name? \n")
    bid = int(input("what is your bid? \n$"))
    dictinary[name] = bid

bider()

question = input("are there any other bidders? type 'yes' or 'no'.\n").lower()
while question == "yes" :
    bider()
    question = input("are there any other bidders? type 'yes' or 'no'.\n").lower()
else :
    print("the winner is " + max(dictinary, key=dictinary.get) + " with a bid of $" + str(max(dictinary.values())))