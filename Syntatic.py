import ply.yacc as yacc
from Lexical import tokens
def p_empty(p):
    'empty :'
    pass
def p_programa(p):
    'programa : program ID DOTCOMMA corpo'

def p_corpo(p):
    'corpo : declara rotina begin sentencas end'

def p_declara(p):
    '''
    declara : var dvar maisdc
            | empty
    '''
def p_maisdc(p):
    'maisdc : DOTCOMMA contadc'

def p_contadc(p):
    '''
    contadc : dvar maisdc
            | empty
    '''

def p_dvar(p):
    'dvar : variaveis : tipovar'
