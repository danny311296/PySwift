inputFile = open('tac.s','r')
outputFile = open('optimizedTac.s','w+')

#Constant Folding optimisation
for line in inputFile:
	if '=' in line and 'goto' not in line:
		lhs = line.split('=')[0].strip()
		print( lhs + ' = ',file=outputFile,end='')
		exp = line.split('=')[1].strip()
		try:
			rhs = eval(exp)
			print(rhs,file=outputFile)
		except:
			print(exp,file=outputFile)
	else:
		print(line,file=outputFile,end='')
