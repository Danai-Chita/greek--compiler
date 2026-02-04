#Georgia Savva AM:4783
#Danai Chita AM:4838


import sys



infile = open(sys.argv[1])
lines = 1

Trans_Diagram = []

greekWords = []

quads = []

temps = 0

scopes = []

lastQuad = 0
outfile2 = open(sys.argv[1][:-3] + '.asm', 'w')
funcType = ''
retFlag = False

def charToInt(ch):
	if ch in [' ', '\t', '\n']:
		return 0
	elif ch == '':
		return 19
	elif ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
		return 1
	elif ch in 'abcdefghijklmnopqrstuvwxyz':
		return 1
	elif ch in 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ':
		return 1
	elif ch in 'αβγδεζηθικλμνξοπρσςτυφχψω':
		return 1
	elif ch in 'άέήίόύώ':
		return 1
	elif ch in '0123456789':
		return 2
	elif ch == '+':
		return 3
	elif ch == '-':
		return 4
	elif ch == '*':
		return 5
	elif ch == '/':
		return 6
	elif ch == '=':
		return 7
	elif ch == '<':
		return 8
	elif ch == '>':
		return 9
	elif ch == ':':
		return 10
	elif ch == '{':
		return 11
	elif ch == ';':
		return 12
	elif ch == ',':
		return 13
	elif ch == '(':
		return 14
	elif ch == ')':
		return 15
	elif ch == '[':
		return 16
	elif ch == ']':
		return 17
	elif ch == '%':
		return 18
	elif ch == '_':
		return 20
	elif ch == '}':
		return 21
	else:
		return 22
		
	
		
def init():
	global Trans_Diagram, greekWords
	
	col_num = 23
	Trans_Diagram = [[0 for j in range(col_num)] for i in range(7)]
	
	Trans_Diagram[0][0] = 0
	Trans_Diagram[0][1] = 1
	Trans_Diagram[0][2] = 2
	Trans_Diagram[0][3] = 'addtk'
	Trans_Diagram[0][4] = 'subtk'
	Trans_Diagram[0][5] = 'multk'
	Trans_Diagram[0][6] = 'divtk'
	Trans_Diagram[0][7] = 'equaltk'
	Trans_Diagram[0][8] = 3
	Trans_Diagram[0][9] = 4
	Trans_Diagram[0][10] = 5
	Trans_Diagram[0][11] = 6
	Trans_Diagram[0][12] = 'semicolontk'
	Trans_Diagram[0][13] = 'commatk'
	Trans_Diagram[0][14] = 'leftpartk'
	Trans_Diagram[0][15] = 'rightpartk'
	Trans_Diagram[0][16] = 'leftbrackettk'
	Trans_Diagram[0][17] = 'rightbrackettk'
	Trans_Diagram[0][18] = 'percenttk'
	Trans_Diagram[0][19] = 'eoftk'
	Trans_Diagram[0][20] = 'errortk'
	Trans_Diagram[0][21] = 'errortk'
	Trans_Diagram[0][22] = 'errortk'
	
	for i in range(col_num):
		Trans_Diagram[1][i] = 'idtk'
	Trans_Diagram[1][1] = 1
	Trans_Diagram[1][2] = 1
	Trans_Diagram[1][20] = 1

	for i in range(col_num):
		Trans_Diagram[2][i] = 'integertk'
	Trans_Diagram[2][2] = 2
		
	for i in range(col_num):
		Trans_Diagram[3][i] = 'lessthantk'
	Trans_Diagram[3][7] = 'lessequaltk'
	Trans_Diagram[3][9] = 'nonequaltk'
	
	for i in range(col_num):
		Trans_Diagram[4][i] = 'morethantk'
	Trans_Diagram[4][7] = 'moreequaltk' 
		
	for i in range(col_num):
		Trans_Diagram[5][i] = 'error1tk'
	Trans_Diagram[5][7] = 'assigntk' 
	
	for i in range(col_num):
		Trans_Diagram[6][i] = 6
	Trans_Diagram[6][21] = 0
	Trans_Diagram[6][19] = 'error2tk'
	
	greekWords = ['πρόγραμμα', 'δήλωση', 'εάν', 'τότε', 'αλλιώς', 'εάν_τέλος', 'επανάλαβε', 'μέχρι', 'όσο', 'όσο_τέλος', 'για', 'έως', 'με_βήμα', 'για_τέλος', 'διάβασε', 'γράψε', 'συνάρτηση', 'διαδικασία', 'είσοδος', 'έξοδος', 'διαπροσωπεία', 'αρχή_συνάρτησης', 'τέλος_συνάρτησης', 'αρχή_διαδικασίας', 'τέλος_διαδικασίας', 'αρχή_προγράμματος', 'τέλος_προγράμματος', 'ή', 'και', 'όχι', 'εκτέλεσε']

	
	outfile2.write('.data\n')
	outfile2.write('str_nl: .asciz "\\n"\n')
	outfile2.write('.text\n')
	outfile2.write('j Lmain\n')
	
def lex():
	global lines, Trans_Diagram, greekWords
	
	state = 0
	word = ''
	
	
	while str(state)[0] < '7':
		ch = infile.read(1)
		word = word + ch
		if ch == '\n':
			lines = lines + 1
		
		col = charToInt(ch)
		state = Trans_Diagram[state][col]
	
		if str(state)[0] == '0':
			word = ''
	
	if state == 'errortk':
		print('Line %d: Unexptected character'%(lines))
		exit(0)
	elif state == 'error1tk':
		print('Line %d: : should be followed by ='%(lines))
		exit(0)
	elif state == 'error2tk':
		print('Line %d: : eof inside comments'%(lines))
		exit(0)
		
	if state == 'idtk':
		if ch == '\n':
			lines = lines - 1
			
		word = word[:-1]
		infile.seek(infile.tell()-1, 0)
		
		if len(word) > 30:
			print('Line %d: : variable above lenght'%(lines))
			exit(0)
			
		if word in greekWords:
			state = word + 'tk'
	elif state == 'integertk' or state == 'lessthantk' or state == 'morethantk':
		if ch == '\n':
			lines = lines - 1
		word = word[:-1]
		infile.seek(infile.tell()-1, 0)
	
	return state, word
	

def inputCheck(actualtk, actual, expectedtk):
	global lines
	if actualtk != expectedtk:
		print("Line %d: Expected '%s' but got '%s'"%(lines, expectedtk[:-2], actual))
		exit(0)
		
		
if len(sys.argv) < 2:
	print("Please provide input file")
	exit(0)

def program(state, word):
	inputCheck(state, word, 'πρόγραμμαtk')
	state, word = lex()
	inputCheck(state, word, 'idtk')
	progname = word
	state, word = lex()
	state, word = programblock(state, word, progname)
	
	inputCheck(state, word, 'eoftk')
	print("Program compiled with no errors");
	
def programblock(state, word, progname):
	addScope(progname)
	state, word = declarations(state, word)
	state, word = subprograms(state, word)
	
	genquad('begin_block', progname, '_', '_')
	
	inputCheck(state, word, 'αρχή_προγράμματοςtk')
	state, word = lex()
	state, word = sequence(state, word)
	inputCheck(state, word, 'τέλος_προγράμματοςtk')
	genquad('halt', '_', '_', '_')
	deleteScope()
	genquad('end_block', progname, '_', '_')

	state, word = lex()
	return state, word
	
def declarations(state, word):
	while state == 'δήλωσηtk':
		state, word = lex()
		state, word = varlist(state, word, 'variable')
	return state, word
	
def varlist(state, word, vartype):
	inputCheck(state, word, 'idtk')
	if vartype != '':
		addEntity([word, vartype, scopes[0][3]])
	state, word = lex()
	while state == 'commatk':
		state, word = lex()
		inputCheck(state, word, 'idtk')
		if vartype != '':
			addEntity([word, vartype, scopes[0][3]])
		state, word = lex()
	return state, word

def subprograms(state, word):
	while state == 'συνάρτησηtk' or state == 'διαδικασίαtk':
		if state == 'συνάρτησηtk':
			state, word = lex()
			state, word = func(state, word)
		else:
			state, word = lex()
			state, word = proc(state, word)
	return state, word

def func(state, word):
	
	inputCheck(state, word, 'idtk')	
	funcname = word
	state, word = lex()
	inputCheck(state, word, 'leftpartk')
	state, word = lex()
	if state == 'idtk':
		state, word = varlist(state, word, '')
	inputCheck(state, word, 'rightpartk')
	state, word = lex()
	state, word = funcblock(state, word, funcname)
	return state, word

def proc(state, word):
	inputCheck(state, word, 'idtk')	
	procname = word
	state, word = lex()
	inputCheck(state, word, 'leftpartk')
	state, word = lex()
	if state == 'idtk':
		state, word = varlist(state, word, '')
	inputCheck(state, word, 'rightpartk')
	state, word = lex()
	state, word = procblock(state, word, procname)
	return state, word

def funcblock(state, word, funcname):
	global scopes, funcType, retFlag
	
	addEntity([funcname, 'proc', -1, -1])
	addScope(funcname)
	inputCheck(state, word, 'διαπροσωπείαtk')
	state, word = lex()

	state, word = funcinput(state, word)
	state, word = funcoutput(state, word)
		
	state, word = declarations(state, word);
	state, word = subprograms(state, word);
	
	scopes[1][1][len(scopes[1][1]) - 1][2] = nextquad()
	funcType = 'func'
	retFlag = False
	genquad('begin_block', funcname, '_', '_')
	
	inputCheck(state, word, 'αρχή_συνάρτησηςtk')
	state, word = lex()
	
	state, word = sequence(state, word)
	scopes[1][1][len(scopes[1][1]) - 1][3] = scopes[0][3]

	inputCheck(state, word, 'τέλος_συνάρτησηςtk')

	genquad('end_block', funcname, '_', '_')
	deleteScope()

	state, word = lex()
	return state, word

def procblock(state, word, procname):
	global funcType
	
	addEntity([procname, 'proc', -1, -1])
	addScope(procname)
	inputCheck(state, word, 'διαπροσωπείαtk')
	state, word = lex()

	state, word = funcinput(state, word)
	state, word = funcoutput(state, word)
		
	state, word = declarations(state, word);
	state, word = subprograms(state, word);
	scopes[1][1][len(scopes[1][1]) - 1][2] = nextquad()
	funcType = 'proc'

	genquad('begin_block', procname, '_', '_')
	
	inputCheck(state, word, 'αρχή_διαδικασίαςtk')
	state, word = lex()
	
	state, word = sequence(state, word)
	scopes[1][1][len(scopes[1][1]) - 1][3] = scopes[0][3]
	
	inputCheck(state, word, 'τέλος_διαδικασίαςtk')
	genquad('end_block', procname, '_', '_')
	deleteScope()
	state, word = lex()
	return state, word
	
def funcinput(state, word):
	if state == 'είσοδοςtk':
		state, word = lex()
		state, word = varlist(state, word, 'CV')
	return state, word
			
def funcoutput(state, word):
	if state == 'έξοδοςtk':
		state, word = lex()
		state, word = varlist(state, word, 'REF')		
	return state, word
			
def sequence(state, word):
	state, word = statement(state, word)
	while state == 'semicolontk':
		state, word = lex()
		state, word = statement(state, word)
	return state, word
	
def statement(state, word):
	if state == 'idtk':
		state, word = assignment_stat(word)
	elif state == 'εάνtk':
		state, word = if_stat()
	elif state == 'όσοtk':
		state, word = while_stat()
	elif state == 'επανάλαβεtk':
		state, word = do_stat()
	elif state == 'γιαtk':
		state, word = for_stat()
	elif state == 'διάβασεtk':
		state, word = input_stat()
	elif state == 'γράψεtk':
		state, word = print_stat()
	elif state == 'εκτέλεσεtk':
		state, word = call_stat()
	else:
		inputCheck(state, word, 'statementtk')
	return state, word	
		
def assignment_stat(id):
	global retFlag
	
	state, word = lex()
	inputCheck(state, word, 'assigntk')		
	state, word = lex()
	state, word, eplace = expression(state, word)
	if id == scopes[0][0]:
		genquad('retv', eplace, '_', '_')
		if funcType == 'proc':
			print("Line %d: proc can't return"%(lines))
			exit(0)
		retFlag = True
	else:	
		genquad(':=', eplace, '_', id)
	
	return state, word
	
def if_stat():
	state, word = lex()
	state, word, btrue, bfalse = condition(state, word)
	inputCheck(state, word, 'τότεtk')	
	backpatch(btrue, nextquad())
	state, word = lex()
	state, word = sequence(state, word)
	ifList = makelist(nextquad())
	genquad('jump', '_', '_', '_')
	backpatch(bfalse, nextquad())
	
	if state == 'αλλιώςtk':
		state, word = elsepart(state, word)
	inputCheck(state, word, 'εάν_τέλοςtk')
	backpatch(ifList, nextquad())
	state, word = lex()
	
	return state, word
	
def elsepart(state, word):
	state, word = lex()
	state, word = sequence(state, word)
	return state, word
	
def while_stat():
	bquad = nextquad()
	state, word = lex()
	state, word, btrue, bfalse = condition(state, word)
	inputCheck(state, word, 'επανάλαβεtk')	
	backpatch(btrue, nextquad())
	state, word = lex()
	state, word = sequence(state, word)
	genquad('jump', '_', '_', bquad)
	backpatch(bfalse, nextquad())
	inputCheck(state, word, 'όσο_τέλοςtk')
	state, word = lex()
	
	return state, word

def do_stat():
	dquad = nextquad()
	state, word = lex()	
	state, word = sequence(state, word)
	inputCheck(state, word, 'μέχριtk')
	state, word = lex()
	state, word, btrue, bfalse = condition(state, word)
	backpatch(btrue, dquad)
	backpatch(bfalse, nextquad())
	
	return state, word

def for_stat():
	true = emptylist()
	false = emptylist()
	state, word = lex()
	inputCheck(state, word, 'idtk')
	id = word
	state, word = lex()
	inputCheck(state, word, 'assigntk')
	state, word = lex()
	state, word, e1place = expression(state, word)
	genquad(':=', e1place, '_', id)
	jumpList = makelist(nextquad())
	genquad('jump', '_', '_', '_')
	inputCheck(state, word, 'έωςtk')
	state, word = lex()
	state, word, e2place = expression(state, word)
	state, word, Step = step(state, word)
	fquad = nextquad()
	genquad('+', id, Step, id)
	backpatch(jumpList, nextquad())
	lessList = makelist(nextquad())
	genquad('<', Step, 0, '_')
	moreList = makelist(nextquad())
	genquad('>', Step, 0, '_')
	j = makelist(nextquad())
	genquad('jump', '_', '_', '_')
	true = merge(true, j)
	backpatch(lessList, nextquad())
	j = makelist(nextquad())
	genquad('>=', id, e2place, '_')
	true = merge(true, j)
	j = makelist(nextquad())
	genquad('jump', '_', '_', '_')
	false = merge(false, j)
	
	backpatch(moreList, nextquad())
	j = makelist(nextquad())
	genquad('<=', id, e2place, '_')
	true = merge(true, j)
	j = makelist(nextquad())
	genquad('jump', '_', '_', '_')
	false = merge(false, j)
	
	inputCheck(state, word, 'επανάλαβεtk')
	state, word = lex()	
	backpatch(true, nextquad())
	state, word = sequence(state, word)
	genquad('jump', '_', '_', fquad)
	backpatch(false, nextquad())
	inputCheck(state, word, 'για_τέλοςtk')
	state, word = lex()
	return state, word	

def step(state, word):	
	if state == 'με_βήμαtk':
		state, word = lex()
		state, word, place = expression(state, word)
		Step = place
	else:
		Step = newTemp()
		genquad(':=', 0, '_', Step)
	return state, word, Step
	
def print_stat():	
	state, word = lex()
	state, word, place = expression(state, word)
	return state, word	
	
def input_stat():
	state, word = lex()
	inputCheck(state, word, 'idtk')
	genquad('inp', word, '_', '_')
	state, word = lex()	

	return state, word

def call_stat():
	state, word = lex()
	inputCheck(state, word, 'idtk')
	procname = word
	state, word = lex()	
	if state == 'leftpartk':
		state, word = lex()
		state, word = actualpars(state, word)
		
	genquad('call', procname, '_', '_')
	return state, word


def actualpars(state, word):
	if state != 'rightpartk':
		state, word = actualparlist(state, word)
	inputCheck(state, word, 'rightpartk')	
	state, word = lex()
	return state, word
	
def actualparlist(state, word):
	state, word = actualparitem(state, word)
	
	while state == 'commatk':
		state, word = lex()
		state, word = actualparitem(state, word)
	return state, word
	
def actualparitem(state, word):
	if state == 'percenttk':
		state, word = lex()
		inputCheck(state, word, 'idtk')
		genquad('par', word, 'REF', '_')
		
		state, word = lex()
	else:
		state, word, eplace = expression(state, word)
		genquad('par', eplace, 'CV', '_')
	return state, word
	
def condition(state, word):
	state, word, btrue, bfalse = boolterm(state, word)
	
	while state == 'ήtk':
		state, word = lex()
		backpatch(bfalse, nextquad())
		state, word, q2true, q2false = boolterm(state, word)
		
		btrue = merge(btrue, q2true)
		bfalse = q2false
	return state, word, btrue, bfalse

def boolterm(state, word):
	state, word, qtrue, qfalse = boolfactor(state, word)
	
	while state == 'καιtk':
		state, word = lex()
		backpatch(qtrue, nextquad())
		state, word, r2true, r2false = boolfactor(state, word)
		
		qfalse = merge(qfalse, r2false)
		qtrue = r2true
		
	return state, word, qtrue, qfalse

def boolfactor(state, word):
	if state == 'όχιtk':
		state, word = lex()
		inputCheck(state, word, 'leftbrackettk')	
		state, word = lex()
		state, word, rfalse, rtrue = condition(state, word)
		inputCheck(state, word, 'rightbrackettk')
		state, word = lex()
	elif state == 'leftbrackettk':
		state, word = lex()
		state, word, rtrue, rfalse = condition(state, word)
		inputCheck(state, word, 'rightbrackettk')
		state, word = lex()
	else:
		state, word, e1place = expression(state, word)
		if state == 'equaltk' or state == 'lessequaltk' or state == 'moreequaltk' or state == 'nonequaltk' or state == 'lessthantk' or state == 'morethantk':
			wop = word
			state, word = lex()
			state, word, e2place = expression(state, word)
			
			rtrue = makelist(nextquad())
			genquad(wop, e1place, e2place, '_')
			rfalse = makelist(nextquad())
			genquad('jump', '_', '_', '_')
		else:
			inputCheck(state, word, 'relational operatortk')
	return state, word, rtrue, rfalse
			
def expression(state, word):

	if state == 'addtk' or state == 'subtk':
		w = word
		state, word = lex()
		word = w + word
		
	state, word, t1place = term(state, word)
	
	while state == 'addtk' or state == 'subtk':
		wop = word
		state, word = lex()
		state, word, t2place = term(state, word)
		
		w = newTemp()
		genquad(wop, t1place, t2place, w)
		t1place = w
		
	return state, word, t1place
	
def term(state, word):
	
	state, word, f1place = factor(state, word)
	
	while state == 'multk' or state == 'divtk':
		wop = word
		state, word = lex()
		state, word, f2place = factor(state, word)
		
		w = newTemp()
		genquad(wop, f1place, f2place, w)
		f1place = w
	return state, word, f1place

def factor(state, word):
	place = word
	if state == 'integertk':
		state, word = lex()
	elif state == 'leftpartk':
		state, word = lex()
		state, word, place = expression(state, word)
		inputCheck(state, word, 'rightpartk')
		state, word = lex()
	elif state == 'idtk':
		state, word = lex()
		if state == 'leftpartk':
			state, word = lex()
			state, word = actualpars(state, word)
			
			w = newTemp()
			genquad('par', w, 'RET', '_')
			genquad('call', place, '_', '_')
			place = w
	else:
		inputCheck(state, word, 'expressiontk')
		
	return state, word, place


def nextquad():
	return len(quads)
	
def genquad(op, x, y, z):
	global quads
	
	quads.append([str(nextquad()), op, str(x), str(y), str(z)])
	
def newTemp():
	global temps, scopes
	
	temps = temps + 1
	t = 't@' + str(temps)
	addEntity([t, 'temp', scopes[0][3]])
	return t
	
def emptylist():
	return []
	
def makelist(x):
	return [x]
	
def merge(list1, list2):
	list1.extend(list2)
	return list1
	
def backpatch(list1, z):
	global quads
	
	for i in list1:
		quads[i][4] = str(z)
		
def intCode():
	outfile = open(sys.argv[1][:-3] + '.int', 'w')
	
	for q in quads:
		outfile.write('%s : %s , %s , %s , %s\n'%(q[0], q[1], q[2], q[3], q[4]))
	

def addScope(scopename):
	global scopes
	
	scopes.insert(0, [scopename, [], len(scopes), 12])
	
def deleteScope():
	global scopes, lastQuad, quads, retFlag
	
	quadsPart = quads[lastQuad:]
	lastQuad = len(quads)
	i = 0
	for q in quadsPart:
		outfile2.write('# %s : %s , %s , %s , %s\n'%(q[0], q[1], q[2], q[3], q[4]))
		
		if q[1] == 'out':
			loadvr(1, q[2])
			outfile2.write('mv a0, t1\n')
			outfile2.write('li a7, 1\n')
			outfile2.write('ecall\n')
			
			outfile2.write('la a0, str_nl\n')
			outfile2.write('li a7, 4\n')
			outfile2.write('ecall\n')
		elif q[1] == 'inp':
			outfile2.write('li a7, 5\n')
			outfile2.write('ecall\n')
			outfile2.write('mv t1, a0\n')
			storerv(1, q[2])
		elif q[1] == 'jump':
			outfile2.write('j L%s\n'%(q[4]))
		elif q[1] == '>' or q[1] == '<' or q[1] == '>=' or q[1] == '>=' or q[1] == '<>' or q[1] == '=':
			loadvr(q[2], 1)
			loadvr(q[3], 2)
			if q[1] == '>':
				outfile2.write('bgt t1, t2, L%s\n'%(q[4]))
			elif q[1] == '<':
				outfile2.write('blt t1, t2, L%s\n'%(q[4]))
			elif q[1] == '>=':
				outfile2.write('bge t1, t2, L%s\n'%(q[4]))
			elif q[1] == '<=':
				outfile2.write('bge t1, t2, L%s\n'%(q[4]))
			elif q[1] == '=':
				outfile2.write('beq t1, t2, L%s\n'%(q[4]))
			elif q[1] == '<>':
				outfile2.write('bne t1, t2, L%s\n'%(q[4]))
		elif q[1] == '+' or q[1] == '-' or q[1] == '*' or q[1] == '/':
			loadvr(q[2], 1)
			loadvr(q[3], 2)
			if q[1] == '+':
				outfile2.write('add t1, t1, t2\n')
			elif q[1] == '-':
				outfile2.write('sub t1, t1, t2\n')
			elif q[1] == '*':
				outfile2.write('mul t1, t1, t2\n')
			elif q[1] == '/':
				outfile2.write('div t1, t1, t2\n')
			storerv(1, q[4])
		elif q[1] == ':=':
			loadvr(q[2], 1)
			storerv(1, q[4])
		elif q[1] == 'retv':
			loadvr(q[2], 1)
			outfile2.write('lw t0, -8(sp)\n')
			outfile2.write('sw t1, (t0)\n')
		elif q[1] == 'par':
			if i == 0:
				k = 0
				for q1 in quadsPart:
					if q1[0] > q[0] and q1[1] == 'call':
						entity, nestingLevel = searchEntity(q1[2])
						if entity[1] != 'func' and entity[1] != 'proc':
							print("Line %d: '%s' cannot be used as func/proc"%(lines, entity[0]))
							exit(0)
						outfile2.write('addi fp, sp, %d\n'%(entity[3]))
						break
			if q[3] == 'CV':
				loadvr(q[2], 0)
				outfile2.write('sw t0, %d(fp)\n'%(-(12+4*i)))
			elif q[3] == 'RET':
				entity, nestingLevel = searchEntity(q[2])
				outfile2.write('addi t0, sp, %d\n'%(-(12+4*i)))
				outfile2.write('sw t0, -8(fp)\n')
			i = i + 1
		elif q[1] == 'call':
			i = 0
			entity, nestingLevel = searchEntity(q[2])
			if entity[1] != 'func' and entity[1] != 'proc':
				print("Line %d: '%s' cannot be used as func/proc"%(lines, entity[0]))
				exit(0)
			outfile2.write('sw sp, -4(fp)\n')
			outfile2.write('addi sp, sp, %d\n'%(entity[3]))
			outfile2.write('jal L%d\n'%(entity[2]))
			outfile2.write('addi sp, sp, -%d\n'%(entity[3]))
		elif q[1] == 'begin_block':
			if len(scopes) == 1:
				outfile2.write('Lmain:\n')
				outfile2.write('addi sp, sp, %s\n'%(scopes[0][2]))
				outfile2.write('mv gp, sp\n')
				
			else:
				
				outfile2.write('sw ra, (sp)\n')
		elif q[1] == 'end_block':
			if len(scopes) > 1:
				outfile2.write('lw ra, (sp)\n')
				outfile2.write('jr ra\n')

				if retFlag == False:
					print("Line %d: Expected return at the end of function %s"%(lines, q[2]))
					exit(0)
		
					
	print(scopes)
	print()
	del scopes[0]
	
def addEntity(entity):
	global scopes
	
	scopes[0][1].append(entity)
	if entity[1] != 'func' and entity[1] != 'proc':
		scopes[0][3] = scopes[0][3] + 4

def searchEntity(entityname):
	global scopes
	
	for i in range(len(scopes)):
		entities = scopes[i][1]
		for j in range(len(entities)):
			entity = entities[j]
			if entity[0] == entityname:
				return entity, scopes[0][2]
	
	print("Line %d: '%s' is not declared"%(lines, entityname))
	exit(0)

def gnlvcode(offset, dif):
	outfile2.write('lw t0, -4(sp)\n')
	for i in range(dif):
		outfile2.write('lw t0, -4(t0)\n')
	
	outfile2.write('addi t0, t0, -%d\n'%(offset))
	
def loadvr(v,r):
	global scopes
	
	if v[0] in '0123456789-+':
		outfile2.write('li t%d, %s\n'%(r, v))
	else:
		entity, nestingLevel = searchEntity(v)
		if entity[1] == 'func' or entity[1] == 'proc':
			print("Line %d: '%s' cannot be used as variable"%(lines, entity[0]))
			exit(0)
			
		if nestingLevel == 0:
			outfile2.write('lw t%d, -%d(gp)\n'%(r, entity[2]))
		elif nestingLevel == len(scopes) - 1:
			if entity[1] != 'REF':
				outfile2.write('lw t%d, -%d(sp)\n'%(r, entity[2]))
			else:
				outfile2.write('lw t0, -%d(gp)\n'%(entity[2]))
				outfile2.write('lw t%d, (t0)\n'%(r))
		else:
			dif = (len(scopes) - 1) - nestingLevel - 1
			gnlvcode(entity[2], dif)
			if entity[1] != 'REF':
				outfile2.write('lw t%d, (t0)\n'%(r))
			else:
				outfile2.write('lw t0, (t0)\n')
				outfile2.write('lw t%d, (t0)\n'%(r))
	
def storerv(r,v):
	entity, nestingLevel = searchEntity(v)
	if entity[1] == 'func' or entity[1] == 'proc':
		print("Line %d: '%s' cannot be used as variable"%(lines, entity[0]))
		exit(0)
	if nestingLevel == 0:
		outfile2.write('sw t%d, -%d(gp)\n'%(r, entity[2]))
	elif nestingLevel == len(scopes) - 1:
		if entity[1] != 'REF':
			outfile2.write('sw t%d, -%d(sp)\n'%(r, entity[2]))
		else:
			outfile2.write('lw t0, -%d(gp)\n'%(entity[2]))
			outfile2.write('sw t%d, (t0)\n'%(r))
	else:
		dif = (len(scopes) - 1) - nestingLevel - 1
		gnlvcode(entity[2], dif)
		if entity[1] != 'REF':
			outfile2.write('lw t%d, (t0)\n'%(r))
		else:
			outfile2.write('sw t0, (t0)\n')
			outfile2.write('sw t%d, (t0)\n'%(r))
			
init()
state, word = lex()
program(state, word)
intCode()
