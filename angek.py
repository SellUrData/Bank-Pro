# amount - Amount person wants to deposit
# bal - total after amount is added


# extract balance data from txt file
def read_dep():
    with open('data.txt', 'r') as file:
        read = file.readlines()
    # print(read[1])
    return((int(read[1])))

def read_wit():
    with open('data.txt', 'r') as file:
        read = file.readlines()
    # print(read[1])
    return((int(read[3])))

def read_bal():
    with open('data.txt', 'r') as file:
        read = file.readlines()
    # print(read[1])
    return((int(read[5])))

#bal takes from line 1 of the txt file 

# computes final balance after deposit
def deposit(bal, dep):
    amount = input("How much would you like to deposit? ")
    if amount.isdigit():
        amount = int(amount)
        if amount > 0:
            bal += amount
            dep += amount
            with open('data.txt', 'r+') as file:
                lines = file.readlines()
                lines[0] = "Total Amount Deposited" + '\n'
                lines[1] = str(dep) + '\n'
                lines[4] = "Total Balance" + '\n'
                lines[5] = str(bal) + '\n'
                file.seek(0)
                file.writelines(lines)
        else:
            print("amount must be greater than 0")
    else: 
        print ("Amount must be a number")
    print("Your New Balance is: " + str(bal))
    return bal



# computes final balance after withdrawls
def withdraw(bal, wit):
    grab = input("How much would you like to take out? ")
    if grab.isdigit():
        grab = int(grab)
        if grab > 0:
            if grab <= bal:
                bal -= grab
                wit -= grab
                with open('data.txt', 'r+') as file:
                    lines = file.readlines()
                    lines[2] = "Total Amount Withdrawn" + '\n'
                    lines[3] = str(wit) + '\n'
                    lines[4] = "Total Balance" + '\n'
                    lines[5] = str(bal) + '\n'
                    file.seek(0)
                    file.writelines(lines)      
            else:
                print("Insufficient funds")
        else:
            print("amount must be greater than 0")
    else: 
        print ("Amount must be a number")    
    print("Your New Balance is: " + str(bal))
    return bal


# deposit(read_bal, read_dep)

def follow_up():
    task = input("Anything else? ")
    if task == "yes":
        main(read_bal(), read_dep(), read_wit())
    elif task == "no":
        exit()
    else:
        print("Sorry we didn't get that")
        follow_up()

def main(bal, dep, wit):
    task = input("How can we get you started? ")
    if task == "deposit":
        deposit(bal, dep)
        follow_up()
    elif task == "withdraw":
        withdraw(bal, wit)
        follow_up()
    elif task == "balance":
        read_bal
        print(bal)
        follow_up()
    else:
        print("Your request was not understood. Would you like to make a deposit or a withdrawl")
    
main(read_bal(), read_dep(), read_wit())