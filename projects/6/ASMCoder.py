#ASMCoder: Utilizes Hack Assembly notation to translate a given C instruction line into binary.
class Coder:
    def __init__(self):
        #Define dictionary with translations
        self.dest = {
            "null":"000",
            "M":"001",
            "D":"010",
            "MD":"011",
            "A":"100",
            "AM":"101",
            "AD":"110",
            "AMD":"111"
            }
        self.comp = {
            #Computation outputs including A bit
            "0":"0101010",
            "1":"0111111",
            "-1":"0111010",
            "D":"0001100",
            "A":"0110000",
            "M":"1110000",
            "!D":"0001101",
            "!A":"0110001",
            "!M":"1110001",
            "-D":"0001111",
            "-A":"0110011",
            "-M":"1110011",
            "D+1":"0011111",
            "A+1":"0110111",
            "M+1":"1110111",
            "D-1":"0001110",
            "A-1":"0110010",
            "M-1":"1110010",
            "D+A":"0000010",
            "D+M":"1000010",
            "D-A":"0010011",
            "D-M":"1010011",
            "A-D":"0000111",
            "M-D":"1000111",
            "D&A":"0000000",
            "D&M":"1000000",
            "D|A":"0010101",
            "D|M":"1010101"
            }
        self.jump = {
            "null":"000",
            "JGT":"001",
            "JEQ":"010",
            "JGE":"011",
            "JLT":"100",
            "JNE":"101",
            "JLE":"110",
            "JMP":"111"
            }
    def get_comp(self, input):
        try:
            self.compout = self.comp[input]
            print(self.compout)
            print('x')
        except:
            print("input must be a valid computation string.")
            
    def get_dest(self, input):
        try:
            self.destout = self.dest[input]
            print('y')
        except:
            print("input must be a valid destination string.")
            
    def get_jump(self, input):
        try:
            self.jumpout = self.jump[input]
            print('z')
        except:
            print("input must be a valid jump string.")        

    def combine(self, comp, dest, jump):
        self.compout = ""
        self.destout = ""
        self.jumpout = ""
        
        self.get_dest(dest)
        self.get_comp(comp)
        self.get_jump(jump)
        
        self.encoding = "111" + self.compout + self.destout + self.jumpout
        return self.encoding
#         if len(self.encoding) == 16:
#             return self.encoding
#         else:
#             return False