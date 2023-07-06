#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import getpass
import datetime

users = ['vijay', 'usama', 'afadat']
pins = ['1234', '2222', '3333']
amounts = [5000, 2000, 3000]
count = 0
print("****************************************************************************")
print("*                                                                          *")
print("*                   Welcome to HBL ATM SYSTEM                              *")
print("*                                                                          *")
print("****************************************************************************")
while True:
    user = input('\nENTER USER NAME: ')
    user = user.lower()
    if user in users:
        if user == users[0]:
            n = 0
        elif user == users[1]:
            n = 1
        else:
            n = 2
        break
    else:
        print('****************')
        print('INVALID USERNAME')
        print('****************')
      
current_date = datetime.date.today()
current_time = datetime.datetime.now().time()

while count < 3:
    print('********************************')
    pin = getpass.getpass("Enter your pin: ")
    print('********************************')
    if pin.isdigit():
        if user == 'vijay':
            if pin == pins[0]:
                break
            else:
                count += 1
                print('***********')
                print('INVALID PIN')
                print('***********')
                print()

        if user == 'usama':
            if pin == pins[1]:
                break
            else:
                count += 1
                print('***********')
                print('INVALID PIN')
                print('***********')
                print()

        if user == 'afadat':
            if pin == pins[2]:
                break
            else:
                count += 1
                print('***********')
                print('INVALID PIN')
                print('***********')
                print()
    else:
        print('************************')
        print('PIN CONSISTS OF 4 DIGITS')
        print('************************')
        count += 1


if count == 3:
    print('***********************************')
    print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
    print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
    print('***********************************')
    exit()

print('*************************')
print('LOGIN SUCCESFUL, CONTINUE')
print('*************************')
print()
print('**************************')
print(str.capitalize(users[n]), 'welcome to ATM')
print('**************************')
print('----------ATM SYSTEM-----------')
while True:

    print('*******************************')
    response = input('SELECT FROM FOLLOWING OPTIONS: \nCheckBalance__(c) \nWithdraw___(w) \nDeposit__(d) \nQuit_______(qq) \nType The Letter Of Your Choices: ').lower()
    print('*******************************')
    valid_responses = ['c', 'w', 'd', 'q']
    response = response.lower()
    if response == 'c':
        print('************************************************')
        print(current_date)
        print(current_time)
        print('************************************************')
        print( 'YOU HAVE ', amounts[n],'RUPEES ON YOUR ACCOUNT.')
        print('************************************************')

    elif response == 'w':
        print('*********************************************************')
        cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
        print('*********************************************************')
        if cash_out%10 != 0:
            print('********************************')
            print('AMOUNT YOU WANT TO WITHDRAW     ')
            print('********************************')
        elif cash_out > amounts[n]:
            print('*****************************')
            print(current_date)
            print(current_time)
            print('*****************************')
            print('YOU HAVE INSUFFICIENT BALANCE')
            print('*****************************')
        else:
            if cash_out >= 500 and cash_out <= 5000:
                amounts[n] = amounts[n] - cash_out
                print('*****************************')
                print(current_date)
                print(current_time)
                print('*******************************************')
                print('YOUR NEW BALANCE IS: ', amounts[n], 'Rupees')
                print('*******************************************')
            else:
                print('Amount Exceed the limit')
        

    elif response == 'd':
        print('********************************************************')
        deposite = int(input('ENTER AMOUNT YOU WOULD LIKE TO Deposit: '))
        print('********************************************************')
        if deposite%10 != 0:
            print('*******************************')
            print('AMOUNT YOU WANT TO Deposite    ')
            print('*******************************')
        else:
            amounts[n] = amounts[n] + deposite
            print('*******************************************')
            print(current_date)
            print(current_time)
            print('*******************************************')
            print('YOUR NEW BALANCE IS: ', amounts[n], 'Rupees')
            print('*******************************************')
    elif response =='q':
        print('**********************************************************')
        print('"You have been logged out.\n Thank you using HBL ATM!\n\n"')
        print('**********************************************************')
        exit()
    else:
        print('******************')
        print('RESPONSE NOT VALID')
        print('******************')



# In[ ]:




