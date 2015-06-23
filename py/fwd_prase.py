#!/bin/python

# # by fohnwind. 20150623 V 0.0.2

import sys

def brace(url):
    head,tmp = url.split("{")
    end = tmp.split("}")
    middle = end[0]
    tail = end[-1]
    item = middle.split(",")
    result = []
    for i in item:
        result.append(head+i+tail)
    
    return result

def bracket(url):
    head,tmp = url.split("[")
    end = tmp.split("]")
    middle = end[0]
    tail = end[-1]
    actiontype = 0
    action = middle.split("-")
    if action[0].isdigit():
        actiontype = 1
        a = int(action[0])
        b = int(action[1]) + 1
    else:
        a = ord(action[0])
        b = ord(action[1])+1

    if a >= b:
        print "wrong range"
        sys.exit(-1)

    result = []
    for i in xrange(a,b):
        if actiontype:
            result.append(head+str(i)+tail)
        else:
            result.append(head+chr(i)+tail)
    return result

def main():
    global result
    result = []
    goal = sys.argv[1]
    for i in sys.argv[1:]:
        goal = i
        get = judge(goal)

        if get is not None:
            for i in get:
                print i
                #pass

def judge(goal):
    if type(goal) != type(['a']):
        temp = [goal]
    else:
        temp = goal

    for i in temp:
        if i is None:
            break

        if i.find('[') > 0:
            judge(bracket(i))
        elif i.find('{') > 0:
            judge(brace(i))
        else:
            result.append(i)

    return result

if __name__ == '__main__':
    main()


