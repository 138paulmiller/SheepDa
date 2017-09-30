#!/usr/bin/env python

'''
SheepDa - A "Soft" Functional Programming Language

Copyright 2017 Paul Miller (github.com/138paulmiller)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

'''


'''
AST Node Tags
'''
APPLY 	= 'APPLY' 	# Lambda Application
CLOSURE = 'CLOSURE'  # Lambda Abstaction
ASSIGN 	= 'ASSIGN'  # Variable assignement
BUILTIN 	= 'BUILTIN' # Builtin Variables

'''
Token Symbol Tags
'''
LPAREN 	= 'LPAREN'
RPAREN 	= 'RPAREN'
LAMBDA 	= 'LAMBDA'
DOT 	= 'DOT'
EQUAL	= 'EQUAL'
VAR 	= 'VAR'
NUM 	= 'NUM'
EOI 	= 'EOI'
ERROR 	= 'ERROR'

def main():

	input = file("src.da").read()
	lexer = Lexer(input)
	# generate ast [expr ... ]
	ast = parse(lexer)
	# global bindings
	bindings = {} 
	# evaluate each expr in ast
	for node in ast:
		evaluate(node, bindings)
			
		# print variable bindings
		# print '----------VARS----------'
		# for var in bindings.items():
		# 	print var
		# print '------------------------'
		# raw_input()
		
class Lexer:
	'''
	 Returns tokens (tag, value)
	'''
	def __init__(self, input):
		self.input = input
		self.pos = 0 
		self.len = len(self.input)

	def peek(self):
		token = None
		# eat whitespace
		while self.pos < self.len and  \
		  (self.input[self.pos] == ' '  or \
		  self.input[self.pos] == '\t' or \
		  self.input[self.pos] == '\n'):
			self.pos+=1
		if self.pos >= self.len:
			token = (EOI, 'End of Input')
		else:
			sym = self.input[self.pos]
			if  sym == '(':
				token = (LPAREN,sym )
			elif sym == ')':
				token = (RPAREN, sym)
			elif sym == '\\':
				token = (LAMBDA, sym)
			elif sym == '.': 
				token = (DOT, sym)
			elif sym == '=': 
				token = (EQUAL, sym)
			elif sym.isalpha(): # id
				var = sym
				i = self.pos+1
				while i <  self.len and self.input[i].isalnum(): 
					var += self.input[i]
					i+=1
				token = (VAR, var)
			elif sym.isdigit(): # id
				num = sym
				i = self.pos+1
				while i <  self.len and self.input[i].isalnum(): 
					num += self.input[i]
					i+=1
				if i < len(self.input) and self.input[i] == '.':
					while i < self.len and \
						self.input[i].isalnum(): 
						num += self.input[i]
						i+=1
				token = (NUM, num)
			else:
				token = (ERROR, 'Lexical Error: Unknown Token: ' + value)
		return token									

	def next(self):
		token = self.peek()
		if token:
			# offset input by token lexeme len
			self.pos += len(token[1])
		else:
			token = (ERROR, 'Lexical Error: Unexpected NULL Token') 
		return token


def parse(lexer):
	'''
	Returns AST Nodes 
		(ASSIGN, (var_id, expr))
		(CLOSURE, ([<var_id> ...], expr))
		(APPLY expr [<expr> ...])
	'''
	ast = []
	tag, value = lexer.peek()
	while tag != ERROR and tag  != EOI:
		if tag == VAR:
			# get var 
			var = lexer.next()
			# check next token for equal sign
			tag, value = lexer.next()
			if tag == EQUAL:
				# return var value (id) and expression
				ast.append((ASSIGN, (var[1], parse_expr(lexer))))
			else: # standalone var
				ast.append(var)
		else:
			ast.append( parse_expr(lexer))
		tag, value = lexer.peek()
	
	return ast


def parse_expr(lexer):
	'''
	Parses individual expressions
	'''
	tag, value = lexer.next()
	root = None
	if tag == VAR or tag == NUM: # if atom
		 # eat token
		root = (tag, value)
		# return 
	elif tag == LAMBDA: # if abstraction
		bindings = [] #  bound parameter ids
		# get next, must be either var or dot
		tag, value = lexer.next()
		# get all following var values (ids)
		while tag == VAR:
			bindings.append(value)
			tag, value = lexer.next()
		if tag == DOT:
			root = (CLOSURE, (bindings, parse_expr(lexer)))
		else:
			root = (ERROR, "Syntax Error: Expected " + DOT + " at: " + value)
	elif tag == LPAREN: # if application
		# apply first expression to all expressions until rparen
		expr = None 
		var = parse_expr(lexer)
		if var[0] != VAR:
		 	expr = var
		else:
		 	expr = var[1]
		args = []
		# eat lparen
		tag, value = lexer.peek()
		while tag != RPAREN and tag != ERROR:
			args.append(parse_expr(lexer))
			tag, value = lexer.peek()
		#eat rparen
		lexer.next()
		root = (APPLY, (expr, args))
	else:
		root = (ERROR, "Syntax Error: Unexpected :"+ value)
	return root

##################		Evaluation		##########################

class Closure:
	'''
		Closure Container
	'''
	def __init__(self, bindings, params, expr):
		# locally bound variables
		self.bindings = {}
		for var in bindings.keys():
			self.bindings[var] = bindings[var]

		# parameters to be substituted at call binding scope
		self.params = []
		for var in params:
			self.params.append(var)		
		# expression to evaluate at the scope of bindings
		self.expr = expr

	def __repr__(self):
		s = 'CLOSURE: ('
		for p in self.params:
			s+= p + ' '
		s += ')'
		# s += ')\n\tBOUND: '
		# for var, value in self.bindings.items():
		# 	s += '\n\t\t' + var + ': ' + str(value) 
		return  s
	

def evaluate(root, bindings):
	expr = root # evaluated expression
	tag, value = root
	if tag == ASSIGN:
		# add expr to binding with var key
		expr = bindings[value[0]] = evaluate(value[1], bindings)
	elif tag == CLOSURE:
		# return a closure object with parent bindings
		expr =  Closure(bindings, value[0], value[1])
	elif tag == APPLY:
		# Evaluate by  binding all closure params with each args
		var = value[0] # get closure id
		args = value[1]   
		closure = None
		# if an application, get the closure
		if var[0] == APPLY:
			closure = evaluate(var, bindings)
		# if application
		elif var not in bindings:
			# get builtin closure 
			closure = evaluate((VAR, var), bindings)
		# get the closure to be called
		else:
			closure = bindings[var]
		# if closure was found
		
		if isinstance(closure, Closure):
			count= len(args)
			params = None
			local_bindings	= {}
			# bind all closure and global bindings locally
			for bind in closure.bindings.keys():
				local_bindings[bind] = closure.bindings[bind]
			for bind in bindings:
				local_bindings[bind] = bindings[bind]


			params = closure.params
			if len(params) != count:
				expr = (ERROR, "Incorrect argument amount passed to application:", var)
			else:
				# evaluate each argument and bind it to the local level 
				for i in range(0, count):
					local_bindings[params[i]] = evaluate(args[i], bindings) 
			expr = evaluate(closure.expr, local_bindings)
			if expr == None:
				expr = (ERROR, str(var) + ' is not bound to this closure')
		# empty closure, could not find
		else:
			expr = (ERROR, str(var) + " is not bound within this application: ")
	elif tag == VAR:
		if value in bindings:
			expr = bindings[value] 	
		else:
			expr = evaluate_builtin(root, bindings)
			# if var value did not match nay closures, then not defined yet
	elif tag == NUM:
		expr = float(value)
	elif tag == ERROR:
		print 'ERROR', expr
	elif tag == BUILTIN:
		expr = evaluate_builtin(value, bindings)
		if expr == None:
			expr = (ERROR, value + ' is not bound within this context.')
	return expr
 

def evaluate_builtin(root, bindings):

	expr = None
	#if var then requesting  closure defition
	if root[0] == VAR:
		tag, value = root
		if value == 'add':
			expr = bindings[value] = Closure(bindings,  ['_x', '_y'], (BUILTIN, 'add'))
		elif value == 'sub':
			expr = bindings[value] = Closure(bindings,  ['_x', '_y'], (BUILTIN, 'sub'))
		elif value == 'mul':
			expr = bindings[value] = Closure(bindings,  ['_x', '_y'], (BUILTIN, 'mul'))
		elif value == 'div':
			expr = bindings[value] = Closure(bindings,  ['_x', '_y'], (BUILTIN, 'div'))
		elif value == 'print':
			expr = bindings[value] = Closure(bindings,  ['_x'], (BUILTIN, 'print'))
	# else ( var, args) call to closure
	else: 
		if root == 'add':
			expr = bindings['_x'] + bindings['_y'] 
		elif root == 'sub':
			expr = bindings['_x'] - bindings['_y'] 
		elif root == 'mul':
			expr = bindings['_x'] * bindings['_y'] 
		elif root == 'div':
			expr = bindings['_x'] / bindings['_y'] 
		elif root == 'print':
			expr = bindings['_x']
			print expr 
	return expr

# Run main after all defintions 
if __name__ == '__main__':
	main()


