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
                translator.handleCommand(command)
                a
            elif  CurrLine[0:3] == "push":
                #Handle push
                command = CurrLine.split("push ")[1]



#TODO:
#figure out if @-1 works
#figure out how to jump back after subroutine calls
#figure out calling each function, stepping through .vm