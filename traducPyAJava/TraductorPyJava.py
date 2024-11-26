from traducPyJavaVisitor import traducPyJavaVisitor  # Importar el Visitor generado
from traducPyJavaParser import traducPyJavaParser  # Importar el Parser generado

class TraductorPyJava(traducPyJavaVisitor):
    def __init__(self):
        self.resultado = ""
        self.indent_level = 0  # Nivel de indentación

    # Función para generar la indentación
    def get_indent(self):
        return "    " * self.indent_level  # 4 espacios por nivel de indentación

    # Visita de una función
    def visitFuncion(self, ctx:traducPyJavaParser.FuncionContext):
        nombre_funcion = ctx.IDENTIFIER().getText()
        parametros = self.visit(ctx.parametros()) if ctx.parametros() else ""
        
        # Generar el método con indentación
        funcion = f"{self.get_indent()}public static int {nombre_funcion}({parametros}) " + "{\n"
        self.indent_level += 1  # Aumentar el nivel de indentación
        funcion += self.visit(ctx.bloque())  # Generar el bloque de código de la función
        self.indent_level -= 1  # Reducir el nivel de indentación
        funcion += f"{self.get_indent()}}}\n"  # Cerrar el bloque correctamente con }}
        return funcion

    # Visita de los parámetros
    def visitParametros(self, ctx:traducPyJavaParser.ParametrosContext):
        parametros = []
        for expr in ctx.expresion():
            parametros.append(f"int {self.visit(expr)}")  # Asumimos int como tipo de parámetro
        return ", ".join(parametros)

    # Visita de una declaración (asignación de variables)
    def visitDeclaracion(self, ctx:traducPyJavaParser.DeclaracionContext):
        variable = ctx.IDENTIFIER().getText()  # Obtener el nombre de la variable
        expresion = self.visit(ctx.expresion())  # Obtener la expresión asignada
        return f"{self.get_indent()}int {variable} = {expresion};\n"  # Traducir la asignación en Java

    # Visita del bloque de código
    def visitBloque(self, ctx:traducPyJavaParser.BloqueContext):
        bloque = ""
        for sentencia in ctx.sentencia():
            bloque += self.visit(sentencia)  # Cada sentencia se maneja con la indentación correcta
        return bloque

    # Visita de una expresión
    def visitExpresion(self, ctx:traducPyJavaParser.ExpresionContext):
        if ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        elif ctx.INT():
            return ctx.INT().getText()
        elif ctx.PLUS():
            return f"{self.visit(ctx.expresion(0))} + {self.visit(ctx.expresion(1))}"
        elif ctx.MINUS():
            return f"{self.visit(ctx.expresion(0))} - {self.visit(ctx.expresion(1))}"
        elif ctx.MULT():
            return f"{self.visit(ctx.expresion(0))} * {self.visit(ctx.expresion(1))}"
        elif ctx.DIV():
            return f"{self.visit(ctx.expresion(0))} / {self.visit(ctx.expresion(1))}"
        else:
            return ""

    # Visita de la sentencia 'return'
    def visitReturn_statement(self, ctx:traducPyJavaParser.Return_statementContext):
        expresion = self.visit(ctx.expresion())
        return f"{self.get_indent()}return {expresion};\n"  # Agregar indentación a return

    # Visita de la sentencia 'print'
    def visitPrint_statement(self, ctx:traducPyJavaParser.Print_statementContext):
        expresion = self.visit(ctx.expresion())
        return f"{self.get_indent()}System.out.println({expresion});\n"  # Agregar indentación a print

    # Visita del programa (estructura global)
    def visitPrograma(self, ctx:traducPyJavaParser.ProgramaContext):
        # Inicializar el resultado con la clase y agregar indentación
        self.resultado = "public class Main {\n"
        self.indent_level += 1  # Aumentar la indentación para el cuerpo de la clase
        
        # Generar todas las funciones
        for funcion in ctx.funcion():
            self.resultado += self.visit(funcion)
        
        # Generar el método main
        self.resultado += f"{self.get_indent()}public static void main(String[] args) {{\n"
        self.indent_level += 1  # Aumentar la indentación para el cuerpo del main
        for sentencia in ctx.sentencia():
            self.resultado += self.visit(sentencia)
        self.indent_level -= 1  # Reducir la indentación al cerrar el main
        self.resultado += f"{self.get_indent()}}}\n"  # Cerrar el método main correctamente con }}
        
        self.indent_level -= 1  # Reducir la indentación al cerrar la clase
        self.resultado += "}\n"  # Cerrar la clase
        return self.resultado
