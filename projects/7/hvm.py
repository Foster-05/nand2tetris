#Calls VMTranslator and handles files and directories to provide an output.
from VMTranslator import VMTranslator
import sys

translator = VMTranslator()
#Open file
translator.handle(sys.argv[1])
