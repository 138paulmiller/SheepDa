## SheepDa



s  	: e s				
	| <var> = e s 		// assignment
	| <null>
e 	:	<var>
	|	<num>			// atom
	|	 \ p. e 		// abstraction
	|	(<var> <...> )	// application
# SheepDa - A "Soft" Functional Programming Language

Sheepda provides a minimal syntax as a "Soft" introduction to the Lambda Calculus.

#### Syntax:
	<stmt> 	: <id> = 	
			| <expr>
	<expr>	: \ <param_id> <...> . <expr>  // Defines an abstraction
			| (<expr> <expr> <..>)			//application
			| <number>
			| <var_id>
