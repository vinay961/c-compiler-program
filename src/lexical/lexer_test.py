from lexer import lexer

# Sample C-like code
data = """
int main() {
    int x = 10 + 20;
    return x;
}
"""

# Pass the data to the lexer
lexer.input(data)

# Tokenize and print each token
print("Tokens:")
while True:
    token = lexer.token()
    if not token:
        break
    print(token)
