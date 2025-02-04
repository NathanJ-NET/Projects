UserPrompt1 = input("Welcome to the useless conversion killer! \nWould you like to convert decimal to binary (1) or binary to decimal (2)")
if  UserPrompt1:='1':
    decimal_num = input("Enter your decimal value here: ")
    print(decimal_num)
else:
    print("/n I asked for a 1 or a 2, not whatever the hell you entered. Try again")

if UserPrompt1:='2':
    binary_num = input("Enter your binary number here: ")
else:
    print("I asked for a 1 or a 2, not whatever the hell you entered. Try again")
