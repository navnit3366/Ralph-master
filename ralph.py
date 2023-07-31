#Josiah N Savage 1/10/18


final_output = []

total_spent = []

def openingStatement():
    while True:
        print("Hello my name is Ralph!")
        print("I will be helping you balance your checking account.")
        print("Side tip: Press enter after you finish each input so that I will know you are ready to continue!")
        print("So lets begin!")
        break
opening_statement = openingStatement()
#p stands for promt

#q stands for question
p1 = input("Lets start by entering the date of the transactions: ")

#r stands for response



while True:
    r_to_p1 = input("Thank you! The date of the transactions is {}. Is that correct?(y/n): ".format(p1).lower())
    if r_to_p1 == "y":
        final_output.append(p1)
        print("Great so lets continue on!")
        break
    elif r_to_p1 == "n":
        print("Well lets go ahead and correct that")
        p2 = input("Please re-enter todays date: ")
        continue
#o stands for output



while True:
    p3 = input("Please list the name of the transaction: ")
    p3_2 = float(input("Thanks! Now enter the amount of the transaction: "))
    p3_3 = input("Awesome you're doing great! Now enter the time of the transaction: ")
    print("Name: {} Amount: ${} Time of purchase: {}".format(p3,p3_2,p3_3))
    q4 = input("Is the above information correct?(y/n): ".lower())

    if q4 == "y":
        final_output.append(p3)
        final_output.append(p3_2)
        final_output.append(p3_3)
        total_spent.append(p3_2)
    q5 = input("Awesome! Would you like to do another one (y/n)?: ".lower())
    if q5 == "y":
        continue
    elif q5 == "n":
        break
    elif q4 == "n":
        p4 = input("Lets fix that then!")
        continue

def sum(total_spent):
    total = 0
    for x in total_spent:
        total += x

    return total
 
print("Here is a list of your transactions:",final_output)

print("Here is the total spent:", sum(total_spent))

print("Thank you very much for using Ralph. We hope to see you again!")  

