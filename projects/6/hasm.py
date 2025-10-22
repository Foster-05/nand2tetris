#hasm: utilizes Parser and SymbolTable to assemble either a file or directory.
import sys
import ASMParser
ASMParser.Parser(sys.argv[1])
