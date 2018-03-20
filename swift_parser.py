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
				| declaration_statement'''

def p_assignment_statement(p):
	'assignment_statement : ID WHITESPACE EQ WHITESPACE NUMBER'
	if(symbol_table[p[1]]==None):
		print('Variable Not initialized')
	else:
		symbol_table[p[1]] = p[5]
	

def p_declaration_statement(p):
	'''declaration_statement : VAR WHITESPACE ID COL WHITESPACE TYPE 
							| VAR WHITESPACE ID COL WHITESPACE TYPE WHITESPACE EQ WHITESPACE NUMBER
							| VAR WHITESPACE ID WHITESPACE EQ WHITESPACE NUMBER '''
	if(len(p)==7):
		symbol_table[p[3]] = 'unintialized'
	elif(len(p)==11):
		symbol_table[p[3]] = p[10]
	else:
		symbol_table[p[3]] = p[7]
	print(symbol_table)


parser = yacc.yacc()

while(1):
	s = input() + '\n'
	parser.parse(s)
