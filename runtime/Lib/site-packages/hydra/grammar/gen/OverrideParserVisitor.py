# Generated from /Users/omry/dev/hydra/hydra/grammar/OverrideParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .OverrideParser import OverrideParser
else:
    from OverrideParser import OverrideParser

# This class defines a complete generic visitor for a parse tree produced by OverrideParser.

class OverrideParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OverrideParser#override.
    def visitOverride(self, ctx:OverrideParser.OverrideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OverrideParser#key.
    def visitKey(self, ctx:OverrideParser.KeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OverrideParser#packageOrGroup.
    def visitPackageOrGroup(self, ctx:OverrideParser.PackageOrGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OverrideParser#package.
    def visitPackage(self, ctx:OverrideParser.PackageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OverrideParser#value.
    def visitValue(self, ctx:OverrideParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OverrideParser#element.
    def visitElement(self, ctx:OverrideParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OverrideParser#simpleChoiceSweep.
    def visitSimpleChoiceSweep(self, ctx:OverrideParser.SimpleChoiceSweepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OverrideParser#argName.
    def visitArgName(self, ctx:OverrideParser.ArgNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OverrideParser#function.
    def visitFunction(self, ctx:OverrideParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OverrideParser#listValue.
    def visitListValue(self, ctx:OverrideParser.ListValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OverrideParser#dictValue.
    def visitDictValue(self, ctx:OverrideParser.DictValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OverrideParser#dictKeyValuePair.
    def visitDictKeyValuePair(self, ctx:OverrideParser.DictKeyValuePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OverrideParser#primitive.
    def visitPrimitive(self, ctx:OverrideParser.PrimitiveContext):
        return self.visitChildren(ctx)



del OverrideParser