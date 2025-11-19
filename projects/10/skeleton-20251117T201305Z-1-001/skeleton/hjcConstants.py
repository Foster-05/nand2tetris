TK_NONE = 0
TK_KEYWORD = 1
TK_SYMBOL = 2
TK_IDENTIFIER = 3
TK_INT_CONST = 4
TK_STRING_CONST = 5

keywords = ['boolean', 'char', 'class', 'constructor', 'do', 'else', 'false', 'field', 'function', 'if', 'int', 'let', 'method', 'null', 'return', 'static', 'this', 'true', 'var', 'void', 'while']

symbols     = '{}()[].,;+-*/&|<>=~'
numberChars = '0123456789'
numberStart = numberChars
identStart  = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
identChars  = identStart + numberChars
