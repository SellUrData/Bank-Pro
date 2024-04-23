balance = 30

def database_entry():
    balance = str(30)
    file = open('data.txt', 'w')
    file.write(balance)

def database_read():
    file = open('data.txt', 'r')


def deposit(bal):
    amount = input("How much would you like to deposit? ")
    if amount.isdigit():
        amount = int(amount)
        if amount > 0:
            bal += amount
            break
        else:
            print("amount must be greater than 0")
    else: 
        print ("Amount must be a number")
    print(amount)
    return amount

    

def withdraw(bal):
    while True:
        grab = input("How much would you like to take out? ")
        if grab.isdigit():
            grab = int(grab)
            if grab > 0:
                if grab <= bal:
                    break
                else:
                    print("Insufficient funds")
            else:
                print("amount must be greater than 0")
        else: 
            print ("Amount must be a number")     
    return grab

def follow_up():
    task = input("Anything else? ")
    if task == "yes":
        main()
    elif task == "no":
        exit()
    else:
        print("Sorry we didn't get that")
        follow_up()

def main():
    task = input("How can we get you started? ")
    if task == "deposit":
        dbalance = deposit(balance)
        print("Your new account balance is $" + str(dbalance))
        database_entry()
        follow_up()
    elif task == "withdraw":
        wbalance = withdraw(balance)
        wbalance -= balance
        print("Your new account balance is $" + str(wbalance))
        follow_up()
    elif task == "balance":
        ubalance = dbalance - wbalance
        print(ubalance)
        follow_up()
    else:
        print("Your request was not understood. Would you like to make a deposit or a withdrawl")
        main()

deposit(balance)


# print("your total acount balance is now $" + str(ubalance))