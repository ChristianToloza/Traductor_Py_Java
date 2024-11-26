grammar traducPyJava;

// Lexer Rules
NEWLINE: '\r'? '\n';  // No saltar las líneas
WS: [ \t]+ -> skip;   // Espacios en blanco que no cuentan como indentación

// Palabras clave de Python
DEF: 'def';
RETURN: 'return';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
IN: 'in';
PRINT: 'print';
CLASS: 'class';
IMPORT: 'import';
AND: 'and';
OR: 'or';
NOT: 'not';

// Operadores y Símbolos
ASSIGN: '=';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
EQ: '==';
NEQ: '!=';
LT: '<';
GT: '>';
LEQ: '<=';
GEQ: '>=';

LPAREN: '(';
RPAREN: ')';
LBRACKET: '[';
RBRACKET: ']';
COLON: ':';
COMMA: ',';
DOT: '.';

// Identificadores
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

// Literales
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"' | '\'' .*? '\'';

// Comentarios
COMMENT: '#' ~[\r\n]* -> skip;

// Parser Rules

programa: (importacion | clase | funcion | sentencia)* NEWLINE* EOF;

clase: CLASS IDENTIFIER COLON NEWLINE bloque;

funcion: DEF IDENTIFIER LPAREN parametros? RPAREN COLON NEWLINE bloque;

bloque: (sentencia NEWLINE+)+;  // Controlar que cada sentencia esté seguida de un NEWLINE, sin permitir líneas vacías

declaracion: IDENTIFIER ASSIGN expresion;

parametros: expresion (COMMA expresion)*;  // Ajustado para aceptar más tipos de expresiones, no solo identificadores

sentencia: if_statement
         | while_statement
         | for_statement
         | print_statement
         | return_statement
         | declaracion;

if_statement: IF expresion COLON NEWLINE bloque (ELSE COLON NEWLINE bloque)?;

while_statement: WHILE expresion COLON NEWLINE bloque;

for_statement: FOR IDENTIFIER IN expresion COLON NEWLINE bloque;

print_statement: PRINT LPAREN expresion RPAREN;

return_statement: RETURN expresion;

expresion: expresion (PLUS | MINUS | MULT | DIV | MOD) expresion
         | expresion (EQ | NEQ | LT | GT | LEQ | GEQ) expresion
         | expresion (AND | OR) expresion
         | NOT expresion
         | IDENTIFIER LPAREN parametros? RPAREN  // Manejar llamadas a funciones con parámetros
         | IDENTIFIER
         | INT
         | FLOAT
         | STRING
         | LPAREN expresion RPAREN;  // Expresiones entre paréntesis, útiles para controlar el orden de operaciones

importacion: IMPORT IDENTIFIER;