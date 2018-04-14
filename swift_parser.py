import ply.yacc as yacc
import random
from ast import *

from swift_lexer import tokens
from collections import defaultdict

symbol_table = defaultdict(lambda: None)
astFile = open('swift.ast','w')

def uniqueid():
    seed = random.getrandbits(32)
    while True:
       yield seed
       seed += 1

unique_sequence = uniqueid()

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
	if(symbol_table[p[1]] != None):
		symbol_table[p[1]]["value"] = p[5]
	else:
		print("Error: Variable not declared")
	

def p_declaration_statement(p):
	'''declaration_statement : VAR WHITESPACE ID COL WHITESPACE TYPE 
							| VAR WHITESPACE ID COL WHITESPACE TYPE WHITESPACE EQ WHITESPACE NUMBER
							| VAR WHITESPACE ID WHITESPACE EQ WHITESPACE expression '''
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
		node = ASTNode("assign")
		assignNode = ASTAssignmentNode(p[3],p[7],next(unique_sequence))
		node.addOperation(assignNode)
		print(node,file=astFile)
	print(symbol_table)

def p_expression(p):
	'''expression : expression PLUS expression
				| expression MINUS expression
				| expression TIMES expression
				| expression DIVIDE expression
				| NUMBER 
				| ID
				'''
	if(len(p)==4):
		if(p[2] == '+'):
			node = ASTNode("expression")
			exprNode = ASTExpressionNode(p[1],p[3],p[2],next(unique_sequence))
			node.addOperation(exprNode)
			print(node,file=astFile)
			p[0] = node
		elif(p[2] == '-'):
			p[0] = p[1] - p[3]
		elif(p[2] == '*'):
			p[0] = p[1] * p[3]
		else:
			p[0] = p[1] / p[3]
	else:
		if(isinstance(p[1],str)):
			p[0] = symbol_table[p[1]]["value"]
		else:
			p[0] = p[1]
	

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


f = open('test2.swift','r')
parser.parse(f.read())
