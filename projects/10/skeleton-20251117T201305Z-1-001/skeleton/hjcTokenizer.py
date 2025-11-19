import hjcConstants as CONSTS

class Tokenizer(object):
    def __init__(self, sourceName):
        """
        Open 'sourceFile' and gets ready to parse it.
        """
        self.sourceFileName = sourceName
        self.fp = open(sourceName, 'r');
        self.lineNumber = 0
        self.line = ''
        self.rawline = ''
        self.inComment = False
        self.tokentype = TK_NONE
        
        # Initialize other varibles here

    def close(self):
        self.fp.close()

    def getNextLine(self):
        try:
            self.rawline = next(self.fp)
            self.lineNumber += 1
        except StopIteration:
            return False

    def _eat(self):
        """
        'Eats' the frontmost character of self.line
        """
        self.line = self.line[1:]

    def Advance(self):
        """
        Reads the next command from the input and makes it the current
        command.
        Returns True if a command was found, False at end of file.
        """
        if length(self.rawline) == 0:
            #get new line and increment line number
            if not self.getNextLine(): #sets new line and increases lineNumber
                return False
            else:
                #New line found
                self.line = self.rawline.replace("\n",'').strip() #Remove newline indicator
                #Remove comments
                self.line = self.line.split("//")[0].strip()
                if self.inComment:
                    if self.line.count("*/") != 0:
                        self.line = self.line.split("*/")[1].strip()
                        self.inComment = False
                    else:
                        self.line = ""
                if self.line.count("/*") != 0:
                    if self.line.count("*/") != 0:
                        self.line = self.line.split("/*")[1].split("*/")[1].strip() #Remove comment section
                    else:
                        self.inComment = True
                        self.line = self.line.split("/*")[0].strip()
                #Replace tabs with spaces
                self.line.replace('\t', '   ').strip()
                
                if length(self.line) == 0:
                    self.Advance() #Loop back
                    
                self._Parse()
                    
    def LineNumber(self):
        pass


    def LineStr(self):
        pass


    def tokenType(self):
        return self.tokentype


    def TokenTypeStr(self):
        pass


    def Keyword(self):
        pass


    def KeywordStr(self, keywordId=None):
        pass


    def Symbol(self):
        return self.symbol


    def identifier(self):
        return ident


    def intVal(self):
        return inte


    def StringVal(self):
        return stri


    def _Parse(self):
            #Parse
        i=0
        j = length(self.line)
        while j > 0:
            if self.line[i] == " ":
                self._eat()
                pass
            elif self.line[i] in CONSTS.symbols:
                self.tokentype = TK_SYMBOL
                self.symbol = self.line[i]
                self.eat()
                
            elif self.line[i].isdigit():
                self.tokentype = TK_INT_CONST
                self._ParseInt(i)
                
            elif self.line[i] in CONSTS.identStart:
                k = 0
                self.templine = ""
                for k < 11:
                    self.templine += self.line[i+k]
                    if self.templine in CONSTS.keywords:
                        self.tokentype = TK_KEYWORD
                        return self.templine #return keyword
                    else:
                        self.tokentype = TK_IDENTIFIER
                        k += 1
                self._ParseIdent(i) #parse identifier starting back from beginning
                
            elif self.line[i] == '"':
                self.tokentype = TK_STRING_CONST
                self._ParseString()
            i += 1
            j -= 1


    def _ParseInt(self, i):
        self.templine = ""
        while True:
            if self.line[i].isdigit():
                self.templine += self.line[i]
                self.eat()
            else:
                break
        inte = self.templine()
        pass


    def _ParseIdent(self, i):
        self.templine = ""
        while True:
            if self.line[i] in CONSTS.identChars:
                self.templine += self.line[i]
                self.eat()
            else:
                break
        ident = self.templine()
        pass

    def _ParseString(self):
        self.templine = ""
        while True:
            if self.line[i] == '"':
                self.eat()
                break
            else:
                self.templine += self.line[i]
        stri =  self.templine
        pass