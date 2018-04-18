from collections import defaultdict

astFileText = list(filter(None,open('swift.ast','r').read().split('\n')))
length = len(astFileText)
tempCount = 0
operation = ''
i = 0
dictionary = defaultdict(lambda: None)
line = astFileText[i]

lineNo = 0
forLoopCount = []
functions = {}

def generateCode(line):
	global tempCount,operation, lineNo
	if(line.split()[0]=="---assign"):
		operation = 'assign'
		lhs = line.split()[1]
		if(line.split()[2] != 'Node'):
			rhs = line.split()[2]
		else:
			rhsNode = line.split()[3]
			expressions = str(" ".join(astFileText[i+1].split())).split('---expression')[1:]
			expressions = expressions[::-1]
			for exp in expressions:
				e = exp.split()
				lhs = e[0]
				op = e[2]
				op1 = e[4]
				op2 = e[5]
				if(not(op1.startswith('Node')) and not(op2.startswith('Node'))):
					print(str(lineNo) +" : "+'t' + str(tempCount) + ' = ' + op1 + " " + op + " " + op2)
					lineNo += 1
					dictionary[lhs] = 't' + str(tempCount)
					tempCount += 1
				else:
					if(op1.startswith('Node')):
						op1 = dictionary[op1]
					if(op2.startswith('Node')):
						op2 = dictionary[op2]
					print(str(lineNo) +" : "+'t' + str(tempCount) + ' = ' + str(op1) + " " + op + " " + str(op2))
					lineNo += 1
					dictionary[lhs] = 't' + str(tempCount)
					tempCount += 1
	elif(line.split()[0] == '---for-loop'):
		_, lhs, _, _id, _, start, _, end = astFileText[i+1].split()
		print(str(lineNo) +" : "+'t' + str(tempCount) + ' = ' + str(start))
		lineNo += 1
		# print(str(lineNo) +" : "+'if '+ 't' + str(tempCount) + ' < ' + str(int(end)+1))
		# lineNo += 1
		dictionary[lhs] = 't' + str(tempCount)
		tempCount += 1
		forLoopCount.append([dictionary[lhs], lineNo-1, int(end)+1])
	elif(line.split()[0] == '---function-defination'):
		keys = astFileText[i+1].split()
		name = keys[1]
		returntype = keys[-1]
		params = keys[3:-2]
		functions[name] = {"params" : params, "returntype": returntype, "startline":lineNo}
		print("Function : "+name)

while(1):

	# print(line)
	if(line.startswith("Node")):
		i += 1
		line = astFileText[i]
		generateCode(line)
		if(operation=='assign'):
			i += 2
		if(i>=length):
			break
		line = astFileText[i]
	elif(line.startswith("EndOfFor")):
		tempVar, ln, end = forLoopCount.pop()
		print(str(lineNo) +" : " + tempVar + " = " + tempVar + " + 1")
		lineNo += 1
		print(str(lineNo) +" : " + 'if ' + tempVar + ' < ' + str(end) +" goto "+ str(ln))
		lineNo += 1
		i += 1
		line = astFileText[i]
	elif(line.startswith("EndofFunction")):
		pass
		break
		# print(str(lineNo) +" : " + tempVar + " = " + tempVar + " + 1")
		# lineNo += 1
	# elif(line.startswith("FuntionCall")):
