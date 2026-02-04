import sys



infile = open(sys.argv[1])
lines = 1

Trans_Diagram = []

greekWords = []


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
	state, word = lex()
	state, word = programblock(state, word)
	
	inputCheck(state, word, 'eoftk')
	print("Program compiled with no errors");
	
def programblock(state, word):
	state, word = declarations(state, word)
	state, word = subprograms(state, word)
	
	inputCheck(state, word, 'αρχή_προγράμματοςtk')
	state, word = lex()
	state, word = sequence(state, word)
	inputCheck(state, word, 'τέλος_προγράμματοςtk')
	state, word = lex()
	return state, word
	
def declarations(state, word):
	while state == 'δήλωσηtk':
		state, word = lex()
		state, word = varlist(state, word)
	return state, word
	
def varlist(state, word):
	inputCheck(state, word, 'idtk')
	state, word = lex()
	while state == 'commatk':
		state, word = lex()
		inputCheck(state, word, 'idtk')
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
	state, word = lex()
	inputCheck(state, word, 'leftpartk')
	state, word = lex()
	if state == 'idtk':
		state, word = varlist(state, word)
	inputCheck(state, word, 'rightpartk')
	state, word = lex()
	state, word = funcblock(state, word)
	return state, word

def proc(state, word):
	inputCheck(state, word, 'idtk')	
	state, word = lex()
	inputCheck(state, word, 'leftpartk')
	state, word = lex()
	if state == 'idtk':
		state, word = varlist(state, word)
	inputCheck(state, word, 'rightpartk')
	state, word = lex()
	state, word = procblock(state, word)
	return state, word

def funcblock(state, word):
	inputCheck(state, word, 'διαπροσωπείαtk')
	state, word = lex()

	state, word = funcinput(state, word)
	state, word = funcoutput(state, word)
		
	state, word = declarations(state, word);
	state, word = subprograms(state, word);
	inputCheck(state, word, 'αρχή_συνάρτησηςtk')
	state, word = lex()
	
	state, word = sequence(state, word)
	
	inputCheck(state, word, 'τέλος_συνάρτησηςtk')
	state, word = lex()
	return state, word

def procblock(state, word):
	inputCheck(state, word, 'διαπροσωπείαtk')
	state, word = lex()

	state, word = funcinput(state, word)
	state, word = funcoutput(state, word)
		
	state, word = declarations(state, word);
	state, word = subprograms(state, word);
	inputCheck(state, word, 'αρχή_διαδικασίαςtk')
	state, word = lex()
	
	state, word = sequence(state, word)
	
	inputCheck(state, word, 'τέλος_διαδικασίαςtk')
	state, word = lex()
	return state, word
	
def funcinput(state, word):
	if state == 'είσοδοςtk':
		state, word = lex()
		state, word = varlist(state, word)
	return state, word
			
def funcoutput(state, word):
	if state == 'έξοδοςtk':
		state, word = lex()
		state, word = varlist(state, word)		
	return state, word
			
def sequence(state, word):
	state, word = statement(state, word)
	while state == 'semicolontk':
		state, word = lex()
		state, word = statement(state, word)
	return state, word
	
def statement(state, word):
	if state == 'idtk':
		state, word = assignment_stat()
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
		
def assignment_stat():
	state, word = lex()
	inputCheck(state, word, 'assigntk')		
	state, word = lex()
	state, word = expression(state, word)
	return state, word
	
def if_stat():
	state, word = lex()
	state, word = condition(state, word)
	inputCheck(state, word, 'τότεtk')	
	state, word = lex()
	state, word = sequence(state, word)
	if state == 'αλλιώςtk':
		state, word = elsepart(state, word)
	inputCheck(state, word, 'εάν_τέλοςtk')
	state, word = lex()
	
	return state, word
	
def elsepart(state, word):
	state, word = lex()
	state, word = sequence(state, word)
	return state, word
	
def while_stat():
	state, word = lex()
	state, word = condition(state, word)
	inputCheck(state, word, 'επανάλαβεtk')	
	state, word = lex()
	state, word = sequence(state, word)

	inputCheck(state, word, 'όσο_τέλοςtk')
	state, word = lex()
	
	return state, word

def do_stat():
	state, word = lex()	
	state, word = sequence(state, word)
	inputCheck(state, word, 'μέχριtk')
	state, word = lex()
	state, word = condition(state, word)
	
	return state, word

def for_stat():
	state, word = lex()
	inputCheck(state, word, 'idtk')
	state, word = lex()
	inputCheck(state, word, 'assigntk')
	state, word = lex()
	
	state, word = expression(state, word)
	inputCheck(state, word, 'έωςtk')
	state, word = lex()
	state, word = expression(state, word)
	state, word = step(state, word)
	inputCheck(state, word, 'επανάλαβεtk')
	state, word = lex()	
	state, word = sequence(state, word)
	inputCheck(state, word, 'για_τέλοςtk')
	state, word = lex()
	return state, word	

def step(state, word):	
	if state == 'με_βήμαtk':
		state, word = lex()
		state, word = expression(state, word)
	return state, word
	
def print_stat():	
	state, word = lex()
	state, word = expression(state, word)
	return state, word	
	
def input_stat():
	state, word = lex()
	inputCheck(state, word, 'idtk')
	state, word = lex()	

	return state, word

def call_stat():
	state, word = lex()
	inputCheck(state, word, 'idtk')
	state, word = lex()	
	if state == 'leftpartk':
		state, word = lex()
		state, word = actualpars(state, word)
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
		state, word = lex()
	else:
		state, word = expression(state, word)
	return state, word
	
def condition(state, word):
	state, word = boolterm(state, word)
	
	while state == 'ήtk':
		state, word = lex()
		state, word = boolterm(state, word)
	return state, word

def boolterm(state, word):
	state, word = boolfactor(state, word)
	
	while state == 'καιtk':
		state, word = lex()
		state, word = boolfactor(state, word)
	return state, word

def boolfactor(state, word):
	if state == 'όχιtk':
		state, word = lex()
		inputCheck(state, word, 'leftbrackettk')	
		state, word = lex()
		state, word = condition(state, word)
		inputCheck(state, word, 'rightbrackettk')
		state, word = lex()
	elif state == 'leftbrackettk':
		state, word = lex()
		state, word = condition(state, word)
		inputCheck(state, word, 'rightbrackettk')
		state, word = lex()
	else:
		state, word = expression(state, word)
		if state == 'equaltk' or state == 'lessequaltk' or state == 'moreequaltk' or state == 'nonequaltk' or state == 'lessthantk' or state == 'morethantk':
			state, word = lex()
			state, word = expression(state, word)
		else:
			inputCheck(state, word, 'relational operatortk')
	return state, word
			
def expression(state, word):

	if state == 'addtk' or state == 'subtk':
		state, word = lex()
	state, word = term(state, word)
	
	while state == 'addtk' or state == 'subtk':
		state, word = lex()
		state, word = term(state, word)
	return state, word
	
def term(state, word):
	
	state, word = factor(state, word)
	
	while state == 'multk' or state == 'divtk':
		state, word = lex()
		state, word = factor(state, word)
	return state, word

def factor(state, word):
	if state == 'integertk':
		state, word = lex()
	elif state == 'leftpartk':
		state, word = lex()
		state, word = expression(state, word)
		inputCheck(state, word, 'rightpartk')
		state, word = lex()
	elif state == 'idtk':
		state, word = lex()
		if state == 'leftpartk':
			state, word = lex()
			state, word = actualpars(state, word)
	else:
		inputCheck(state, word, 'expressiontk')
	return state, word

init()
state, word = lex()
program(state, word)
