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
    tokens = []  # Inicializa a lista de tokens vazia
    i = 0        # Inicializa um índice para percorrer a string de entrada
    
    while i < len(input_string):
        char = input_string[i]  # Obtém o caractere atual da string de entrada
        
        if char.isdigit():  # Verifica se o caractere é um dígito
            j = i
            while j < len(input_string) and (input_string[j].isdigit() or input_string[j] == '.'):
                j += 1
            num_str = input_string[i:j]
            if '.' in num_str:
                if num_str.count('.') == 1:
                    tokens.append((REAL, num_str))
                else:
                    raise ValueError("Valor de input inválido. Tente substituir o ',' pelo '.' " + num_str)
            elif num_str == '0':
                tokens.append((NATURAL, num_str))
            else:
                if num_str.startswith('-') and num_str[1:].isdigit():
                    tokens.append((INTEIRO, num_str))
                else:
                    tokens.append((NATURAL, num_str))
            i = j
            
        else:  # Se o caractere não for um dígito
            if char in ('+', '-', '*', '/'):  # Verifica se é um operador
                tokens.append((ADIC if char == '+' else SUB if char == '-' else MULT if char == '*' else DIV, char))
                i += 1
                
            elif char in ('(', ')'):  # Verifica se é um parêntese
                tokens.append((PAREN, char))
                i += 1
                
            else:  # Se o caractere não for um dígito nem um operador nem um parêntese
                raise ValueError("Invalid character: " + char)
                
        while i < len(input_string) and input_string[i].isspace():
            i += 1  # Avança o índice enquanto houver espaços em branco
            
    return tokens  # Retorna a lista de tokens detectados

# Input do usuário
user_input = input("Por favor, digite uma expressão: ")

# Tokenização do input do usuário
tokens = token(user_input)  # Chama a função para obter a lista de tokens
for token_type, token_value in tokens:
    print(f"{token_type}: {token_value}")  # Imprime os tokens e seus valores
