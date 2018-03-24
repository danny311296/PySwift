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
				| function_defination
				| for_loop'''

def p_assignment_statement(p):
	'assignment_statement : ID WHITESPACE EQ WHITESPACE NUMBER'
	if(symbol_table[p[1]] != None):
		symbol_table[p[1]]["value"] = p[5]
	else:
		print("Error: Variable not declared")
	

def p_declaration_statement(p):
	'''declaration_statement : VAR WHITESPACE ID COL WHITESPACE TYPE 
							| VAR WHITESPACE ID COL WHITESPACE TYPE WHITESPACE EQ WHITESPACE NUMBER
							| VAR WHITESPACE ID WHITESPACE EQ WHITESPACE NUMBER '''
	if(symbol_table[p[3]]!=None):
		print('Error: Variable already declared')	
	elif(len(p)==7):
		symbol_table[p[3]] = {}
		symbol_table[p[3]]["type"] = p[6]
		symbol_table[p[3]]["value"] = "uninitialised"
	elif(len(p)==11):
		symbol_table[p[3]] = {}
		symbol_table[p[3]]["type"] = p[6]
		symbol_table[p[3]]["value"] = p[10]
	else:
		symbol_table[p[3]] = {}
		symbol_table[p[3]]["value"] = p[7]
		symbol_table[p[3]]["type"] = "Int"
	#print(symbol_table)

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

def p_for_loop(p):
	'for_loop : FOR WHITESPACE ID WHITESPACE IN WHITESPACE NUMBER TRIPLEDOT NUMBER WHITESPACE LBRACE ENTER statements RBRACE'

parser = yacc.yacc()


f = open('test.swift','r')
parser.parse(f.read())
print("\n\nSymbol Table\n")
print(symbol_table)
parser.parse(ip)
