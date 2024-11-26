from antlr4 import *
from traducPyJavaLexer import traducPyJavaLexer
from traducPyJavaParser import traducPyJavaParser
from TraductorPyJava import TraductorPyJava  # Asegúrate de que el archivo y la clase coincidan

def main():
    # Abrir el archivo de entrada y generar el flujo de entrada
    input_stream = FileStream('prueba.txt')
    
    # Inicializar el lexer y el parser
    lexer = traducPyJavaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = traducPyJavaParser(stream)
    tree = parser.programa()  # Genera el árbol de análisis

    # Traducir usando el visitante
    traductor = TraductorPyJava()
    resultado = traductor.visit(tree)
    
    # Guardar el resultado en un archivo .java
    with open('multi.java', 'w') as salida:
        salida.write(resultado)
    
    print("Traducción completada.")

if __name__ == "__main__":
    main()
