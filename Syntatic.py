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

def p_tipovar(p):
    '''
    tipovar : integer
            | real
            | pilha_of_integer
            | pilha_of_real
    '''
def p_variaveis(p):
    'variaveis : ID maisvar'
def p_maisvar(p):
    '''
    maisvar : COMMA maisvar
            | empty
    '''
def p_rotina(p):
    '''
    rotina : procedimento
           | funcao
           | empty
    '''
def p_procedimento(p):
    'procedimento : procedure ID parametros DOTCOMMA corpo DOTCOMMA rotina'
def p_funcao(p):
    'funcao : function ID parametros TWODOT tipofuncao DOTCOMMA corpo DOTCOMMA rotina'
def p_parametros(p):
    '''
    parametros : LPAREN listaparametros RPAREN
               | empty
    '''
def p_listaparmetros(p):
    'listaparametros : listaid TWODOT tipovar contlistapar'
def p_contlistapar(p):
    '''contlistapar : DOTCOMMA listaparametros
                    | empty
    '''
def p_tipofuncao(p):
    '''
    tipofuncao : integer
               | real
               | pilha_of_real
               | pilha_of_integer
    '''
def p_sentencas(p):
    'sentencas : comando maissentencas'
def p_maissentencas(p):
    'maissentencas : DOTCOMMA contsentencas'
def p_contsentencas(p):
    '''
    contsentencas : sentencas
                  | empty
    '''
def p_varread(p):
    'varread : ID maisvarread'
def p_maisvarread(p):
    '''
    maisvarread : COMMA varread
                | empty
    '''
def p_varwrite(p):
    'varwrite : ID maisvarwrite'
def p_maisvarwrite(p):
    '''
    maisvarwrite : COMMA varwrite
                 | empty
    '''
def p_comando(p):
    '''
    comando : read LPAREN varread RPAREN
            | if LPAREN condicao RPAREN then begin sentencas end pfalsa
            | for ID ATTR expressao to expressao do begin sentencas end
            | atribuicao
            | write LPAREN varwrite RPAREN
            | while LPAREN condicao RPAREN do begin sentencas end
            | repeat sentencas until LPAREN condicao RPAREN
            | chamadaprocedimento
    '''
def p_atribuicao(p):
    'atribuicao : ID ATTR expressao'
    p[0] = p[3]
def p_chamadaprocedimento(p):
    'chamadaprocedimento : ID argumentos'
def p_argumentos(p):
    '''
    argumentos : LPAREN listaarg RPAREN
               | empty
    '''
def p_listaarg(p):
    'listaarg : expressao contlistaarg'
def p_contlistaarg(p):
    '''
    contlistaarg : COMMA listaarg
                 | empty
    '''
def p_condicao(p):
    '''
    condicao :  relacao LPAREN expressaonum COMMA expressaonum RPAREN
             | relacao LPAREN expressaopilha COMAA expressaopilha RPAREN
    '''
def p_pfalsa(p):
    '''
    pfalsa : else begin sentencas end
           | empty
    '''
def p_relacao(p):
    '''
    relacao : EQUALS
            | GREAT
            | LESS
            | GREATEQ
            | LESSEQ
            | DIFFERENT
    '''
def p_expressao(p):
    '''
    expressao : expressaonum
              | expressaopilha
    '''
def p_expressaonum(p):
    '''
    expressaonum : termo
                 | ID argumentos
    '''
def p_operando(p):
    '''
    operando : ID
             | integernum
             | realnum
             | operador LPAREN operando COMMA operando RPAREN
             | PLUS
             | MINUS
             | TIMES
             | DIVIDE
             | DIVIDER
    '''