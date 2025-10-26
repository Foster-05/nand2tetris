#Calls VMTranslator and handles files and directories to provide an output.
from VMTranslator import VMTranslator
import sys

translator = VMTranslator(sys.argv[1])
translator.LogicNot()
translator.gt()
#Open file
# 
# with open(sys.argv[1], 'r') as f:
#     for line in f:
#         CurrLine = line
#         CleanLine()
#         if CurrLine != "":
#             if CurrLine[0] != "(":
#                 ROMAddress += 1
#             elif CurrLine[0] == "(":
#                 Sym = CurrLine.split("(")[1].split(")")[0]
#                 symboltranslator.addEntry(Sym, ROMAddress)
#                 





#TODO:
#figure out if @-1 works
#figure out how to jump back after subroutine calls
#figure out calling each function, stepping through .vm