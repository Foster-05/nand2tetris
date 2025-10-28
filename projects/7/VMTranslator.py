#Provides VM translation functions to hasm.
import os

class VMTranslator:
##############################################################################
    def handle(self, inputfile):
        #Handle file vs file in directory
        if os.path.isdir(inputfile):
            self.normDirName = os.path.normpath(inputfile)
            [self.path, self.name] = os.path.split(self.normDirName)
            self.outputfile = os.path.join(self.path, self.name, self.name + ".asm")
            self.init()
            for f in os.listdir(inputfile):
                if f.endswith('.vm'):
                    print(f'Processing {f}')
                    VMName = os.path.join(inputfile, f)
                    self.Process(VMName)
        else:
            print('file')
            self.outputfile = inputfile.replace(".vm", ".asm")
            self.init()
            self.Process(inputfile)

    def init(self):
        #this needs to be separate i swear
        self.f = open(self.outputfile, 'a')
        
        self.locationdir = {
            'local':"LCL",
            'argument':"ARG",
            'this':"THIS",
            'that':"THAT",
            'temp':'R5'
            }
        
        self.symbolCount = 0
        
    def Process(self, file):
        with open(file, 'r') as f:
            for line in f:
                CurrLine = line
                CurrLine = self.cleanLine(CurrLine)
                if CurrLine != "":
                    if CurrLine[0:2] == "pop":
                        #Handle pop
                        command = CurrLine.split("pop ")[1]
                        self.handlePushPop(command, 'pop')
                        
                    elif  CurrLine[0:3] == "push":
                        #Handle push
                        command = CurrLine.split("push ")[1]
                        self.handlePushPop(command, 'push')
                    elif CurrLine == 'and':
                        self.LogicAnd()
                    elif CurrLine == 'or':
                        self.LogicOr()
                    elif CurrLine == 'not':
                        self.LogicNot()
                    elif CurrLine == 'add':
                        #Other arithmetic logic instructions
                        self.add()
                    elif CurrLine == 'sub':
                        self.sub()
                    elif CurrLine == 'neg':
                        self.neg()
                    elif CurrLine == 'eq':
                        self.eq()    
                    elif CurrLine == 'gt':
                        self.gt()
                    elif CurrLine == 'lt':
                        self.lt()
        ################################################################################3
        
    def cleanLine(self, CurrLine):
            # remove line endings
            line = CurrLine.strip()
            # remove comments -- split the line at the first comment character
            #                    and only keep leftmost portion
            line = line.split("//")[0].strip()
            return line
        
    def handlePushPop(self, command, type):
        #Determines memory segments etc
        try:
            segment, index = command.split(" ")
            index = int(index)
        except:
            print('unable to split command')
        if segment in self.locationdir:
            location = self.locationdir[segment]
            if type == 'push':
                self.pushValue(location, index)
            else:
                self.pop(location, index)
                
        elif segment == 'pointer':
            if index == 1:
                location = 'THAT'
            elif index == 0:
                location = 'THIS'
            else:
                print('pointer offest failed')
                
            if type == 'push':
                self.pushValue(location, 0)
            else:
                self.pop(location, 0)
                
        elif segment == 'constant':
            self.f.write('@' + index + "\n")
            self.f.write('D=A' + "\n")
            #Only pushes
            self.pushD()
        elif segment == 'static':
            staticvar = self.outputfile + "." + str(index)
            self.f.write('@' + staticvar + "\n")
            self.f.write('D=A' + "\n")
            if type == 'push':
                self.pushD()
            else:
                self.pop(staticvar, 0)
        else:
            print('unrecognized segment')
            
###############################################################################        
        #Push-pop
    def popD(self, location, offsetin):
        #Where location will already be a defined @XXX value and offsetin is an integer
            #Addr = location + i, store in R13
            self.f.write("@" + location + "\n")
            self.f.write("A=M" + "\n")
            self.offset(offsetin)
            self.f.write("D=A" + "\n")
            #Temporary storage
            self.f.write("@R13" + "\n")
            self.f.write("M=D" + "\n")
            #SP--
            self.f.write("@SP" + "\n")
            self.f.write("M=M-1" + "\n")
            #Addr = SP
            self.f.write("D=M" + "\n")
            self.f.write("@R13" + "\n")
            self.f.write("A=M" + "\n")
            self.f.write("M=D" + "\n")
        
    def pushD(self):
            self.f.write("@SP" + "\n")
            self.f.write("A=M" + "\n")
            self.f.write("M=D" + "\n")
            self.f.write("@SP" + "\n")
            self.f.write("M=M+1" + "\n")
            
    def pushValue(self, location, offsetin):
            #Addr = location + i, store in R13
            self.f.write("@" + location + "\n")
            self.f.write("A=M" + "\n")
            self.offset(offsetin)
            #Read value @ location + offset
            self.f.write("D=M" + "\n")
            self.pushD()
###################################################################################
        #Arithmetic-Logical commands

    def offset(self, i):
            self.offsetstr = "A=A+1 \n" * int(i)
            self.f.write(self.offsetstr)
        
    def add(self):
        #Pops two most recent values off the stack, adds, and pushes back on
            self.popD('R13', 0)
            self.popD('R14', 0)
            self.f.write("@R13" + "\n")
            self.f.write("D=M" + "\n")
            self.f.write("@R14" + "\n")
            self.f.write("D=D+M" + "\n")
            self.pushD()
        
    def sub(self):
        #Pops two most recent values off the stack, subtracts, and pushes back on
            self.popD('R13', 0)
            self.popD('R14', 0)
            self.f.write("@R13" + "\n")
            self.f.write("D=M" + "\n")
            self.f.write("@R14" + "\n")
            self.f.write("D=D-M" + "\n")
            self.pushD()
        
    def neg(self):
            #Arithmetic negation
            self.popD('R13', 0)
            self.f.write("@R13" + "\n")
            self.f.write("D=-M" + "\n")
            self.pushD()
        
    def eq(self):
        #Determines if two most recent values on the stack are equal and pushes back true (-1) or false (0)
            self.popD('R13', 0)
            self.popD('R14', 0)
            self.f.write("@R13" + "\n")
            self.f.write("D=M" + "\n")
            self.f.write("@R14" + "\n")
            self.f.write("D=D-M" + "\n")
            #D=0 if equal, valued if not
            self.f.write("@ETrue" + str(self.symbolCount) +"" + "\n")
            self.f.write("D;JEQ" + "\n")
            #If greater than, jump past false and push true
            #If less than, push false
            self.f.write("D=0" + "\n")
            self.pushD()
            self.f.write("@EFalse" + str(self.symbolCount) +"" + "\n")
            self.f.write("D;JMP" + "\n")
            #Always jump because we wrote
            #Create unique symbols that will skip the "true" write if false
            self.f.write("(ETrue" + str(self.symbolCount) +")" + "\n")
            #Write true
            self.f.write("D=-1" + "\n")
            self.pushD()
            self.f.write("(EFalse" + str(self.symbolCount) +")" + "\n")
            #Empty, we wrote previously
            self.symbolCount += 1
        
    def gt(self):
        #Determines if two most recent values on the stack, x>y and pushes back true (-1) or false (0)
        #y is the most recent item on the stack, popped to R13
            self.popD('R13', 0)
            self.popD('R14', 0)
            self.f.write("@R14" + "\n")
            self.f.write("D=M" + "\n")
            self.f.write("@R13" + "\n")
            #x-y
            self.f.write("D=D-M" + "\n")
            #D>0 if gt, negative if not
            self.f.write("@GTrue" + str(self.symbolCount) +"" + "\n")
            self.f.write("D;JGT" + "\n")
            #If greater than, jump past false and push true
            #If less than, push false
            self.f.write("D=0" + "\n")
            self.pushD()
            self.f.write("@GFalse" + str(self.symbolCount) +"" + "\n")
            self.f.write("D;JMP" + "\n")
            #Always jump because we wrote
            #Create unique symbols that will skip the "true" write if false
            self.f.write("(GTrue" + str(self.symbolCount) +")" + "\n")
            #Write true
            self.f.write("D=-1" + "\n")
            self.pushD()
            self.f.write("(GFalse" + str(self.symbolCount) +")" + "\n")
            #Empty, we wrote previously
            self.symbolCount += 1
    def lt(self):
        #Determines if two most recent values on the stack, x<y and pushes back true (-1) or false (0)
        #y is the most recent item on the stack, popped to R13
            self.popD('R13', 0)
            self.popD('R14', 0)
            self.f.write("@R13" + "\n")
            self.f.write("D=M" + "\n")
            self.f.write("@R14" + "\n")
            #y-x
            self.f.write("D=D-M" + "\n")
            #D>0 if lt, negative if not
            self.f.write("@LTrue" + str(self.symbolCount) +"" + "\n")
            self.f.write("D;JGT" + "\n")
            #If greater than, jump past false and push true
            #If less than, push false
            self.f.write("D=0" + "\n")
            self.pushD()
            self.f.write("@LFalse" + str(self.symbolCount) +"" + "\n")
            self.f.write("D;JMP" + "\n")
            #Always jump because we wrote
            #Create unique symbols that will skip the "true" write if false
            self.f.write("(LTrue" + str(self.symbolCount) +")" + "\n")
            #Write true
            self.f.write("D=-1" + "\n")
            self.pushD()
            self.f.write("(LFalse" + str(self.symbolCount) +")" + "\n")
            #Empty, we wrote previously
            self.symbolCount += 1
        
    def LogicAnd(self):
        #Computes bitwise AND of x,y and pushes back to stack
            self.popD('R13', 0)
            self.popD('R14', 0)
            self.f.write("@R13" + "\n")
            self.f.write("D=M" + "\n")
            self.f.write("@R14" + "\n")
            #x&y
            self.f.write("D=D&M" + "\n")
            self.pushD()
    def LogicOr(self):
        #Computes bitwise OR of x,y and pushes back to stack
            self.popD('R13', 0)
            self.popD('R14', 0)
            self.f.write("@R13" + "\n")
            self.f.write("D=M" + "\n")
            self.f.write("@R14" + "\n")
            #x|y
            self.f.write("D=D|M" + "\n")
            self.pushD()
    def LogicNot(self):
        #Computes bitwise NOT of y and pushes back to stack
            self.popD('R13', 0)
            self.popD('R14', 0)
            self.f.write("@R13" + "\n")
            self.f.write("D=M" + "\n")
            self.f.write("@R14" + "\n")
            #!y
            self.f.write("D=!D" + "\n")
            self.pushD()
            
    ##################################################################################################

