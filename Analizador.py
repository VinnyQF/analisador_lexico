# Declaração dos tokens
NATURAL = 'NUMERO NATURAL'
INTEIRO = 'NUMERO INTEIRO'
REAL = 'NUMERO REAL'
ADIC = 'ADIÇÃO'
SUB = 'SUBTRAÇÃO'
DIV = 'DIVISÃO'
MULT = 'MULTIPLICAÇÃO'
PAREN = 'PARÊNTESES'

# Função que detecta os tokens e os transforma em string
def token(input_string):
    tokens = []
    i = 0
    while i < len(input_string):
        char = input_string[i]
        # Detecta se o character especial é um dos tipos de dígito
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
            # Verifica se o caracter especial é um dos tipos de modificador
            if char in ('+', '-', '*', '/'):
                tokens.append((ADIC if char == '+' else SUB if char == '-' else MULT if char == '*' else DIV, char))
                i += 1
            elif char in ('(', ')'):
                tokens.append((PAREN, char))
                i += 1
            else:
                # Mensagem de erro para caracteres inválidos
                raise ValueError("Invalid character: " + char)

        # Pular espaço vazio
        while i < len(input_string) and input_string[i].isspace():
            i += 1

    return tokens

# Input do usuário
user_input = input("Por favor, digite uma expressão: ")

# Tokenização do input do usuário
tokens = token(user_input)
for token_type, token_value in tokens:
    print(f"{token_type}: {token_value}")