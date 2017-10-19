# SheepDa
## A "Soft" Functional Programming Language based on the Lambda Calculus
Sheepda provides a minimal syntax as a "Soft" introduction to Functional Programming.
Language features closures, dynamic binding and dynamic evaluation with LISP-like syntax. 

#### Usage
./sheepda [<file>|-h]
To use REPL, call without arguments

##### Syntax:
	<stmt>	: <id> = <expr>					// Assignment to idetifier
			| <expr>						// Stand-alone Expression
			| ; <sym> ... \n				// Comment, ends at newline
	<expr>	: \ <param_id> <...> . <expr>	// Defines an abstraction
			| (<expr> <expr> <..>)			// Application
			| <number>						// Integer of Floating point literal
			| <id>							// Identifier
	

### TODO:
	* Add Tuple Primitives
	* Tuple/List construction applications Cons and Car 
	* Add Map and Reduce applications of Tuples
	* Create include file application to load file evaluations into bindings
	* FILE I/O print applications
