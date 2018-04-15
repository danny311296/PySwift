class ASTNode:
	def __init__(self,Type,idNo):
		self.Type = Type
		self.idNo = idNo
		self.operation = None
	def __str__(self):
		output = ('Node ' + str(self.idNo) + '\n' + '\t\t---' + self.Type + '\n\t\t---' + str(self.operation)).split('\n')[0:3]
		return output[0] + '\n' + output[1] + '\n' + output[2] + '\n'
	def addOperation(self,operation):
		self.operation = operation

class ASTAssignmentNode:
	def __init__(self,variable,assignValue):
		self.variable = variable
		self.assignValue = assignValue
	def __str__(self):
		return   self.variable + '     ' + str(self.assignValue)

class ASTExpressionNode:
	def __init__(self,l,r,o):
		self.l = l
		self.o = o
		self.r = r
	def __str__(self):
		return " operation " + self.o  + " on " + str(self.l) + " " + str(self.r)

class ASTFunctionDefinationNode:
	def __init__(self,name,statements):
		self.name = name
		self.statements = statements
	def __str__(self):
		return " function " + self.name  + " \n " + str(self.statements)

class ASTIfSTatement:
	def __init__(self, id, operation, val):
		self.id = id
		self.val = val
		self.operation = operation
	def __str__(self):
		return " if " + self.id + " " + self.operation + " " + self.val
