#!/usr/bin/env python3

import operator

prev_result = 0

def percentage(val, perc):
    return val * (1 + perc / 100)

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '%': percentage,
    '//': operator.floordiv,
    '&': operator.and_,
    '|': operator.or_,
    '~': operator.invert,
    ':ans': None,
}

def calculate(myarg):
    global prev_result
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            if token == '~':
                arg = stack.pop()
                result = function(arg)
                stack.append(result)
            elif token == ":ans":
                stack.append(prev_result)
            else:
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = function(arg1, arg2)
                stack.append(result)
        # print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    #print("Result: ", stack[0])
    return stack.pop()

def main():
    global prev_result
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)
        prev_result = result

if __name__ == '__main__':
    main()
