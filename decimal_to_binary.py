def start_decimal_to_binary_conversion():
    while True: 
        UserPrompt1 = input("Welcome to the useless conversion killer! \nWould you like to convert decimal to binary (1) or binary to decimal (2)? ")

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
        
        else:
            print("I asked for a 1 or a 2, not whatever the hell you entered. Try again.")
            continue  

        continue_or_exit = input("Would you like to perform another conversion? (y/n): ")
        if continue_or_exit.lower() != 'y':
            break

start_decimal_to_binary_conversion()
