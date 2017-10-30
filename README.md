# SheepDa
### A Soft Functional Scripting Language
Sheepda provides a minimal syntax as a "Soft" introduction to Functional Programming concepts.
Language features closures, dynamic binding, static scoping, and lazy evaluation with a syntax mixture of LISP and Lamba-Calculus. 

#### Usage
See HELP for menu


##### Why?
This project started out as a small toy language to help programmers quickly understand fundamental functional programming concepts such as first-class functions, immutability and lazy-evaluation. 

However, I plan to add many features to help provide programmers with a large enough toolset to transition this toy into a general purpose language. 

Learning SheepDa should be much easier than most languages. 
Below is the Grammar/Syntax of the language. Notice that there are only statements and expressions!


##### Syntax:
	<stmt>	: <id> = <expr>					// Assignment to idetifier
			| <expr>						// Stand-alone Expression
			| ; <sym> ... \n				// Comment, ends at newline
	<expr>	: \ <param_id> <...> . <expr>	// Defines an abstraction
			| (<expr> <expr> <..>)			// Application
			| <number>						// Integer of Floating point literal
			| <id>							// Identifier
			| "<string>"
	

### TODO:
	- [] FILE I/O applications to set where to print
	- [] List construction applications Cons and Car 
	- [] Add Map and Reduce applications of Lists to enable Table like
	- [] Create include file application to load file evaluations into bindings
