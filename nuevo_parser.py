# -*- enconding: utf-8 -*-
#!/usr/bin/python
import ply.yacc as yacc
import os
from nuevo_lexer import tokens
import sys


VERBOSE = 1



def p_declaration(p):
    '''declaration : var_declaration
    | fun_declaration'''
    pass


def p_var_declaration_1(p):
    '''var_declaration : type_specifier ID SEMICOLON
    | type_specifier var_declaration_list SEMICOLON
    '''
    pass


def p_var_declaration_list_1(p):
    'var_declaration_list : var_declaration_list COMMA var EQUAL operation_expression'
    pass


def p_var_declaration_list_2(p):
    'var_declaration_list : var EQUAL operation_expression'
    pass


def p_fun_declaration_1(p):
    'fun_declaration : type_specifier ID LPAREN params RPAREN compount_stmt'
    pass


def p_type_specifier_1(p):
    'type_specifier : INT'
    pass


def p_type_specifier_2(p):
    'type_specifier : VOID'
    pass


def p_type_specifier_3(p):
    'type_specifier : CHAIN'
    pass


def p_params_1(p):
    'params : param_list'
    pass


def p_param_list_1(p):
    'param_list : param COMMA param_list'
    pass


def p_param_list_2(p):
    'param_list : param'
    pass


def p_param_list_3(p):
    'param_list : empty'
    pass


def p_param_1(p):
    'param : type_specifier ID'
    pass


def p_compount_stmt(p):
    'compount_stmt : LBLOCK local_declarations statement_list RBLOCK'
    pass


def p_local_declarations_1(p):
    'local_declarations : local_declarations var_declaration'
    pass


def p_local_declarations_2(p):
    'local_declarations : empty'
    pass


def p_statement_list_1(p):
    'statement_list : statement_list statement'
    pass


def p_statement_list_2(p):
    'statement_list : empty'
    pass


def p_statement(p):
    '''statement : expression_stmt
            | compount_stmt
            | selection_stmt
            | iteration_stmt
            | return_stmt
    '''
    pass


def p_expression_stmt_1(p):
    '''expression_stmt : expression SEMICOLON'''
    pass


def p_expression_stmt_2(p):
    'expression_stmt : SEMICOLON'
    pass


def p_expression_stmt_3(p):
    '''expression_stmt : PRINT LPAREN var RPAREN SEMICOLON
    | PRINT LPAREN QUOTES STRING QUOTES RPAREN SEMICOLON
    '''
    pass



def p_expression_stmt_4(p):
    '''expression_stmt : ID PLUSPLUS
    | PLUSPLUS ID
    | ID MINUSMINUS
    | MINUSMINUS ID
    '''
    pass


def p_selection_stmt_1(p):
    'selection_stmt : IF LPAREN expression RPAREN statement'
    pass


def p_selection_stmt_2(p):
    'selection_stmt : IF LPAREN expression RPAREN statement ELSE statement'
    pass


def p_iteration_stmt(p):
    'iteration_stmt : WHILE LPAREN expression RPAREN statement'
    pass


def p_iteration_stmt1(p):
    '''iteration_stmt :
| FOR LPAREN var SEMICOLON expression SEMICOLON expression RPAREN statement
| FOR LPAREN var SEMICOLON expression SEMICOLON var PLUSPLUS RPAREN statement
| FOR LPAREN var SEMICOLON expression SEMICOLON PLUSPLUS var  RPAREN statement
| FOR LPAREN var SEMICOLON expression SEMICOLON var MINUSMINUS RPAREN statement
| FOR LPAREN var SEMICOLON expression SEMICOLON MINUSMINUS var  RPAREN statement
    '''
    pass


def p_return_stmt_1(p):
    'return_stmt : RETURN SEMICOLON'
    pass


def p_return_stmt_2(p):
    'return_stmt : RETURN expression SEMICOLON'
    pass


def p_expression_1(p):
    '''expression : var EQUAL expression'''
    pass


def p_expression_2(p):
    'expression : simple_expression'
    pass


def p_var(p):
    'var : ID'
    pass

def p_simple_expression_1(p):
    'simple_expression : operation_expression relop operation_expression'
    pass


def p_simple_expression_2(p):
    'simple_expression : operation_expression'
    pass


def p_relop(p):
    '''relop : LESS
        | LESSEQUAL
        | GREATER
        | GREATEREQUAL
        | DEQUAL
        | DISTINT
        | QUOTES
    '''
    pass


def p_operation_expression_1(p):
    'operation_expression : factor simb_op operation_expression '
    pass


def p_operation_expression_2(p):
    'operation_expression : factor'
    pass


def p_simb_op_1(p):
    'simb_op : addop'
    pass


def p_simb_op_2(p):
    'simb_op : mulop'
    pass


def p_addop(p):
    '''addop : PLUS
    | MINUS
    '''
    pass


def p_mulop(p):
    '''mulop : TIMES
    | DIVIDE
    '''
    pass


def p_factor_1(p):
    'factor : LPAREN expression RPAREN'
    pass


def p_factor_2(p):
    'factor : var'
    pass


def p_factor_3(p):
    'factor : call'
    pass


def p_factor_4(p):
    'factor : NUMBER'
    pass


def p_call(p):
    'call : ID LPAREN args RPAREN'
    pass


def p_args(p):
    '''args : args_list
            | empty
    '''
    pass


def p_args_list_1(p):
    'args_list : expression COMMA args_list '
    pass


def p_args_list_2(p):
    'args_list : expression'
    pass


def p_empty(p):
    'empty :'
    pass


def sintax(t):
    os.system("g++ -Wall "+t)
    pass


def p_error(p):
    #print str(dir(p))
    #print str(dir(c_lexer))
    if VERBOSE:
        if p is not None:
            print "Error de Sintaxis"
        else:
            print "Error de Lexico"
    else:
        raise Exception('Syntax', 'error')


parser = yacc.yacc()
def ejecutar_parser(data):
    
    parser.parse(data)
"""
ejecutar_parser('test/prueba1.alv')
if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'test/prueba1.alv'

    f = open(fin,'r')
    data = f.read()
"""