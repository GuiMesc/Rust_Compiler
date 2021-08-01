<<<<<<< HEAD
import ply.yacc as yacc
import ply.lex as lex
from Lexico import tokens

def p_start1(p):
    '''
    start: declaracao_variavel_externa
    
    '''

parser = yacc.yacc()

while True:
    try:
        s = input()
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
=======
import ply.yacc as yacc
import ply.lex as lex
from Lexico import tokens

def p_start1(p):
    '''
    start: declaracao_variavel_externa
    
    '''

parser = yacc.yacc()

while True:
    try:
        s = input()
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
>>>>>>> 2a6bab10b95896c458e84d81727aa7ad2511931e
    print(result)