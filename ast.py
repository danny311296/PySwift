class ASTNode:
	def __init__(self,Type):
		self.Type = Type
		self.operation = None
	def __str__(self):
		return 'Node \n' + '\t\t---' + self.Type + '\n\t\t---' + str(self.operation)
	def addOperation(self,operation):
		self.operation = operation

class ASTAssignmentNode:
	def __init__(self,variable,assignValue,idNo):
		self.variable = variable
		self.assignValue = assignValue
		self.idNo = idNo
	def __str__(self):
		return "Node ID " + str(self.idNo) + " " + self.variable + '     ' + str(self.assignValue)

class ASTExpressionNode:
	def __init__(self,l,r,o,idNo):
		self.l = l
		self.o = o
		self.r = r
		self.idNo = idNo
	def __str__(self):
		return "Node ID " + str(self.idNo) + " operation " + self.o  + " on " + str(self.l) + " " + str(self.r) 
