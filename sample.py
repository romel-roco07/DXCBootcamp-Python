from pdb import Restart


print('Welcome to Karl ATM Bank Phils')
restart=('Y')
balance= 1000.00
chances = 3
while chances >= 0:
    pin = int(input('\nPlease Enter Your 4 Digit Pin: '))
    if pin == (1234):
        print('Pin Verified!\n')
        while restart not in ('n','NO', 'no','N'):
            print('*********** MENU ***********\n')
            print('Please Type 1 to check your balance\n')
            print('Please Type 2 to withdraw\n')
            print('Please Type 3 to deposit\n')
            print('Please Type 4 to quit\n')
            option = int(input('What Would you like to choose? = '))
            if option == 1:
                print('yourbalance is ',balance,'\n')
                restart = input('Would you like to go back to the  menu? Type y for yes and n for no: ')
                if restart in ('n','NO', 'no','N'):
                    print('Thank you for choosing Karl Bank')
                    break
            if option == 2:
                w_amount = float(input('Enter the amount you want to withdraw: \n'))
                reenter_amt=('Y')
                while w_amount > balance and reenter_amt=='Y':
                    reenter_amt = input('Insufficient Balance. Want to enter new amount? (y/n): ')
                    if(reenter_amt=='n'):
                        break
                    else:
                        w_amount = float(input('Enter the amount you want to withdraw: \n'))
                if w_amount < balance:
                    balance = balance - w_amount
                    print('Current Balance is PHP' +str(balance))
                restart = input('Would you like to go back to the  menu? Type y for yes and n for no: ')
                if restart in ('n','NO', 'no','N'):
                    print('Thank you for choosing Karl Bank')
                    break
            if option == 3:
                d_amount = float(input('Enter the amount you want to deposit: \n'))
                balance = balance + d_amount
                print('Deposit Successful. \nYour Current Balance is PHP' +str(balance))
                restart = input('Would you like to go back to the  menu? Type y for yes and n for no: ')
                if restart in ('n','NO', 'no','N'):
                    print('Thank you for choosing Karl Bank')
                    break
            elif option == 4:
                print('Please wait whilst you card is Returned...\n')
                print('Thank you for your service')
                break
            else:
                print('Please Enter a correct number, \n')
    elif pin != ('1234'):
        print('Incorrect Pin')
        chances = chances - 1
        if chances == 0:
            print('3 Attempts Alert, No More Tries')
            break




