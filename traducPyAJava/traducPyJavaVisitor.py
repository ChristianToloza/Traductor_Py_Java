# Generated from traducPyJava.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .traducPyJavaParser import traducPyJavaParser
else:
    from traducPyJavaParser import traducPyJavaParser

# This class defines a complete generic visitor for a parse tree produced by traducPyJavaParser.

class traducPyJavaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by traducPyJavaParser#programa.
    def visitPrograma(self, ctx:traducPyJavaParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traducPyJavaParser#clase.
    def visitClase(self, ctx:traducPyJavaParser.ClaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traducPyJavaParser#funcion.
    def visitFuncion(self, ctx:traducPyJavaParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traducPyJavaParser#bloque.
    def visitBloque(self, ctx:traducPyJavaParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traducPyJavaParser#declaracion.
    def visitDeclaracion(self, ctx:traducPyJavaParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traducPyJavaParser#parametros.
    def visitParametros(self, ctx:traducPyJavaParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traducPyJavaParser#sentencia.
    def visitSentencia(self, ctx:traducPyJavaParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traducPyJavaParser#if_statement.
    def visitIf_statement(self, ctx:traducPyJavaParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traducPyJavaParser#while_statement.
    def visitWhile_statement(self, ctx:traducPyJavaParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traducPyJavaParser#for_statement.
    def visitFor_statement(self, ctx:traducPyJavaParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traducPyJavaParser#print_statement.
    def visitPrint_statement(self, ctx:traducPyJavaParser.Print_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traducPyJavaParser#return_statement.
    def visitReturn_statement(self, ctx:traducPyJavaParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traducPyJavaParser#expresion.
    def visitExpresion(self, ctx:traducPyJavaParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traducPyJavaParser#importacion.
    def visitImportacion(self, ctx:traducPyJavaParser.ImportacionContext):
        return self.visitChildren(ctx)



del traducPyJavaParser