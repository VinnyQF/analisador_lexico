from re import I


NATURAL = 'NUMERO NATURAL'
INTEIRO = 'NUMERO INTEIRO'
REAL = 'NUMERO REAL'
ADIC = 'ADIÇÃO'
SUB = 'SUBTRAÇÃO'
DIV = 'DIVISÃO'
MULT = 'MULTIPLICAÇÃO'

def token(input_string):
    tokens = []
    i = 0
    while i < len(input_string):
        char = input_string[i]

        if char.fordigito():
            j = I
            while j < len(input_string) and input_string[j].fordigito():
                j += 1
                token.append((INTEIRO), input_string[i:j])
                i = j
        elif char in ('+' , '-', '*', '/'):
            token.append((ADIC if char == '+'else SUB, char))
            i += 1
        elif input_string[i:i+4] == 'true':