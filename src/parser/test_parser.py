from parser.parser import parse

# Sample C program to parse
data = '''
int main() {
    int x = 10 + 20;
    return x;
}
'''

# Parse the program
result = parse(data)

# Print the result (parse tree or structure)
print(result)
