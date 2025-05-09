from tqdm import tqdm
import time
# UT10030,i'm sivakumar glezian and im submitting my new banking app'Global internationals'
# firstly thanks unicomtic & to trust my contribution.
# it consists normal banking functions
# firstly login
# next code figures shows the banking functions..............................................................
print('Hello user: Welcome to our global international banking')
print("Starting global banking...")
print( 'this is our main branch code is 00048')
print('dear customer we are ready to finishing requests')


# Progress bar for starting
for _ in tqdm(range(5), desc="Starting bank programme"):
    time.sleep(0.3)  

# Banking function to get user data and write to file
def banking_functions():
    user_name = input('Enter the new user name: ')
    user_id_number = int(input('Enter the new user ID number: '))
    user_account_num = int(input('Enter the account number: '))
    with open('sample.txt', 'w') as file:
        file.write(f'User Name: {user_name}\n')
        file.write(f'User ID Number: {user_id_number}\n')
        file.write(f'User Account Number: {user_account_num}\n')
# Call banking function
banking_functions()

print("Logging in, please wait...")
for _ in tqdm(range(5), desc="Processing"):
    time.sleep(0.3)  

print("Login successfully.")

# Deposit and withdrawal
deposit = int(input('Enter the deposit amount: '))
withdraw = int(input('Enter the withdraw amount: '))
available = deposit - withdraw
with open('sample.txt', 'w') as file:
        file.write(f'deposit amount is: {deposit}\n')
        file.write(f'withdrawal amount is: {withdraw}\n')
        file.write(f'available balance is: {available}\n')
        file.close()


# Banking calculations function
def banking_calculations(deposit, withdraw, available):
    print("Available Balance:", available)
    if available > 0:
        print('Transaction successful.')
    elif available == 0:
        print('Balance is zero.')
    else:
        print('Insufficient funds.')


banking_calculations(deposit, withdraw, available)
# if any unwanted codes here, next time i will correct for coming other projects
# thankyou unicomtic
