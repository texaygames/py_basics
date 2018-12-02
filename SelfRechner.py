def calculate():
    ope = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    num_1 = int(input("Please Type in your first number: "))
    num_2 = int(input("Please Type in your second number: "))

    if ope == "+":
        print("{} + {} = ".format(num_1, num_2))
        print(num_1 + num_2)

    elif ope == "-":
        print("{} - {} = ".formate(num_1, num_2))
        print(num_1 - num_2)

    elif ope == "*":
        print("{} * {} = ".formate(num_1, num_2))
        print(num_1 * num_2)

    elif ope == "/":
        print("{} / {} = ".formate(num_1, num_2))
        print(num_1 / num_2)

    else:
        print("You have not typed in a valid number")

    again()

def again():
    calc_again = input("Möchtest du noch einmal rechnen? [J/N]")

    if calc_again.upper() == "J":
        calculate()
    elif calc_again.upper() == "N":
        print("Bis Balt!  :)")

    else:
        again()

calculate()
