# SheepDa
## A "Soft" Functional Programming Language based on the Lambda Calculus

Sheepda provides a minimal syntax as a "Soft" introduction to Functional Programming.

#### Syntax:
	<stmt> 	: <id> = 	
			| <expr>
	<expr>	: \ <param_id> <...> . <expr>  // Defines an abstraction
			| (<expr> <expr> <..>)			//application
			| <number>
			| <var_id>
