import ply.yacc as yacc

from swift_lexer import tokens

def p_assignment_statement(p):
	'assignment_statement : VAR WHITESPACE ID WHITESPACE EQ WHITESPACE NUMBER'

parser = yacc.yacc()

while(1):
	s = input()
	parser.parse(s)
