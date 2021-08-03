import ply.lex as lex
# List of token names.   This is always required

reserved = {
'as'        :   'AS',
'break'     :   'BREAK',
'const'     :   'CONST',
'continue'  :   'CONTINUE',
'create'    :   'CREATE',
'dyn'       :   'DYN',
'else'      :   'ELSE',
'enum'      :   'ENUM',
'extern'    :   'EXTERN',
'false'     :   'FALSE',
'fn'        :   'FN',
'for'       :   'FOR',
'if'        :   'IF',
'impl'      :   'IMPL',
'in'        :   'IN',
'let'       :   'LET',
'loop'      :   'LOOP',
'match'     :   'MATCH',
'mod'       :   'MOD',
'move'      :   'MOVE',
'mut'      :   'MUT',
'pub'       :   'PUB',
'ref'       :   'REF',
'return'    :   'RETURN',
'Self'      :   'SELF',
'self'      :   'sELF',
'static'    :   'STATIC',
'trait'     :   'TRAIT',
'true'      :   'TRUE',
'type'      :   'TYPE',
'union'     :   'UNION',
'unsafe'    :   'UNSAFE',
'use'       :   'USE',
'where'     :   'WHERE',
'while'     :   'WHILE',
'abstract'  :   'ABSTRACT',
'become'    :   'BECOME',
'box'       :   'BOX',
'do'        :   'DO',
'final'     :   'FINAL',
'priv'      :   'PRIV',
'try'       :   'TRY',
'typeof'    :   'TYPEOF',
'unsized'   :   'UNSIZED',
'virtual'   :   'VIRTUAL',
'yield'     :   'YIELD'
}
tokens = [
 'COLON',
 'SEMICOLON',
 'LEFTPAREN',
 'RIGHTPAREN',
 'LEFTKEY',
 'RIGHTKEY',
 'LEFTBRACKET',
 'RIGHTBRACKET',
 'ASSIGN',
 'ASSIGN_PLUS',
 'ASSIGN_MINUS',
 'ASSIGN_DIVIDE',
 'ASSIGN_TIMES',
 'ASSIGN_RESDIV',
 'ASSIGN_AND',
 'ASSIGN_OR',
 'ASSIGN_XOR',
 'ASSIGN_LEFTSHIFT',
 'ASSIGN_RIGHTSHIFT',
 'PLUS',
 'MINUS',
 'DIVIDE',
 'TIMES',
 'RESDIV',
 'INT',
 'FLOAT',
 'EQUAL',
 'NOTEQUAL',
 'GREATER',
 'LOWER',
 'GREATEREQUAL',
 'LOWEREQUAL',
 'OR',
 'AND',
 'XOR',
 'ID',
 'DOISPONTOS',
 'SINGLEOR',
 'AMPERSAND',
 'LEFTSHIFT',
 'RIGHTSHIFT',
 'NOT',
 'TIPO'
] + list(reserved.values())

# Regular expression rules for simple tokens
t_COLON = r'\,'
t_SEMICOLON = r'\;'
t_LEFTPAREN = r'\('
t_RIGHTPAREN = r'\)'
t_LEFTKEY = r'\{'
t_RIGHTKEY = r'\}'
t_LEFTBRACKET = r'\['
t_RIGHTBRACKET = r'\]'
t_ASSIGN = r'\='
t_ASSIGN_PLUS = r'\+\='
t_ASSIGN_MINUS = r'\-\='
t_ASSIGN_DIVIDE = r'\/\='
t_ASSIGN_TIMES = r'\*\='
t_ASSIGN_RESDIV = r'\%\='
t_ASSIGN_AND = r'\&\='
t_ASSIGN_OR = r'\|\='
t_ASSIGN_XOR = r'\^\='
t_ASSIGN_LEFTSHIFT = r'\<\<\='
t_ASSIGN_RIGHTSHIFT = r'\>\>\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIVIDE = r'\/'
t_TIMES = r'\*'
t_RESDIV = r'\%'
t_EQUAL = r'\=\='
t_NOTEQUAL = r'\!\='
t_GREATER = r'\>'
t_LOWER = r'\<'
t_GREATEREQUAL = r'\>\='
t_LOWEREQUAL = r'\<\='
t_OR = r'\|\|'
t_AND = r'\&\&'
t_XOR = r'\^'
t_SINGLEOR = r'\|'
t_DOISPONTOS = r'\:'
t_LEFTSHIFT = r'\<\<'
t_RIGHTSHIFT = r'\>\>'
t_NOT = r'\!'
# A regular expression rule with some action code
def t_INT(t):
  r'\d+' 
  t.value = int(t.value)    
  return t

def t_FLOAT(t):
  r'\d+\.\d+'
  t.value = float(t.value)
  return t



def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  t.type = reserved.get(t.value, 'ID')
  return t


# Define a rule so we can track line numbers
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


# Test it out
data = '''
3 + 4 * 10
+ -20 *2
if if if asdasdas
'''

# Give the lexer some input
lexer.input(data)

for tok in lexer:
  print(tok.type, tok.value, tok.lineno, tok.lexpos) 