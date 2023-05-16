import ply.yacc as yacc
from Lexical import tokens, data, line
import pandas as pd
SymbolTable = {}
FuncScope = False
def p_programa(p):
    'programa : PROGRAM ID DOTCOMMA corpo'

def p_corpo(p):
    'corpo : declara rotina BEGIN sentencas END'
def p_empty(p):
    'empty :'
    pass

def p_declara(p):
    '''
    declara : VAR dvar maisdc
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
    'dvar : variaveis TYPE tipovar'

type_list = []
def p_tipovar(p):
    '''
    tipovar : INTEGER
            | REAL
            | PILHAINTEGER
            | PILHAREAL
    '''
    type_list.append(p[1])
    print(p[1])

varlist = []
def p_variaveis(p):
    'variaveis : ID maisvar'
    SymbolTable[p[1]] = {'Tipo': p_tipovar(p)}
    varlist.append((p[1],p.lineno))
    return p[1]
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
    'procedimento : PROCEDURE ID parametros DOTCOMMA corpo DOTCOMMA rotina'

funcList = []
def p_funcao(p):
    'funcao : FUNCTION ID parametros TWODOT tipofuncao DOTCOMMA corpo DOTCOMMA rotina'
    #type_list.append(p[2])
    lin = p.lineno(2)
    funcList.append((p[2],lin))
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

def p_listaid(p):
    'listaid : ID contlistaid'
    SymbolTable[p[1]] = {'Tipo': p_tipovar(p)}
    lin = p.lineno(1)
    varlist.append((p[1],lin))


def p_contlistaid(p):
    '''
    contlistaid : DOTCOMMA listaparametros
                | empty
    '''

funcTypeList = []
def p_tipofuncao(p):
    '''
    tipofuncao : INTEGER
               | REAL
               | PILHAINTEGER
               | PILHAREAL
    '''
    funcTypeList.append((p[1]))

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
    comando : READ LPAREN varread RPAREN
            | IF LPAREN condicao RPAREN THEN BEGIN sentencas END pfalsa
            | FOR ID ATTR expressao TO expressao DO BEGIN sentencas END
            | atribuicao
            | WRITE LPAREN varwrite RPAREN
            | WHILE LPAREN condicao RPAREN DO BEGIN sentencas END
            | REPEAT sentencas UNTIL LPAREN condicao RPAREN
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
             | relacao LPAREN expressaopilha COMMA expressaopilha RPAREN
    '''

def p_pfalsa(p):
    '''
    pfalsa : ELSE BEGIN sentencas END
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
    '''

def p_operador(p):
    '''
    operador : PLUS
             | MINUS
             | TIMES
             | DIVIDE
             | DIVIDER
    '''

def p_termo(p):
    '''
    termo : operador LPAREN operando COMMA operando RPAREN
          | ID
          | integernum
          | realnum
    '''

def p_expressaopilha(p):
    '''
    expressaopilha : oppilha LPAREN conteudo RPAREN
                   | CONCATENA LPAREN conteudo COMMA conteudo RPAREN
                   | INVERTE LPAREN conteudo RPAREN
    '''

def p_conteudo(p):
    '''
    conteudo : HASHTAG HASHTAG
             | HASHTAG integernum integernumcont HASHTAG
             | HASHTAG realnum realnumcont HASHTAG
    '''

def p_integernumcont(p):
    '''
    integernumcont : COMMA integernum integernumcont
                   | empty
    '''

def p_realnumcont(p):
    '''
    realnumcont : COMMA realnum realnumcont
                | empty
    '''

def p_oppilha(p):
    '''
    oppilha : INPUT
            | OUTPUT
            | LENGTH
    '''

def p_integernum(p):
    'integernum : NUMBER'

def p_realnum(p):
    'realnum : RNUMBER'

def p_error(p):
    if p:
        print(f'Syntax error at token {p.type} line {p.lineno - line + 1}')
        # Just discard the token and tell the parser it's okay.
        parser.errok()
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
result = parser.parse(data,tracking=True)
print(varlist[0][1])
for i in range(0,len(type_list),2):
    SymbolTable[type_list[i]]['Tipo'] = type_list[i + 1]
for nome,tipo in zip(funcList, funcTypeList):
    SymbolTable[nome[0]] = {'Tipo':tipo}
for element in SymbolTable:
    if SymbolTable[element]['Tipo'] == 'integer':
        SymbolTable[element]['Valor'] = '0'
    if SymbolTable[element]['Tipo'] == 'real':
        SymbolTable[element]['Valor'] = '0.0'
    if SymbolTable[element]['Tipo'] == 'pilha_of_integer':
        SymbolTable[element]['Valor'] = '##' 
    if SymbolTable[element]['Tipo'] == 'pilha_of_real':
        SymbolTable[element]['Valor'] = '##' 

nome_variavel = []
tipo = []
valor =  []
escopo = []
for element in SymbolTable:
    nome_variavel.append(element)
    valor.append(SymbolTable[element]["Valor"])
    tipo.append(SymbolTable[element]["Tipo"])
    escopo.append("Global")

dados = {"ID": nome_variavel,'Tipo': tipo, "Valor": valor, "Escopo": escopo}
dataframe = pd.DataFrame(dados)
dataframe.to_markdown("Tabelas/Tabela Sintática.md")
print(dataframe.to_markdown())
