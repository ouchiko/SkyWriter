#!/usr/bin/env python

import skywriter
import signal
import sys
import os

def clear():
    os.system('clear')

def cyclearea(x,y):
    clear()
    x=round(x*100)
    y=round(y*25)
    for ya in range(26):
        for xa in range(101):
            if (xa==x and ya==y):
                sys.stdout.write('^')
            else:
                sys.stdout.write('#')
        sys.stdout.write("\n")
    print x,y

@skywriter.touch()
def touch(arg):
    print "Touch ", arg

@skywriter.move()
def move(x,y,z):
    cyclearea(x,y)
    print (x,y,z)


signal.pause()
