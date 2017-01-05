from arithmetic import *
input_file = open("calculator_data.txt")

while True:
    # uncomment below if direct user input is preferred:
    # user_input = raw_input("> ")
    user_input = input_file

    # goes through each line in input_file splitting on spaces
    for line in input_file:
        tokens = line.split()

        # creates an empty list to hold undetermined number of arguments
        int_numbers_to_calculate = []

        numbers_to_calculate = tokens[1:]
        for number in numbers_to_calculate:
            number = float(number)
            int_numbers_to_calculate.append(number)

        if tokens[0] == 'q':
            exit()
        if tokens[0] == '+':
            print reduce(add, int_numbers_to_calculate)
        elif tokens[0] == '-':
            print reduce(subtract, int_numbers_to_calculate)
        elif tokens[0] == '*':
            print reduce(multiply, int_numbers_to_calculate)
        elif tokens[0] == '/':
            print divide(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == 'square':
            print square(int(tokens[1]))
        elif tokens[0] == 'cube':
            print cube(int(tokens[1]))
        elif tokens[0] == 'pow':
            print power(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == 'mod':
            print mod(int(tokens[1]), int(tokens[2]))
        else:
            print "I don't understand that input"
