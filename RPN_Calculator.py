#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: pandian_krishna
Recreated an Old Lab because I was bored
"""

import math
import operator
ops = {'+':operator.add,    #take data from operator
       '-':operator.sub,
       '*':operator.mul,
       '/':operator.truediv}

def Valid(s):   #checks if it's valid 
    try:
        float(s)
        return True
    except ValueError:
        return False

def calculate(equation):
    stack = []
    result = None
    for i in equation:
        if Valid(i):
            stack.insert(0,i)   #inserts the value
            if len(stack) > 50: #stops the size
                print('Too Many Characters')
        else:
            if len(stack) < 2:  #make sure it doesn't fail
                print('Not Enough Space')
                break
            else:
                if len(i) == 1:
                    int1 = float(stack.pop(1))
                    int2 = float(stack.pop(0))
                    result = ops[i](int1,int2)
                    stack.insert(0,str(result))
                else:
                    int1 = float(stack.pop(0))
                    result = ops[i](math.radians(int1))
                    stack.insert(0,str(result))
    if len(stack) > 1:  #checks if stack still has values
        result = None
    return result


def main():
    while True: #infinite loop
        raw_input = input('Enter a Valid equation: ').split(' ')
        answer = calculate(raw_input)
        if answer == None:
            print('Invalid String')
        else:    
            print('Answer: %02f' % answer)


if __name__ == '__main__':
    main()