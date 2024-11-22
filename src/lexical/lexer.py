import ply.lex as lex

# List of tokens
tokens = [
    'INT',         
    'RETURN',      
    'IDENTIFIER',  
    'NUMBER',      
    'LPAREN',      
    'RPAREN',      
    'LBRACE',      
    'RBRACE',      
    'SEMICOLON',   
    'EQUALS',      
    'PLUS',        
]

# Reserved keywords (like "int" and "return")
reserved = {
    'int': 'INT',
    'return': 'RETURN',
}

# Token rules: Simple patterns for tokens
t_LPAREN = r'\('       
t_RPAREN = r'\)'       
t_LBRACE = r'\{'       
t_RBRACE = r'\}'       
t_SEMICOLON = r';'     
t_EQUALS = r'='        
t_PLUS = r'\+'         

# Rule for identifiers (variable names, function names)
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:    # Checking if it's a keyword like "int" or "return"
        t.type = reserved[t.value]
    return t

# Rule for numbers (integer literals)
def t_NUMBER(t):
    r'\d+'                     
    t.value = int(t.value)     
    return t

# Ignore spaces and tabs
t_ignore = ' \t'

# Rule for newlines (to track line numbers)
def t_newline(t):
    r'\n+'                     # Matches one or more newlines
    t.lexer.lineno += len(t.value)  # Update the line number count

# Error handling (for invalid characters)
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)        

# Build the lexer
lexer = lex.lex()