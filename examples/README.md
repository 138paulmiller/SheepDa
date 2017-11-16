##### Examples
As of now, there are some string processing features that I believe to be somewhat useful.
SheepDa provides basic arithmetic operators such as addition, subtraction, multiplication and division (+ - * /)
The operators can accept numbers as well as strings!
When a string argument is passed, the expression is evaluated differently dependent on the argument types.

For example:
Given msg = "Hello World!123"
Appending the string "World" to the msg. 
	
	res = (+ msg "World")  ;res = "Hello World!123World" 
Appending the number 12.3 to the msg. 
	
	res = (+ msg 12.3)  ;res = "Hello World!12312.3" 
Removing the substring "World" from the msg. 
	
	res = (- msg "World") ;res = "Hello !123" 
Removing the number 12 from msg.
	
	res = (- msg 12) ;res = "Hello World!3" 
Repeating msg 3 times.
	
	res = (* msg 3) ;res = "Hello World!123Hello World!123Hello World!123" 
Removing all instances of "l" and "o" from msg.
	
	res = (/ msg "lo") ;res = "He Wrd!123" 
Removing all instances of "123"from msg.
	
	res = (/ msg 123) ;res = "He Wrd!123" 
