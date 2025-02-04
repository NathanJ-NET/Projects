def start_decimal_to_binary_conversion():
    while True: 
        UserPrompt1 = input("Welcome to the useless conversion killer! \nWould you like to convert decimal to binary (1), binary to decimal (2), hexadecimal to binary (3), \nbinary to hexadecimal (4), decimal to hexadecimal (5), or hexadecimal to decimal (6)?")

        if UserPrompt1 == '1': 
            decimal_num = input("Enter your decimal value here: ")
            print(f"You want {decimal_num}? Sounds good! Doing calculations and stuff...")

            try:
                decimal_num = int(decimal_num)
                binary_num = bin(decimal_num)[2:]
                print(f"Here's your decimal value {decimal_num} in binary: {binary_num}")
            except ValueError:
                print("I asked for a valid integer, not whatever that is. Try again.")
                continue  

        elif UserPrompt1 == '2':
            binary_num = input("Enter your binary value here: ")
            print(f"You want {binary_num}? Sounds good! Doing calculations and stuff...")

            try:
                decimal_num = int(binary_num, 2)
                print(f"Here's your binary value {binary_num} as a decimal number: {decimal_num}.")
            except ValueError:
                print("I asked for a valid binary number, not whatever that is. Try again.")
                continue  
        elif UserPrompt1 == '3':
            hexa_num = input("Enter your hexadecimal value here: ")
            print(f"You want {hexa_num}? Sounds good! Doing calculations and stuff...")

            try:
                hexa_num = 
                print(f"Here's your hexadecimal value {hexa_num} as a binary value: {}.")
        else:
            print("I asked for a 1, 2, 3, 4, 5 or 6, not whatever the hell you entered. Try again.")
            continue  

        continue_or_exit = input("Would you like to perform another conversion? (y/n): ")
        if continue_or_exit.lower() != 'y':
            break

start_decimal_to_binary_conversion()
