# SheepDa

### A Soft Functional Scripting Language
Weak and dynamically typed, statically bound, functional scripting language. Inspired by Lambda calculus with LISP/Scheme like syntax and features.   
##### What do you mean by soft?
The language is very forgiving, and tries its best when operating on varying types. This makes it easier for a programmer to see what happens without running into runtime errors. For instance, what will subtrcating a number from a string mean? SheepDa will implicity cast the number to a string, and remove all instances of the substring. See examples for more use cases.  

#### Usage
See HELP for menu


##### Syntax:
	Each production follows Regex Format 
	Note: Whitespace is ignored, unless in string literal
	id	: [a-zA-Z]+[a-zA-Z0-9]*		// Identifier
	stmt	: id=expr			// Binds expression to identifier
		| expr				// Stand-alone Expression
		| ; .* \n			// Comments, ends at newline
	exprs 	: expr \s exprs
		| expr
	expr	: (\\ id* \. expr )		// Defines an abstraction
		| (expr expr* )			// Applies expressions on the right to the leftmost expression
		| [0-9]+\.?[0-9]*		// Integer of Floating point number 
		| id 
		| \[ exprs \]			// List, Note: exprs are space seperated
		| ".*"				// String, anything encapsulated within quotes


## Built-In Functions
#### Special Form
	(if  a b c)	
	(set i b)	
	(while a b)	
	(import a)
	(exit a)
#### Math
	(+ a b)
	(- a b)
	(* a b)
	(/ a b)
	(% a b)
	(< a b)
	(> a b)
	(eq a b)
	(root a b)
	(exp a b)
	(and a b)
	(or a b)
	(not a)
#### IO
	(print a)
	(read a [b ..] )
#### Type	
	(type a)
	(int a)
	(float a)
	(string a)
	(bool a)
#### List 
	(list a b )
	(range a b)
	(head l)
	(tail l )
	(reverse l )
	(filter f l)
	(fold f a l)
	(map f l1 [l2 ... ]) 



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
- [ ] FILE I/O applications 
- [ ] Derived expression to extend current functionality, such as  case
- [ ] Create a golfing ext - shorten builtin identifiers
