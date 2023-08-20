NATURAL = 'NUMERO NATURAL'
INTEIRO = 'NUMERO INTEIRO'
REAL = 'NUMERO REAL'
ADIC = 'ADIÇÃO'
SUB = 'SUBTRAÇÃO'
DIV = 'DIVISÃO'
MULT = 'MULTIPLICAÇÃO'
PAREN = 'PARÊNTESES'

def token(input_string):
    tokens = []
    i = 0
    while i < len(input_string):
        char = input_string[i]

        if char.isdigit():
            j = i
            while j < len(input_string) and (input_string[j].isdigit() or input_string[j] == '.'):
                j += 1
            num_str = input_string[i:j]
            if '.' in num_str:
                if num_str.count('.') == 1:
                    tokens.append((REAL, num_str))
                else:
                    raise ValueError("Invalid input value: " + num_str)
            elif num_str == '0':
                tokens.append((NATURAL, num_str))
            else:
                if num_str.startswith('-') and num_str[1:].isdigit():
                    tokens.append((INTEIRO, num_str))
                else:
                    tokens.append((NATURAL, num_str))
            i = j
        else:
            # Handle operators +, -, *, /
            if char in ('+', '-', '*', '/'):
                tokens.append((ADIC if char == '+' else SUB if char == '-' else MULT if char == '*' else DIV, char))
                i += 1
            elif char in ('(', ')'):
                tokens.append((PAREN, char))
                i += 1
            else:
                # Invalid character
                raise ValueError("Invalid character: " + char)

        # Skip whitespace
        while i < len(input_string) and input_string[i].isspace():
            i += 1

    return tokens

# Example input
user_input = input("Por favor, digite uma expressão: ")

# Tokenize the input
tokens = token(user_input)
for token_type, token_value in tokens:
    print(f"{token_type}: {token_value}")