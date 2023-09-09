# Generated from /Users/omry/dev/hydra/hydra/grammar/OverrideParser.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\33")
        buf.write("\u009c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\2\5\2 \n\2\3\2\3\2\3\2\3\2\5\2&\n\2\5")
        buf.write("\2(\n\2\3\2\3\2\3\2\3\2\5\2.\n\2\5\2\60\n\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\5\3:\n\3\3\3\3\3\3\3\3\3\5\3@\n")
        buf.write("\3\3\4\3\4\3\4\3\4\6\4F\n\4\r\4\16\4G\5\4J\n\4\3\5\3\5")
        buf.write("\3\6\3\6\5\6P\n\6\3\7\3\7\3\7\3\7\5\7V\n\7\3\b\3\b\3\b")
        buf.write("\6\b[\n\b\r\b\16\b\\\3\t\3\t\3\t\3\n\3\n\3\n\5\ne\n\n")
        buf.write("\3\n\3\n\3\n\5\nj\n\n\3\n\7\nm\n\n\f\n\16\np\13\n\5\n")
        buf.write("r\n\n\3\n\3\n\3\13\3\13\3\13\3\13\7\13z\n\13\f\13\16\13")
        buf.write("}\13\13\5\13\177\n\13\3\13\3\13\3\f\3\f\3\f\3\f\7\f\u0087")
        buf.write("\n\f\f\f\16\f\u008a\13\f\5\f\u008c\n\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\6\16\u0096\n\16\r\16\16\16\u0097\5")
        buf.write("\16\u009a\n\16\3\16\2\2\17\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\2\4\4\2\n\n\27\27\5\2\7\7\22\31\33\33\2\u00a8\2")
        buf.write("/\3\2\2\2\4?\3\2\2\2\6I\3\2\2\2\bK\3\2\2\2\nO\3\2\2\2")
        buf.write("\fU\3\2\2\2\16W\3\2\2\2\20^\3\2\2\2\22a\3\2\2\2\24u\3")
        buf.write("\2\2\2\26\u0082\3\2\2\2\30\u008f\3\2\2\2\32\u0099\3\2")
        buf.write("\2\2\34\35\5\4\3\2\35\37\7\3\2\2\36 \5\n\6\2\37\36\3\2")
        buf.write("\2\2\37 \3\2\2\2 \60\3\2\2\2!\"\7\4\2\2\"\'\5\4\3\2#%")
        buf.write("\7\3\2\2$&\5\n\6\2%$\3\2\2\2%&\3\2\2\2&(\3\2\2\2\'#\3")
        buf.write("\2\2\2\'(\3\2\2\2(\60\3\2\2\2)*\7\5\2\2*+\5\4\3\2+-\7")
        buf.write("\3\2\2,.\5\n\6\2-,\3\2\2\2-.\3\2\2\2.\60\3\2\2\2/\34\3")
        buf.write("\2\2\2/!\3\2\2\2/)\3\2\2\2\60\61\3\2\2\2\61\62\7\2\2\3")
        buf.write("\62\3\3\2\2\2\63@\5\6\4\2\64\65\5\6\4\2\65\66\7\6\2\2")
        buf.write("\669\5\b\5\2\678\7\7\2\28:\5\b\5\29\67\3\2\2\29:\3\2\2")
        buf.write("\2:@\3\2\2\2;<\5\6\4\2<=\7\b\2\2=>\5\b\5\2>@\3\2\2\2?")
        buf.write("\63\3\2\2\2?\64\3\2\2\2?;\3\2\2\2@\5\3\2\2\2AJ\5\b\5\2")
        buf.write("BE\7\27\2\2CD\7\t\2\2DF\7\27\2\2EC\3\2\2\2FG\3\2\2\2G")
        buf.write("E\3\2\2\2GH\3\2\2\2HJ\3\2\2\2IA\3\2\2\2IB\3\2\2\2J\7\3")
        buf.write("\2\2\2KL\t\2\2\2L\t\3\2\2\2MP\5\f\7\2NP\5\16\b\2OM\3\2")
        buf.write("\2\2ON\3\2\2\2P\13\3\2\2\2QV\5\32\16\2RV\5\24\13\2SV\5")
        buf.write("\26\f\2TV\5\22\n\2UQ\3\2\2\2UR\3\2\2\2US\3\2\2\2UT\3\2")
        buf.write("\2\2V\r\3\2\2\2WZ\5\f\7\2XY\7\f\2\2Y[\5\f\7\2ZX\3\2\2")
        buf.write("\2[\\\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]\17\3\2\2\2^_\7\27")
        buf.write("\2\2_`\7\3\2\2`\21\3\2\2\2ab\7\27\2\2bq\7\13\2\2ce\5\20")
        buf.write("\t\2dc\3\2\2\2de\3\2\2\2ef\3\2\2\2fn\5\f\7\2gi\7\f\2\2")
        buf.write("hj\5\20\t\2ih\3\2\2\2ij\3\2\2\2jk\3\2\2\2km\5\f\7\2lg")
        buf.write("\3\2\2\2mp\3\2\2\2nl\3\2\2\2no\3\2\2\2or\3\2\2\2pn\3\2")
        buf.write("\2\2qd\3\2\2\2qr\3\2\2\2rs\3\2\2\2st\7\r\2\2t\23\3\2\2")
        buf.write("\2u~\7\16\2\2v{\5\f\7\2wx\7\f\2\2xz\5\f\7\2yw\3\2\2\2")
        buf.write("z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|\177\3\2\2\2}{\3\2\2\2")
        buf.write("~v\3\2\2\2~\177\3\2\2\2\177\u0080\3\2\2\2\u0080\u0081")
        buf.write("\7\17\2\2\u0081\25\3\2\2\2\u0082\u008b\7\20\2\2\u0083")
        buf.write("\u0088\5\30\r\2\u0084\u0085\7\f\2\2\u0085\u0087\5\30\r")
        buf.write("\2\u0086\u0084\3\2\2\2\u0087\u008a\3\2\2\2\u0088\u0086")
        buf.write("\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008c\3\2\2\2\u008a")
        buf.write("\u0088\3\2\2\2\u008b\u0083\3\2\2\2\u008b\u008c\3\2\2\2")
        buf.write("\u008c\u008d\3\2\2\2\u008d\u008e\7\21\2\2\u008e\27\3\2")
        buf.write("\2\2\u008f\u0090\7\27\2\2\u0090\u0091\7\7\2\2\u0091\u0092")
        buf.write("\5\f\7\2\u0092\31\3\2\2\2\u0093\u009a\7\32\2\2\u0094\u0096")
        buf.write("\t\3\2\2\u0095\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097")
        buf.write("\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u009a\3\2\2\2")
        buf.write("\u0099\u0093\3\2\2\2\u0099\u0095\3\2\2\2\u009a\33\3\2")
        buf.write("\2\2\30\37%\'-/9?GIOU\\dinq{~\u0088\u008b\u0097\u0099")
        return buf.getvalue()


class OverrideParser ( Parser ):

    grammarFileName = "OverrideParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'~'", "'+'", "'@'", "':'", 
                     "'@:'", "'/'" ]

    symbolicNames = [ "<INVALID>", "EQUAL", "TILDE", "PLUS", "AT", "COLON", 
                      "ATCOLON", "SLASH", "DOT_PATH", "POPEN", "COMMA", 
                      "PCLOSE", "BRACKET_OPEN", "BRACKET_CLOSE", "BRACE_OPEN", 
                      "BRACE_CLOSE", "FLOAT", "INT", "BOOL", "NULL", "UNQUOTED_CHAR", 
                      "ID", "ESC", "WS", "QUOTED_VALUE", "INTERPOLATION" ]

    RULE_override = 0
    RULE_key = 1
    RULE_packageOrGroup = 2
    RULE_package = 3
    RULE_value = 4
    RULE_element = 5
    RULE_simpleChoiceSweep = 6
    RULE_argName = 7
    RULE_function = 8
    RULE_listValue = 9
    RULE_dictValue = 10
    RULE_dictKeyValuePair = 11
    RULE_primitive = 12

    ruleNames =  [ "override", "key", "packageOrGroup", "package", "value", 
                   "element", "simpleChoiceSweep", "argName", "function", 
                   "listValue", "dictValue", "dictKeyValuePair", "primitive" ]

    EOF = Token.EOF
    EQUAL=1
    TILDE=2
    PLUS=3
    AT=4
    COLON=5
    ATCOLON=6
    SLASH=7
    DOT_PATH=8
    POPEN=9
    COMMA=10
    PCLOSE=11
    BRACKET_OPEN=12
    BRACKET_CLOSE=13
    BRACE_OPEN=14
    BRACE_CLOSE=15
    FLOAT=16
    INT=17
    BOOL=18
    NULL=19
    UNQUOTED_CHAR=20
    ID=21
    ESC=22
    WS=23
    QUOTED_VALUE=24
    INTERPOLATION=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class OverrideContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(OverrideParser.EOF, 0)

        def key(self):
            return self.getTypedRuleContext(OverrideParser.KeyContext,0)


        def EQUAL(self):
            return self.getToken(OverrideParser.EQUAL, 0)

        def TILDE(self):
            return self.getToken(OverrideParser.TILDE, 0)

        def PLUS(self):
            return self.getToken(OverrideParser.PLUS, 0)

        def value(self):
            return self.getTypedRuleContext(OverrideParser.ValueContext,0)


        def getRuleIndex(self):
            return OverrideParser.RULE_override

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOverride" ):
                listener.enterOverride(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOverride" ):
                listener.exitOverride(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOverride" ):
                return visitor.visitOverride(self)
            else:
                return visitor.visitChildren(self)




    def override(self):

        localctx = OverrideParser.OverrideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_override)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OverrideParser.DOT_PATH, OverrideParser.ID]:
                self.state = 26
                self.key()
                self.state = 27
                self.match(OverrideParser.EQUAL)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OverrideParser.COLON) | (1 << OverrideParser.BRACKET_OPEN) | (1 << OverrideParser.BRACE_OPEN) | (1 << OverrideParser.FLOAT) | (1 << OverrideParser.INT) | (1 << OverrideParser.BOOL) | (1 << OverrideParser.NULL) | (1 << OverrideParser.UNQUOTED_CHAR) | (1 << OverrideParser.ID) | (1 << OverrideParser.ESC) | (1 << OverrideParser.WS) | (1 << OverrideParser.QUOTED_VALUE) | (1 << OverrideParser.INTERPOLATION))) != 0):
                    self.state = 28
                    self.value()


                pass
            elif token in [OverrideParser.TILDE]:
                self.state = 31
                self.match(OverrideParser.TILDE)
                self.state = 32
                self.key()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==OverrideParser.EQUAL:
                    self.state = 33
                    self.match(OverrideParser.EQUAL)
                    self.state = 35
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OverrideParser.COLON) | (1 << OverrideParser.BRACKET_OPEN) | (1 << OverrideParser.BRACE_OPEN) | (1 << OverrideParser.FLOAT) | (1 << OverrideParser.INT) | (1 << OverrideParser.BOOL) | (1 << OverrideParser.NULL) | (1 << OverrideParser.UNQUOTED_CHAR) | (1 << OverrideParser.ID) | (1 << OverrideParser.ESC) | (1 << OverrideParser.WS) | (1 << OverrideParser.QUOTED_VALUE) | (1 << OverrideParser.INTERPOLATION))) != 0):
                        self.state = 34
                        self.value()




                pass
            elif token in [OverrideParser.PLUS]:
                self.state = 39
                self.match(OverrideParser.PLUS)
                self.state = 40
                self.key()
                self.state = 41
                self.match(OverrideParser.EQUAL)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OverrideParser.COLON) | (1 << OverrideParser.BRACKET_OPEN) | (1 << OverrideParser.BRACE_OPEN) | (1 << OverrideParser.FLOAT) | (1 << OverrideParser.INT) | (1 << OverrideParser.BOOL) | (1 << OverrideParser.NULL) | (1 << OverrideParser.UNQUOTED_CHAR) | (1 << OverrideParser.ID) | (1 << OverrideParser.ESC) | (1 << OverrideParser.WS) | (1 << OverrideParser.QUOTED_VALUE) | (1 << OverrideParser.INTERPOLATION))) != 0):
                    self.state = 42
                    self.value()


                pass
            else:
                raise NoViableAltException(self)

            self.state = 47
            self.match(OverrideParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def packageOrGroup(self):
            return self.getTypedRuleContext(OverrideParser.PackageOrGroupContext,0)


        def AT(self):
            return self.getToken(OverrideParser.AT, 0)

        def package(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OverrideParser.PackageContext)
            else:
                return self.getTypedRuleContext(OverrideParser.PackageContext,i)


        def COLON(self):
            return self.getToken(OverrideParser.COLON, 0)

        def ATCOLON(self):
            return self.getToken(OverrideParser.ATCOLON, 0)

        def getRuleIndex(self):
            return OverrideParser.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey" ):
                return visitor.visitKey(self)
            else:
                return visitor.visitChildren(self)




    def key(self):

        localctx = OverrideParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_key)
        self._la = 0 # Token type
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.packageOrGroup()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.packageOrGroup()
                self.state = 51
                self.match(OverrideParser.AT)
                self.state = 52
                self.package()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==OverrideParser.COLON:
                    self.state = 53
                    self.match(OverrideParser.COLON)
                    self.state = 54
                    self.package()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.packageOrGroup()
                self.state = 58
                self.match(OverrideParser.ATCOLON)
                self.state = 59
                self.package()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PackageOrGroupContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def package(self):
            return self.getTypedRuleContext(OverrideParser.PackageContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(OverrideParser.ID)
            else:
                return self.getToken(OverrideParser.ID, i)

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(OverrideParser.SLASH)
            else:
                return self.getToken(OverrideParser.SLASH, i)

        def getRuleIndex(self):
            return OverrideParser.RULE_packageOrGroup

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackageOrGroup" ):
                listener.enterPackageOrGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackageOrGroup" ):
                listener.exitPackageOrGroup(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPackageOrGroup" ):
                return visitor.visitPackageOrGroup(self)
            else:
                return visitor.visitChildren(self)




    def packageOrGroup(self):

        localctx = OverrideParser.PackageOrGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_packageOrGroup)
        self._la = 0 # Token type
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.package()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(OverrideParser.ID)
                self.state = 67 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 65
                    self.match(OverrideParser.SLASH)
                    self.state = 66
                    self.match(OverrideParser.ID)
                    self.state = 69 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==OverrideParser.SLASH):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PackageContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OverrideParser.ID, 0)

        def DOT_PATH(self):
            return self.getToken(OverrideParser.DOT_PATH, 0)

        def getRuleIndex(self):
            return OverrideParser.RULE_package

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackage" ):
                listener.enterPackage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackage" ):
                listener.exitPackage(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPackage" ):
                return visitor.visitPackage(self)
            else:
                return visitor.visitChildren(self)




    def package(self):

        localctx = OverrideParser.PackageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_package)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            _la = self._input.LA(1)
            if not(_la==OverrideParser.DOT_PATH or _la==OverrideParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(OverrideParser.ElementContext,0)


        def simpleChoiceSweep(self):
            return self.getTypedRuleContext(OverrideParser.SimpleChoiceSweepContext,0)


        def getRuleIndex(self):
            return OverrideParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = OverrideParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.simpleChoiceSweep()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive(self):
            return self.getTypedRuleContext(OverrideParser.PrimitiveContext,0)


        def listValue(self):
            return self.getTypedRuleContext(OverrideParser.ListValueContext,0)


        def dictValue(self):
            return self.getTypedRuleContext(OverrideParser.DictValueContext,0)


        def function(self):
            return self.getTypedRuleContext(OverrideParser.FunctionContext,0)


        def getRuleIndex(self):
            return OverrideParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = OverrideParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_element)
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.primitive()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.listValue()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.dictValue()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 82
                self.function()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleChoiceSweepContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OverrideParser.ElementContext)
            else:
                return self.getTypedRuleContext(OverrideParser.ElementContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(OverrideParser.COMMA)
            else:
                return self.getToken(OverrideParser.COMMA, i)

        def getRuleIndex(self):
            return OverrideParser.RULE_simpleChoiceSweep

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleChoiceSweep" ):
                listener.enterSimpleChoiceSweep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleChoiceSweep" ):
                listener.exitSimpleChoiceSweep(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleChoiceSweep" ):
                return visitor.visitSimpleChoiceSweep(self)
            else:
                return visitor.visitChildren(self)




    def simpleChoiceSweep(self):

        localctx = OverrideParser.SimpleChoiceSweepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_simpleChoiceSweep)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.element()
            self.state = 88 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 86
                self.match(OverrideParser.COMMA)
                self.state = 87
                self.element()
                self.state = 90 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==OverrideParser.COMMA):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OverrideParser.ID, 0)

        def EQUAL(self):
            return self.getToken(OverrideParser.EQUAL, 0)

        def getRuleIndex(self):
            return OverrideParser.RULE_argName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgName" ):
                listener.enterArgName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgName" ):
                listener.exitArgName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgName" ):
                return visitor.visitArgName(self)
            else:
                return visitor.visitChildren(self)




    def argName(self):

        localctx = OverrideParser.ArgNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_argName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(OverrideParser.ID)
            self.state = 93
            self.match(OverrideParser.EQUAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OverrideParser.ID, 0)

        def POPEN(self):
            return self.getToken(OverrideParser.POPEN, 0)

        def PCLOSE(self):
            return self.getToken(OverrideParser.PCLOSE, 0)

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OverrideParser.ElementContext)
            else:
                return self.getTypedRuleContext(OverrideParser.ElementContext,i)


        def argName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OverrideParser.ArgNameContext)
            else:
                return self.getTypedRuleContext(OverrideParser.ArgNameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(OverrideParser.COMMA)
            else:
                return self.getToken(OverrideParser.COMMA, i)

        def getRuleIndex(self):
            return OverrideParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = OverrideParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(OverrideParser.ID)
            self.state = 96
            self.match(OverrideParser.POPEN)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OverrideParser.COLON) | (1 << OverrideParser.BRACKET_OPEN) | (1 << OverrideParser.BRACE_OPEN) | (1 << OverrideParser.FLOAT) | (1 << OverrideParser.INT) | (1 << OverrideParser.BOOL) | (1 << OverrideParser.NULL) | (1 << OverrideParser.UNQUOTED_CHAR) | (1 << OverrideParser.ID) | (1 << OverrideParser.ESC) | (1 << OverrideParser.WS) | (1 << OverrideParser.QUOTED_VALUE) | (1 << OverrideParser.INTERPOLATION))) != 0):
                self.state = 98
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 97
                    self.argName()


                self.state = 100
                self.element()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==OverrideParser.COMMA:
                    self.state = 101
                    self.match(OverrideParser.COMMA)
                    self.state = 103
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        self.state = 102
                        self.argName()


                    self.state = 105
                    self.element()
                    self.state = 110
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 113
            self.match(OverrideParser.PCLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACKET_OPEN(self):
            return self.getToken(OverrideParser.BRACKET_OPEN, 0)

        def BRACKET_CLOSE(self):
            return self.getToken(OverrideParser.BRACKET_CLOSE, 0)

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OverrideParser.ElementContext)
            else:
                return self.getTypedRuleContext(OverrideParser.ElementContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(OverrideParser.COMMA)
            else:
                return self.getToken(OverrideParser.COMMA, i)

        def getRuleIndex(self):
            return OverrideParser.RULE_listValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListValue" ):
                listener.enterListValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListValue" ):
                listener.exitListValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListValue" ):
                return visitor.visitListValue(self)
            else:
                return visitor.visitChildren(self)




    def listValue(self):

        localctx = OverrideParser.ListValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_listValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(OverrideParser.BRACKET_OPEN)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OverrideParser.COLON) | (1 << OverrideParser.BRACKET_OPEN) | (1 << OverrideParser.BRACE_OPEN) | (1 << OverrideParser.FLOAT) | (1 << OverrideParser.INT) | (1 << OverrideParser.BOOL) | (1 << OverrideParser.NULL) | (1 << OverrideParser.UNQUOTED_CHAR) | (1 << OverrideParser.ID) | (1 << OverrideParser.ESC) | (1 << OverrideParser.WS) | (1 << OverrideParser.QUOTED_VALUE) | (1 << OverrideParser.INTERPOLATION))) != 0):
                self.state = 116
                self.element()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==OverrideParser.COMMA:
                    self.state = 117
                    self.match(OverrideParser.COMMA)
                    self.state = 118
                    self.element()
                    self.state = 123
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 126
            self.match(OverrideParser.BRACKET_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DictValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACE_OPEN(self):
            return self.getToken(OverrideParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(OverrideParser.BRACE_CLOSE, 0)

        def dictKeyValuePair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OverrideParser.DictKeyValuePairContext)
            else:
                return self.getTypedRuleContext(OverrideParser.DictKeyValuePairContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(OverrideParser.COMMA)
            else:
                return self.getToken(OverrideParser.COMMA, i)

        def getRuleIndex(self):
            return OverrideParser.RULE_dictValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDictValue" ):
                listener.enterDictValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDictValue" ):
                listener.exitDictValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDictValue" ):
                return visitor.visitDictValue(self)
            else:
                return visitor.visitChildren(self)




    def dictValue(self):

        localctx = OverrideParser.DictValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_dictValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(OverrideParser.BRACE_OPEN)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OverrideParser.ID:
                self.state = 129
                self.dictKeyValuePair()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==OverrideParser.COMMA:
                    self.state = 130
                    self.match(OverrideParser.COMMA)
                    self.state = 131
                    self.dictKeyValuePair()
                    self.state = 136
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 139
            self.match(OverrideParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DictKeyValuePairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OverrideParser.ID, 0)

        def COLON(self):
            return self.getToken(OverrideParser.COLON, 0)

        def element(self):
            return self.getTypedRuleContext(OverrideParser.ElementContext,0)


        def getRuleIndex(self):
            return OverrideParser.RULE_dictKeyValuePair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDictKeyValuePair" ):
                listener.enterDictKeyValuePair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDictKeyValuePair" ):
                listener.exitDictKeyValuePair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDictKeyValuePair" ):
                return visitor.visitDictKeyValuePair(self)
            else:
                return visitor.visitChildren(self)




    def dictKeyValuePair(self):

        localctx = OverrideParser.DictKeyValuePairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_dictKeyValuePair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(OverrideParser.ID)
            self.state = 142
            self.match(OverrideParser.COLON)
            self.state = 143
            self.element()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUOTED_VALUE(self):
            return self.getToken(OverrideParser.QUOTED_VALUE, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(OverrideParser.ID)
            else:
                return self.getToken(OverrideParser.ID, i)

        def NULL(self, i:int=None):
            if i is None:
                return self.getTokens(OverrideParser.NULL)
            else:
                return self.getToken(OverrideParser.NULL, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(OverrideParser.INT)
            else:
                return self.getToken(OverrideParser.INT, i)

        def FLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(OverrideParser.FLOAT)
            else:
                return self.getToken(OverrideParser.FLOAT, i)

        def BOOL(self, i:int=None):
            if i is None:
                return self.getTokens(OverrideParser.BOOL)
            else:
                return self.getToken(OverrideParser.BOOL, i)

        def INTERPOLATION(self, i:int=None):
            if i is None:
                return self.getTokens(OverrideParser.INTERPOLATION)
            else:
                return self.getToken(OverrideParser.INTERPOLATION, i)

        def UNQUOTED_CHAR(self, i:int=None):
            if i is None:
                return self.getTokens(OverrideParser.UNQUOTED_CHAR)
            else:
                return self.getToken(OverrideParser.UNQUOTED_CHAR, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(OverrideParser.COLON)
            else:
                return self.getToken(OverrideParser.COLON, i)

        def ESC(self, i:int=None):
            if i is None:
                return self.getTokens(OverrideParser.ESC)
            else:
                return self.getToken(OverrideParser.ESC, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(OverrideParser.WS)
            else:
                return self.getToken(OverrideParser.WS, i)

        def getRuleIndex(self):
            return OverrideParser.RULE_primitive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitive" ):
                listener.enterPrimitive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitive" ):
                listener.exitPrimitive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive" ):
                return visitor.visitPrimitive(self)
            else:
                return visitor.visitChildren(self)




    def primitive(self):

        localctx = OverrideParser.PrimitiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_primitive)
        self._la = 0 # Token type
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OverrideParser.QUOTED_VALUE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.match(OverrideParser.QUOTED_VALUE)
                pass
            elif token in [OverrideParser.COLON, OverrideParser.FLOAT, OverrideParser.INT, OverrideParser.BOOL, OverrideParser.NULL, OverrideParser.UNQUOTED_CHAR, OverrideParser.ID, OverrideParser.ESC, OverrideParser.WS, OverrideParser.INTERPOLATION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 147 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 146
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OverrideParser.COLON) | (1 << OverrideParser.FLOAT) | (1 << OverrideParser.INT) | (1 << OverrideParser.BOOL) | (1 << OverrideParser.NULL) | (1 << OverrideParser.UNQUOTED_CHAR) | (1 << OverrideParser.ID) | (1 << OverrideParser.ESC) | (1 << OverrideParser.WS) | (1 << OverrideParser.INTERPOLATION))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 149 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OverrideParser.COLON) | (1 << OverrideParser.FLOAT) | (1 << OverrideParser.INT) | (1 << OverrideParser.BOOL) | (1 << OverrideParser.NULL) | (1 << OverrideParser.UNQUOTED_CHAR) | (1 << OverrideParser.ID) | (1 << OverrideParser.ESC) | (1 << OverrideParser.WS) | (1 << OverrideParser.INTERPOLATION))) != 0)):
                        break

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





