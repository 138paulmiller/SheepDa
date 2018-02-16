# SheepDa
### A Soft Functional Scripting Language
Sheepda provides a minimal syntax as a "Soft" introduction to Functional Programming concepts.
Language features closures, dynamic binding, static scoping, and lazy evaluation with a syntax mixture of LISP and Lamba-Calculus. 

#### Usage
See HELP for menu

##### Why?
This project started out as a small language to help programmers quickly understand fundamental functional programming concepts such as first-class functions, immutability and lazy-evaluation. 
I will be spending time adding various features to the language to help it evolve from a toy language into a useful scripting language.

##### Syntax:
	<stmt>	: <id> = <expr>			// Binds expression to identifier
		| <expr>			// Stand-alone Expression
		| ; <sym> ... \n		// Comments, ends at newline
	<expr>	: (\ <param_id> <...> . <expr>)	// Defines an abstraction
		| (<expr> <expr> <..>)		// Applies expressions on the right to the leftmost expression
		| [0-9]+.?[0-9]*		// Integer of Floating point number 
		| [a-zA-Z]+[a-zA-Z0-9]*		// Identifier 
		| [ <expr> ... ]		// List, closed brakcets with exprs seperated by spaces
		| "."				// String, anything encapsulated within quotes

##### Overview
Various example programs can be found in the example directory. 
LISP-like prefix expressions with a lambda calculus like abstraction syntax.

Anonymous functions using the lambda operator.


	x = ( \ x y . (+ x y ))		; Assign closed expression to x
	(print (x 10 20))		; Prints 30, x->10
	(print (\x y.(+ x y) 10 20))	; Also prints 30, lambda expression dynamically evaluated
	
	p = print
	(p "Hello")			; p is now a reference to print


Importing other files

	(import "examples/fib.da") 	; Interprets the file at the relative directory of script 

	
Builtin List features.
	
	x = [ 1 2 3 4 5 6 7 8 9]	; Creates a list
	y = (range 1 10)		; Creates a list = [1 .. 9]
	
	(print (head x) )		; 1
	(print (tail x) ) 		; [2 3 4 5 6 7 8 9]	

	z = (map * x y ) 		; z = [ (* x[0] y[0]) ... (* x[9] y[9]) ]
	(print z)			; [ 1 4 9 16 25 36 49 64 81 ]
	
	w = (fold - 0 [ 1 2 3 4 5] ) 	; w = 1 - (2 - (3 - (4 - (5 - 0)))) = 3 
	
	;Lists are lazy and evaluated when needed
	
	l = [ (* 8 8 ) 3 "Hello"]	;l = [ (* 8 8 ) 3 "Hello"], literally
	p = (head l)			;p = 64
	(print p)			; 64
	
### TODO:
- [ ] FILE I/O applications to set where to print

