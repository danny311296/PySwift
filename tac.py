from collections import defaultdict

astFileText = list(filter(None,open('swift.ast','r').read().split('\n')))
length = len(astFileText) 
tempCount = 0
i = 0
labelCount = 0
dictionary = defaultdict(lambda: None)
line = astFileText[i]

def generateCodeForBasicStatement(line):
	global tempCount,i
	lhsvar = line.split()[1]
	if(line.split()[2] != 'Node'):
		rhs = line.split()[2]
		print(lhsvar + ' = ' + rhs)
		i += 1
	else:
		expressions = str(" ".join(astFileText[i+1].split())).split('---expression')[1:]
		expressions = expressions[::-1]
		iterationCount = 0
		for exp in expressions:
			iterationCount += 1
			e = exp.split()
			lhs = e[0]
			op = e[2]
			op1 = e[4]
			op2 = e[5]
			if(iterationCount == len(expressions)):
				if(op1.startswith('Node')):
					op1 = dictionary[op1]
				if(op2.startswith('Node')):
					op2 = dictionary[op2]				
				print('t' + str(tempCount) + ' = ' + str(op1) + " " + op + " " + str(op2))
				dictionary[lhs] = 't' +str(tempCount)
				print(lhsvar + ' = ' + 't' + str(tempCount) )
				tempCount += 1
				break
			if(not(op1.startswith('Node')) and not(op2.startswith('Node'))):
				print('t' + str(tempCount) + ' = ' + op1 + " " + op + " " + op2)
				dictionary[lhs] = 't' + str(tempCount)
				tempCount += 1
			else:
				if(op1.startswith('Node')):
					op1 = dictionary[op1]
				if(op2.startswith('Node')):
					op2 = dictionary[op2]				
				print('t' + str(tempCount) + ' = ' + str(op1) + " " + op + " " + str(op2))
				dictionary[lhs] = 't' + str(tempCount)
				tempCount += 1
		i += 2

def generateCodeForForLoop(line):
	global tempCount,i,labelCount
	var =  astFileText[i+1].split()[2]
	initial = astFileText[i+1].split()[3]
	final = astFileText[i+1].split()[4]
	print(var + ' = ' + initial)
	print("L" + str(labelCount) + ":")
	i += 4
	l = astFileText[i]
	while(1):
		generateCodeForBasicStatement(astFileText[i])
		l = astFileText[i]
		if(l == 'End of For statement'):
			break
		i += 1 
		l = astFileText[i]
	i += 1
	print('t' + str(tempCount) + ' = ' + var + ' + 1')
	print(var + ' = ' + 't' + str(tempCount)) 
	tempCount += 1 
	print('if ' + var + ' <= ' + final + ' goto L' + str(labelCount))
	labelCount += 1

def generateCode(line):
	if(line.split()[0]=="---assign"):
		generateCodeForBasicStatement(line)
	elif(line.split()[0]=='---for-loop'):
		generateCodeForForLoop(line)


while(1):
	if(line.startswith("Node")):
		i += 1
		line = astFileText[i]
		generateCode(line)
		if(i>=length):
			break
		line = astFileText[i]
		
			

