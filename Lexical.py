import ply.lex as lex
reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'begin':'BEGIN',
    'end':'END',
    'program':'PROGRAM',
    'pilha_of_integer':'PILHAINTEGER',
    'pilha_of_real':'PILHAREAL',
    'var':'VAR',
    'function':'FUNCTION',
    'read':'READ',
    'write':'WRITE',
    'concatena':'CONCATENA',
    'inverte':'INVERTE',
    'integer':'INTEGER',
    'real':'REAL',
    'for':'FOR',
    'to':'TO',
    'do':'DO',
    'repeat':'REPEAT',
    'until':'UNTIL',
    'input':'INPUT',
    'output':'OUTPUT',
    'length':'LENGTH'
}
tokens = [
    'ID',
    'NUMBER',
    'RNUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'DIVIDER',
    'LPAREN',
    'RPAREN',
    'GREAT',
    'LESS',
    'GREATEQ',
    'LESSEQ',
    'EQUALS',
    'DIFFERENT',
    'ATTR',
    'COMMA',
    'DOTCOMMA',
    'DOT',
    'TWODOT',
    'HASHTAG'
]

tokens = tokens + list(reserved.values())

t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'//'
t_DIVIDER = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_GREAT = r'>'
t_LESS = r'<'
t_GREATEQ = r'>='
t_LESSEQ = r'<='
t_EQUALS = r'='
t_DIFFERENT = r'<>'
t_ATTR = r':='
t_COMMA = r','
t_DOTCOMMA = r';'
t_DOT = r'\.'
t_TWODOT = r':'
t_HASHTAG = r'\#'

errors =[]

def t_RNUMBER(t):
    r'[0-9]+\.?[0-9]+'
    t.value = float(t.value)
    return t
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    errors.append(f'({t.value[0]},lin: {t.lineno})')
    t.lexer.skip(1)

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

lexer = lex.lex()

file = open('test.txt','r')
data = file.read()
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(f'({tok.type}, {tok.value}) lin: {tok.lineno}')
if errors:
    print(f'Erros léxicos:{errors}')