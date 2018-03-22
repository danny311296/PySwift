import ply.yacc as yacc

from swift_lexer import tokens
from collections import defaultdict

symbol_table = defaultdict(lambda: None)

def p_start(p):
	'''start : statements 
			| empty'''

def p_empty(p):
	'empty :'
	pass

def p_statements(p):
	'statements : statement ENTER next_statement'

def p_next_statement(p):
	'''next_statement : statement ENTER next_statement 
					| empty''' 

def p_statement(p):
	'''statement : assignment_statement 
				| declaration_statement
				| function_defination'''

def p_assignment_statement(p):
	'assignment_statement : ID WHITESPACE EQ WHITESPACE NUMBER'
	symbol_table[p[1]] = p[5]
	

def p_declaration_statement(p):
	'''declaration_statement : VAR WHITESPACE ID COL WHITESPACE TYPE 
							| VAR WHITESPACE ID COL WHITESPACE TYPE WHITESPACE EQ WHITESPACE NUMBER
							| VAR WHITESPACE ID WHITESPACE EQ WHITESPACE NUMBER '''
	if(symbol_table[p[3]]!=None):
		print('Error: Variable already declared')	
	elif(len(p)==7):
		symbol_table[p[3]] = 'unintialized'
	elif(len(p)==11):
		symbol_table[p[3]] = p[10]
	else:
		symbol_table[p[3]] = p[7]
	print(symbol_table)

def p_function_defination(p):
	'function_defination : FUNC WHITESPACE ID LPAREN optional_parameters RPAREN WHITESPACE optional_return_type WHITESPACE LBRACE ENTER statements RBRACE'

def p_optional_parameters(p):
	'''optional_parameters : has_parameter
						| empty'''

def p_has_parameter(p):
	'''has_parameter : has_parameter COMMA has_parameter
						| ID COL WHITESPACE TYPE'''

def p_optional_return_type(p):
	'optional_return_type : ARROW WHITESPACE TYPE'

parser = yacc.yacc()


f = open('test.swift','r')
#print(f.read())
parser.parse(f.read())
