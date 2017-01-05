from arithmetic import *

while True:
    user_input = raw_input("> ")
    tokens = user_input.split()
    infinite = []

    if tokens[0] == 'q':
        break

    int_tokens = tokens[1:]
    for i in int_tokens:
        number = float(i)
        infinite.append(number)

    # return number

    if tokens[0] == '+':
        print reduce(add, infinite)
    elif tokens[0] == '-':
        print reduce(subtract, infinite)
    elif tokens[0] == '*':
        print reduce(multiply, infinite)
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
