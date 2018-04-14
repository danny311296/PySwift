class ASTNode:
	def __init__(self,Type):
		self.Type = Type
		self.operation = None
	def __str__(self):
		return 'Node ' + self.Type + ' ' + str(self.operation)
	def addOperation(self,operation):
		self.operation = operation

class ASTAssignmentNode:
	def __init__(self,variable,assignValue):
		self.variable = variable
		self.assignValue = assignValue
	def __str__(self):
		return self.variable + '     ' + str(self.assignValue)

class ASTExpressionNode:
	def __init__(self,l,r,o):
		self.l = l
		self.o = o
		self.r = r
	def __str__(self):
		return "operation " + self.o  + " on " + str(self.l) + " " + str(self.r) 
