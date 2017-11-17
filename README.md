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
	<expr>	: \ <param_id> <...> . <expr>	// Defines an abstraction
		| (<expr> <expr> <..>)		// Applies expressions on the right to the leftmost expression
		| [0-9]+.?[0-9]*		// Integer of Floating point number 
		| [a-zA-Z]+[a-zA-Z0-9]*		// Identifier 
		| "."				// String, anything encapsulated within quotes
	

### TODO:
- [ ] FILE I/O applications to set where to print
- [ ] List construction applications Cons and Car 
- [ ] Add Map and Reduce applications of Lists to enable Table like
- [ ] Create include file application to load file evaluations into bindings

