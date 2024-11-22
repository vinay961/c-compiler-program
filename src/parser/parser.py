import ply.yacc as yacc
from lexical.lexer import tokens  

# Grammar rules (productions)

# Rule for the program structure
def p_program(p):
    '''program : declaration_list'''
    # A program is a list of declarations
    p[0] = p[1]

# Rule for handling a list of declarations
def p_declaration_list(p):
    '''declaration_list : declaration
                        | declaration_list declaration'''
    if len(p) == 2:
        # Single declaration
        p[0] = [p[1]]
    else:
        # Multiple declarations (combine lists)
        p[0] = p[1] + [p[2]]

# Rule for handling a single declaration
def p_declaration(p):
    '''declaration : type IDENTIFIER LPAREN RPAREN LBRACE declaration_list RBRACE'''
    # A declaration is a function with:
    # - A type (e.g., int)
    # - An identifier (function name)
    # - A block of declarations inside {}
    p[0] = ('function', p[2], p[1], p[6])

# Rule for handling the type of a declaration
def p_type(p):
    '''type : INT'''
    # The type is `int`
    p[0] = p[1]

# Error handling rule
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at end of input")

# Build the parser
parser = yacc.yacc()

# Parse function
def parse(data):
    return parser.parse(data)
