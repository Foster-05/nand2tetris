#Calls VMTranslator and handles files and directories to provide an output.
from VMTranslator import VMTranslator
import sys

translator = VMTranslator(sys.argv[1])
translator.LogicNot()
translator.gt()
#Open file

with open(sys.argv[1], 'r') as f:
    for line in f:
        CurrLine = line
        CurrLine = cleanLine(CurrLine)
        if CurrLine != "":
            if CurrLine[0:2] == "pop":
                #Handle pop
                command = CurrLine.split("pop ")[1]
                translator.handlePushPop(command, 'pop')
                
            elif  CurrLine[0:3] == "push":
                #Handle push
                command = CurrLine.split("push ")[1]
                translator.handlePushPop(command, 'push')
                s
            elif CurrLine = 'and':
                translator.LogicAnd()
            elif CurrLine = 'or':
                translator.LogicOr()
            elif CurrLine = 'not':
                translator.LogicNot()
            else:
                #Other arithmetic logic instructions
                translator.CurrLine()

#TODO:
#figure out if @-1 works
#figure out how to jump back after subroutine calls
#X figure out calling each function, stepping through .vm 