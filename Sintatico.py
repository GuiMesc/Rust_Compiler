import ply.yacc as yacc
import ply.lex as lex
from Lexico import tokens

def p_start1(p):
    '''start : declaracao_variavel_externa'''

def p_start2(p):
    '''start : declaracao_constante'''

def p_start3(p):
    '''start : declaracao_funcao'''

def p_start4(p):
    '''start : declaracao_variavel_externa start'''

def p_start5(p):
    '''start : declaracao_constante start'''

def p_start6(p):
    '''start : declaracao_funcao start'''

def p_variavel_externa(p):
    '''declaracao_variavel_externa : STATIC ID ASSIGN expressao'''

def p_variavel_externa2(p):
    '''declaracao_variavel_externa : STATIC ID DOISPONTOS TIPO ASSIGN expressao'''

def p_constante(p):
    '''declaracao_constante : CONST ID ASSIGN expressao'''

def p_constante2(p):
    '''declaracao_constante : CONST ID DOISPONTOS TIPO ASSIGN expressao'''

def p_variavel(p):
    '''declaracao_variavel : LET ID ASSIGN expressao'''

def p_variavel2(p):
    '''declaracao_variavel : LET MUT ID ASSIGN expressao'''

def p_variavel3(p):
    '''declaracao_variavel : LET ID DOISPONTOS TIPO ASSIGN expressao'''

def p_variavel4(p):
    '''declaracao_variavel : LET MUT ID DOISPONTOS TIPO ASSIGN expressao'''

def p_expressao(p):
    '''expressao : expressao_com_bloco'''

def p_expressao2(p):
    '''expressao : expressao_sem_bloco'''

def p_expressao_bloco1(p):
    '''expressao_com_bloco : expressao_de_bloco'''

def p_expressao_bloco2(p):
    '''expressao_com_bloco : expressao_de_loop'''

def p_expressao_bloco3(p):
    '''expressao_com_bloco : expressao_de_if'''

def p_expressao_bloc4(p):
    '''expressao_com_bloco : expressao_de_let_if'''

def p_expressao_de_bloco(p):
    '''expressao_de_bloco : LEFTKEY declaracao RIGHTKEY'''

def p_declaracao(p):
    '''declaracao : SEMICOLON'''

#def p_declaracao2(p):
#    '''declaracao : item'''

def p_declaracao3(p):
    '''declaracao : expressao'''

def p_expressao_de_loop1(p):
    '''expressao_de_loop : expressao_loop_infinito'''

def p_expressao_de_loop2(p):
    '''expressao_de_loop : expressao_loop_predicado'''

def p_expressao_de_loop3(p):
    '''expressao_de_loop : expressao_loop_iterador'''

def p_expressao_de_loop4(p):
    '''expressao_loop_infinito : LOOP expressao_de_bloco'''

def p_expressao_de_loop5(p):
    '''expressao_loop_predicado : WHILE expressao_de_bloco'''

def p_expressao_de_loop6(p):
    '''expressao_loop_iterador : FOR ID IN expressao'''

def p_expressao_parada(p):
    '''expressao_parada : BREAK'''

def p_expressao_parada(p):
    '''expressao_continue : CONTINUE'''

def p_expressao_if(p):
    '''expressao_de_if : IF expressao expressao_de_bloco ELSE expressao_de_bloco'''

def p_expressao_if2(p):
    '''expressao_de_if : IF expressao expressao_de_bloco ELSE expressao_de_if'''

def p_expressao_if3(p):
    '''expressao_de_if : IF expressao expressao_de_bloco ELSE expressao_de_let_if'''

def p_expressao_if4(p):
    '''expressao_de_let_if : IF LET ID ASSIGN expressao expressao_de_bloco ELSE expressao_de_bloco'''

def p_expressao_if5(p):
    '''expressao_de_let_if : IF expressao expressao_de_bloco ELSE expressao_de_if'''

def p_expressao_if5(p):
    '''expressao_de_let_if : IF expressao expressao_de_bloco ELSE expressao_de_let_if'''

def p_declaracao_funcao(p):
    '''declaracao_funcao : FN ID LEFTPAREN parametros_da_funcao RIGHTPAREN tipo_de_retorno LEFTPAREN expressao_de_bloco RIGHTPAREN'''

def p_parametros(p):
    '''parametros_da_funcao : ID DOISPONTOS TIPO'''

def p_tipo_retorno(p):
    '''tipo_de_retorno : MINUS GREATER TIPO'''

def p_expressao_sem_bloco1(p):
    '''expressao_sem_bloco : literal_expression'''

def p_expressao_sem_bloco2(p):
    '''
    expressao_sem_bloco : exp
    '''

def p_expressao_sem_bloco3(p):
    '''
    expressao_sem_bloco : group_expression
    '''

def p_expressao_sem_bloco4(p):
    '''
    expressao_sem_bloco : call_expression
    '''
def p_expressao_sem_bloco5(p):
    '''
    expressao_sem_bloco : index_expression
    '''
def p_literal_expression(p):
    '''
    literal_expression : INT
    '''

def p_literal_expression1(p):
    '''
    literal_expression1 : FLOAT
    '''

def p_exp(p):
    '''
    exp : exp1 ASSIGN exp
    '''
    #p[0] = p[1] = p[3]

def p_exp1(p):
    '''
    exp : exp1 ASSIGN_PLUS exp
    '''
    #p[0] = p[1] + p[2]
def p_exp2(p):
    '''
    exp : exp1 ASSIGN_MINUS exp
    '''
def p_exp3(p):
    '''
    exp : exp1 ASSIGN_TIMES exp
    '''
def p_exp4(p):
    '''
    exp : exp1 ASSIGN_DIVIDE exp
    '''
def p_exp5(p):
    '''
    exp : exp1 ASSIGN_RESDIV exp
    '''
def p_exp6(p):
    '''
    exp : exp1 ASSIGN_AND exp
    '''
def p_exp7(p):
    '''
    exp : exp1 ASSIGN_OR exp
    '''
def p_exp8(p):
    '''
    exp : exp1 ASSIGN_XOR exp
    '''
def p_exp9(p):
    '''
    exp : exp1 ASSIGN_LEFTSHIFT exp
    '''
def p_exp10(p):
    '''
    exp : exp1 ASSIGN_RIGHTSHIFT exp
    '''
def p_exp11(p):
    '''
    exp : exp1
    '''
def p_exp12(p):
    '''
    exp1 : exp1 OR exp2
    '''
   # p[0] = p[1] | p[2]
def p_exp13(p):
    '''
    exp1 : exp2
    '''
def p_exp14(p):
    '''
    exp2 : exp2 AND exp3
    '''
   # p[0] = p[1] and p[2]
def p_exp15(p):
    '''
    exp2 : exp3 
    '''
def p_exp16(p):
    '''
    exp3 : exp3 EQUAL exp4
    '''
   # p[0] = p[1] == p[2]
def p_exp17(p):
    '''
    exp3 : exp3 NOTEQUAL exp4
    '''
   # p[0] = p[1] != p[2]
def p_exp18(p):
    '''
    exp3 : exp3 LOWER exp4
    '''
   # p[0] = p[1] < p[2]
def p_exp19(p):
    '''
    exp3 : exp3 GREATER exp4
    '''
   # p[0] = p[1] > p[2]
def p_exp20(p):
    '''
    exp3 : exp3 LOWEREQUAL exp4
    '''
   # p[0] = p[1] <= p[2]
def p_exp21(p):
    '''
    exp3 : exp3 GREATEREQUAL exp4
    '''
   # p[0] = p[1] >= p[2]
def p_exp22(p):
    '''
    exp3 : exp4
    '''

def p_exp23(p):
    '''
    exp4 : exp4 SINGLEOR exp5
    '''

def p_exp24(p):
    '''
    exp4 : exp5 
    '''
def p_exp25(p):
    '''
    exp5 : exp5 XOR exp6
    '''
   # p[0] = p[1] ^ p[2]
def p_exp26(p):
    '''
    exp5 : exp6
    '''
def p_exp27(p):
    '''
    exp6 : exp6 AMPERSAND exp7
    '''

def p_exp28(p):
    '''
    exp6 : exp7
    '''
def p_exp29(p):
    '''
    exp7 : exp7 LEFTSHIFT exp8
    '''
def p_exp30(p):
    '''
    exp7 : exp7 RIGHTSHIFT exp8
    '''
def p_exp31(p):
    '''
    exp7 : exp8
    '''
def p_exp32(p):
    '''
    exp8 : exp8 PLUS exp9
    '''
def p_exp33(p):
    '''
    exp8 : exp8 MINUS exp9
    '''
def p_exp34(p):
    '''
    exp8 : exp9
    '''
def p_exp35(p):
    '''
    exp9 : exp9 TIMES exp10
    '''
def p_exp36(p):
    '''
    exp9 : exp9 DIVIDE exp10
    '''
def p_exp37(p):
    '''
    exp9 : exp9 RESDIV exp10
    '''
def p_exp38(p):
    '''
    exp9 : exp10
    '''
def p_exp39(p):
    '''
    exp10 : MINUS exp10 
    '''
def p_exp40(p):
    '''
    exp10 : NOT exp10 
    '''

def p_exp40(p):
    '''
    exp10 : expressao_sem_bloco
    '''
def p_group_expression(p):
    '''
    group_expression : LEFTPAREN expressao RIGHTPAREN
    '''

def p_call_expression(p):
    '''
    call_expression : expressao LEFTPAREN call_params RIGHTPAREN
    '''

def p_call_params(p):  
    '''
    call_params : expressao LEFTPAREN expressao RIGHTPAREN
    '''

def p_index_expression(p):
    '''
    index_expression : expressao LEFTBRACKET expressao RIGHTBRACKET
    '''

parser = yacc.yacc()

while True:
    try:
        s = input()
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)