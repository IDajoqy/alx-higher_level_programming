#!/usr/bin/python3
f __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argc = len(argv)
    if argc != 4:
        print('usage: {} <1> <operator> <b>'.format(argv[0]))
        exit(1)
    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div,
    }
    if argv[2] in ops:
        num1 = int(argv[1])
        num2 = int(argv[3])
        op = ops[argv[2]]
        result = op(num,1, num2)
        print('{{:d {:s} {:d} = {:d}'.format(num1, argv[2], num2,result))
    else:
        print('unknown operator. available operators: +, -, *, and /')
        exit(0)
