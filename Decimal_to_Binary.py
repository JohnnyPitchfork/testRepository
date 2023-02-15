#!/usr/bin/env python

# Decimal conversion table
in_binary = []

def calc_no_shooter(number):
    number = int(number)
    if number == 0 or number == 1:
        number = 0
    elif number == 2 or number == 3:
        number = 1
    elif number == 4 or number == 5:
        number = 2
    elif number == 6 or number == 7:
        number = 3
    elif number == 8 or number == 9:
        number = 4
    return number

def calc_with_shooter(number):
    number = int(number)
    if number == 0 or number == 1:
        number = 5
    elif number == 2 or number == 3:
        number = 6
    elif number == 4 or number == 5:
        number = 7
    elif number == 6 or number == 7:
        number = 8
    elif number == 8 or number == 9:
        number = 9
    return number


def digit_list(input_number):
    input_len = len(str(input_number))
    input_number = str(input_number)
    y = 0
    d_list = ""
    odd = False
    for i in range(0,input_len):
        x = int(input_number[i])
        
        if odd == False:
            y=str(calc_no_shooter(int(x)))
        else: 
            y=str(calc_with_shooter(int(x)))
        d_list = str(d_list) + str(y)

        if (x % 2) == 0:
            odd = False
        else:
            odd = True

    
    return d_list


def main():
    in_binary = []
    user_input = int(input('Enter whole number to convert to binary:\t'))

    primary_input = user_input

    while int(user_input) >= 1:

        if (user_input % 2) == 0:
            in_binary.insert(0,0)
        else:
            in_binary.insert(0,1)

        user_input = int(digit_list(user_input))
        print(user_input)
    print(f"{primary_input} in binary is: {in_binary}")
    

if __name__ == "__main__":
    main()