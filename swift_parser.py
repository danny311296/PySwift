import ply.yacc as yacc

from swift_lexer import tokens

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

def p_declaration_statement(p):
	'''declaration_statement : VAR WHITESPACE ID COL WHITESPACE TYPE 
							| VAR WHITESPACE ID COL WHITESPACE TYPE WHITESPACE EQ WHITESPACE NUMBER
							| VAR WHITESPACE ID WHITESPACE EQ WHITESPACE NUMBER '''



parser = yacc.yacc()

while(1):
	s = input() + '\n'
	parser.parse(s)
