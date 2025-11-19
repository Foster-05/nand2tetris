"""
hjc.py -- Hack computer Jack compiler
"""

import sys
import os
import hjcTokenizer
import hjcConstants as CONSTS
import hjcTokenWriter
#import hjcCompilationEngine


def ProcessT(sourceFileName, outputFileName):
    print('Processing', sourceFileName)

    # xml tokenizer test output
    outputFileName = outputFileName.replace('.vm', 'T.xml')
    tokWriter = hjcTokenWriter.TokenWriter(outputFileName, 'tokens')

    tokenizer = hjcTokenizer.Tokenizer(sourceFileName)
    while tokenizer.Advance():
        printToken(tokenizer, outputFile)
    tokenizer.close()
    tokWriter.Close()

def printToken(tokenizer, tokWriter):
    """This function interacts with the tokenizer class.
    It checks the type of token, and then prints the output
    through the tokWriter class."""
    txt = ""
    if tokenizer.tokenType == CONSTS.TK_IDENTIFIER:
        txt = tokenizer.identifier
        tokWriter.WriteXml('identifier', txt)
    elif tokenizer.tokenType == CONSTS.TK_INT_CONST:
        txt = str(tokenizer.intval)
        tokWriter.WriteXml('integerConstant', txt)
    elif tokenizer.tokenType == CONSTS.TK_KEYWORD:
        txt = tokenizer.Keyword
        tokWriter.WriteXml('keyword', txt)
    elif tokenizer.tokenType == CONSTS.TK_STRING_CONST:
        txt = tokenizer.stringval
        tokWriter.WriteXml('stringConstant', txt)
    elif tokenizer.tokenType == CONSTS.TK_SYMBOL:
        txt = tokenizer.Symbol
        tokWriter.WriteXml('symbol', txt)
    else:
        txt = "ERROR! ERROR! ERROR!"

def Process(sourceFileName, outputFileName):
    print('Processing', sourceFileName)

    # xml tokenizer test output
    outputFileName = outputFileName.replace('.vm', '.xml')
    tokWriter = hjcTokenWriter.TokenWriter(outputFileName)
    tokenizer = hjcTokenizer.Tokenizer(sourceFileName)

    # begin compiling class###################################################
    print("YOU need to implement CompilationEngine class!")
    #compEngine = hjcCompilationEngine.CompilationEngine(tokenizer, tokWriter)
    #compEngine.compileClass()

    tokenizer.close()
    tokWriter.close()


def ProgramUsage():
    """######################################################################
    usage: JackAnalyzer sourceFile.jack
    sourceFile may be a directory in which case all .jack files
    in the directory will be processed to .vm files
    """
    sys.exit(-1)
    

def main():
    # Check number of arguments
    if len(sys.argv) != 2:
        ProgramUsage()
        
    sourceName = sys.argv[1]
    # check if is a JACK file
    if os.path.splitext(sourceName)[1].lower() == os.path.extsep + 'jack':
          # it is a single jack file, so process it
          outName = os.path.splitext(sourceName)[0] + os.path.extsep + 'vm'
          ProcessT(sourceName, outName)
          Process(sourceName, outName)
    elif os.path.isdir(sourceName):
        dirName = sourceName
        # process each .jack file in the directory
        print('Processing directory', dirName)
        if dirName[-1] == os.path.sep:
            dirName = dirName[:-1]
        for AFile in os.listdir(dirName):
            # check if ends in .jack
            if os.path.splitext(AFile)[1].lower() == os.path.extsep + 'jack':
                outName = os.path.splitext(AFile)[0] + os.path.extsep + 'vm'
                outName = dirName + os.path.sep + outName
                sourceName = dirName + os.path.sep + AFile
                ProcessT(sourceName, outName)
                Process(sourceName, outName)
    else:
        dirName = '.'

        # process single .jack file
        outName = os.path.splitext(sourceName)[0] + os.path.extsep + 'vm'
        outName = dirName + os.path.sep + outName
        ProcessT(sourceName, outName)
        Process(sourceName, outName)


# Run main code
main()
# Process('ExpressionLessSquare/Main.jack', 'ExpressionLessSquare/Main.vm')
