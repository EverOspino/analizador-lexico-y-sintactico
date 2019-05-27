# -*- encondig: utf-8 -*-

import ply.lex as lex
import os

# lista de tokens
tokens = (

    # Palabras Reservadas
    'PRINT',
    'ELSE',
    'IF',
    'INT',
    'STRING',
    'CHAIN',
    'RETURN',
    'VOID',
    'WHILE',
    'FOR',

    # Symbolos
    #'HASH',
    #'POINT',
    'PLUS',
    'PLUSPLUS',
    'MINUS',
    'MINUSMINUS',
    'TIMES',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'DEQUAL',
    'DISTINT',
    'SEMICOLON',
    'COMMA',
    #'LGREATER',
    #'RGREATER',
    'LPAREN',
    'RPAREN',
    #'LBRACKET',
    #'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'QUOTES',

    #Otros
    'ID',
    'NUMBER',
)


# Reglas de Expresiones Regualres para token de Contexto simple

t_PLUS = r'\+'
t_MINUS = r'-'
t_MINUSMINUS = r'\-\-'
#t_POINT = r'\.'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_LESS = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
#t_LBRACKET = r'\['
#t_RBRACKET = r'\]'
t_LBLOCK = r'{'
t_RBLOCK = r'}'
t_QUOTES = r'\"'


def t_PRINT(t):
    r'mostrar'
    return t


def t_IF(t):
    r'si'
    return t


def t_ELSE(t):
    r'sino'
    return t


def t_INT(t):
    r'entero'
    return t


def t_CHAIN(t):
    r'cadena'
    return t


def t_RETURN(t):
    r'retorna'
    return t


def t_VOID(t):
    r'vacio'
    return t


def t_WHILE(t):
    r'mientras'
    return t


def t_FOR(t):
    r'para'
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#exprecion regular para reconocer los identificadores


def t_ID(t):
    r'\w+(_\d\w)*'
    return t


def t_STRING(t):
#expresion RE para reconocer los String
    r'\"?(\w+ \ *\w*\d* \ *)\"?'
    return t

"""
def t_HASH(t):
    r'\#'
    return t
"""

def t_PLUSPLUS(t):
    r'\+\+'
    return t


def t_LESSEQUAL(t):
    r'<='
    return t


def t_GREATEREQUAL(t):
    r'>='
    return t


def t_DEQUAL(t):
    r'=='
    return t


def t_DISTINT(t):
    r'!='
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'


def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


def t_comments_C99(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1


def t_error(t):
    print (("Error Lexico: " + str(t.value[0])))
    t.lexer.skip(1)


def test(data, lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print (tok)

lexer = lex.lex()

def Analizador_lexico():
    a = '/home/ospino/Descargas/Compiladores/COM/fuente/fibonacci.c'

    if ( os.path.exists(a)):
        f = open(a)
        data = f.read()
        f.close()
        #Build lexer and try on
        lexer.input(data)
        test(data, lexer)
    else:
        print ("El archivo no existe")


# Test
def main(direccion = 'fuente/prueba.txt'):

    # Test  ESTO ES SOLO PARA PROBAR EL FUNCINAMIENTO DE ANIZADOR LEXICO.
    #Cargamos el archivo "c.cpp" que esta en la carpeta ejemplos y lo guardamos
    #la variable data para despues enviarla al analizador lexico para que la
    #descomponga en tokes

    f = open(direccion)
    data = f.read()
    f.close()
    #Build lexer and try on
    lexer.input(data)
    test(data, lexer)

#main()