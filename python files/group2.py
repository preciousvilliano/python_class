def group2():
    Account_name = input("enter user account name: " )
    Password = int(input("enter password"))
    import random
    Account_num = int( random.randint(100000000, 999999999))
    Account_bal =(0.00)

    print(f"Account_name: {Account_name}")
    print(f"password: {Password}")
    print(f"Account_num: {Account_num}")
    print(f"Account_bal: {Account_bal}")