import ply.lex as lex

tokens = ['NUMBER','VAR','ID','WHITESPACE','ENTER','EQ']

t_WHITESPACE = r'\ +'
t_ENTER = r'\n'

literals = [ '+' , '-' , '*' , '/' , '(' , ')' , '=']

reserved = { 'var': 'VAR' }

tokens = tokens + list(reserved.values())

def t_EQ(t):
	r'='
	return t

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_ID(t):
	r'[a-z|A-Z][a-z|A-Z|0-9]*'
	t.type = reserved.get(t.value,'ID')
	return t

lexer = lex.lex(debug=1)

if(__name__ == "__main__"):
	lex.runmain()
