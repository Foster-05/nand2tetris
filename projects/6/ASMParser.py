#ASMParser: Reads through a given .asm file, utilizing Symbols, and stores output to .hack file using Coder.
import os
from ASMCoder import Coder
from ASMSymbols import Symbols
import time
class Parser:
    def __init__(self, inputfile):
        #Find output file, treating directories as necessary
        self.ROMAddress = 0
        self.previousRom = 0
        self.AvailableRAM = 16
        self.sym = ''
        self.CurrLine = ''
        self.output = ''
        self.coder = Coder()
        self.symboltranslator = Symbols()
        self.lineno = 0
        self.more = 0
        self.inputfile = inputfile
        
        self.HandleFile()
        self.FirstPass()
        self.SecondPass()

                
                
    def CleanLine(self):
        # remove line endings
        line = self.CurrLine.strip()
        # remove comments -- split the line at the first comment character
        #                    and only keep leftmost portion
        line = line.split("#")[0].strip() #and strip for good measure
        line = line.split("//")[0].strip()
        self.CurrLine = line
        print(line)
        
    def symbol(self, line):
        try:
            self.sym = line.split("@")[1]
            try:
                self.sym = int(self.sym)
            except:
                print("label")
        except:
            self.sym = line.split("(")[1].split(")")[0]
            try:
                self.sym = int(self.sym)
            except:
                print("label")
        
    def HandleFile(self):
        #Handle file vs file in directory
        if os.path.isdir(self.inputfile):
            print('dir')
            self.normDirName = os.path.normpath(dir)
            [self.path, self.name] = os.path.split(normDirName)
            self.outfile = os.path.join(path, name, name + ".hack")
        else:
            print('file')
            self.outfile = self.inputfile.replace(".asm", ".hack")
            
    def FirstPass(self):
        #Open file
        with open(self.inputfile, 'r') as self.f:
        #First pass
            for line in self.f:
                self.CurrLine = line
                self.CleanLine()
                if self.CurrLine != "":
                    if self.CurrLine[0] != "(":
                        self.ROMAddress += 1
                    elif self.CurrLine[0] == "(":
                        self.Sym = self.CurrLine.split("(")[1].split(")")[0]
                        self.symboltranslator.addEntry(self.Sym, self.ROMAddress)
                        
    def SecondPass(self):
        #Second pass
        #File is closed, reopen so we seek back to the first line
        self.f = open(self.inputfile, 'r')
        with open(self.outfile, 'w') as self.fi:
            for line in self.f:
                self.CurrLine = line
                self.CleanLine()
                self.sym = ""
                
                if self.CurrLine == "":
                    continue
                else:
                    self.lineno += 1
                    
                    if self.CurrLine[0] == "@":
                        #A comm
                        self.HandleA()
                        continue
                        
                    elif "=" in self.CurrLine:
                        #C comm  
                        self.HandleC()
                        continue
                    
                    elif ";" in self.CurrLine:
                        #Pure jump comm
                        self.HandleJump()
                        continue
                    
                    elif ")" in self.CurrLine:
                        #L comm
                        self.symbol(self.CurrLine)
                        self.symboltranslator.GetAddress(self.sym)
                        continue
                    
                    else:
                        #C comm with no destination or jump
                        self.comp = self.CurrLine
                        self.jump = "null"
                        self.dest = "null"
                        self.output = self.coder.combine(self.comp, self.dest, self.jump)
                        self.WriteOut(self.fi, self.output)
                        
    def HandleSymbol(self):
        if type(self.sym) != int:
                            #If it's a symbol, check if it's in the table and get address before or after adding
                            if self.symboltranslator.contains(self.sym):
                                self.sym = self.symboltranslator.GetAddress(self.sym)
                            else:
                                self.symboltranslator.addEntry(self.sym, self.AvailableRAM)
                                self.AvailableRAM += 1
                                self.sym = self.symboltranslator.GetAddress(self.sym)
    
    def BinaryConversion(self, input):
        self.binary = bin(int(input))[2:]
                        
        if len(self.binary) != 16:
            pad = 16 - len(self.binary)
            self.output = ("0"*pad) + self.binary
        else:
            self.output = self.binary

    def WriteOut(self, file, input):
        file.write(str(input) + "\n")
        print(input)
        
    def Strip(self):
        self.dest = self.dest.strip()
        self.comp = self.comp.strip()
        self.jump = self.jump.strip()
        
    def HandleA(self):
        self.symbol(self.CurrLine)
        self.HandleSymbol()
        #self.sym will now be the integer address to goto
        self.BinaryConversion(self.sym)
        self.WriteOut(self.fi, self.output)
    
    def HandleC(self):
        self.dest, self.rest = self.CurrLine.split("=")
        try:
            self.comp, self.jump = self.rest.split(";")
            print('split')
        except:
            self.comp = self.rest
            self.jump = "null"
        
        self.Strip()
        self.output = self.coder.combine(self.comp, self.dest, self.jump)
        self.WriteOut(self.fi, self.output)

    def HandleJump(self):
        self.comp, self.jump = self.CurrLine.split(';')
        self.dest = "null"
        self.Strip()
        self.output = self.coder.combine(self.comp, self.dest, self.jump)
        self.WriteOut(self.fi, self.output)
        
