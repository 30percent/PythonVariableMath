# see http://effbot.org/zone/simple-top-down-parsing.txt

import sys
import re
from methodsclassestobeincluded import *
import inspect

class literal_token:
        def __init__(self, value):
                self.value = value
        def nud(self):
                return self.value
                
class variable_token:
        var_map = {"(empty)": 0}
        current = "(empty)"

        @staticmethod
        def include(value):
                try:
                        variable_token.var_map[value] += 1
                        variable_token.current = value
                except KeyError:
                        variable_token.var_map[value] = 0
                        variable_token.current = value
        def nud(self):
                
                return variable_token.var_map[variable_token.current]

class operator_add_token:
        lbp = 10
        def nud(self):
                return expression(100)
        def led(self, left):
                return left + expression(10)

class operator_sub_token:
        lbp = 10
        def nud(self):
                return -expression(100)
        def led(self, left):
                return left - expression(10)

class operator_mul_token:
        lbp = 20
        def led(self, left):
                return left * expression(20)

class operator_div_token:
        lbp = 20
        def led(self, left):
                return left / expression(20)

#30-1 allows for right associativity 1^2^3 such that 1^(2^3)
class operator_pow_token:
        lbp = 30
        def led(self, left):
                return left ** expression(30-1)

class operator_rparen_token:
        lbp = 0

class end_token:
        lbp = 0

class operator_lparen_token:
        lbp = 150

        def nud(self):
                expr = expression()
                advance()
                return expr

def advance():
        global token
        if isinstance(token, operator_rparen_token):
                token = next()
        else:
                raise SyntaxError("Syntax Error. Open Parens without close.")
        
def tokenize_python(program):
        import tokenize
        from cStringIO import StringIO
        type_map = {
                tokenize.NUMBER: "(literal)",
                tokenize.STRING: "(literal)",
                tokenize.OP: "(operator)",
                tokenize.NAME: "(name)",
                }
        for t in tokenize.generate_tokens(StringIO(program).next):
                try:
                        yield type_map[t[0]], t[1]
                except KeyError:
                        if t[0] == tokenize.ENDMARKER:
                                break
                        else:
                                raise SyntaxError("Syntax Error")
        #yield "(end)", "(end)"

def tokenize(program):
        #for number, operator in re.findall("\s*(?:(\d+)|(\*\*|.))", program):
        for ident, value in tokenize_python(program):
                if ident == "(literal)":
                        yield literal_token(int(value))
                elif ident == "(name)":
                        variable_token.include(value)
                        yield variable_token()
                elif ident =="(operator)":
                        if value == "+":
                                yield operator_add_token()
                        elif value == "-":
                                yield operator_sub_token()
                        elif value == "*":
                                yield operator_mul_token()
                        elif value == "/":
                                yield operator_div_token()
                        elif value == "**":
                                yield operator_pow_token()
                        elif value == "(":
                                yield operator_lparen_token()
                        elif value == ")":
                                yield operator_rparen_token()
                        else:
                                raise SyntaxError("Unknown operator: %r" % value)
                elif ident == "(end)":
                        yield end_token()
                else:
                        raise SyntaxError("unknown operator: %r" % value)
        yield end_token()


def expression(rbp=0):
        global token
        t = token
        token = next()
        left = t.nud()
        while rbp < token.lbp:
                t = token
                token = next()
                left = t.led(left)
        return left

def parse(program):
        global token, next
        next = tokenize(program).next
        token = next()
        val = expression()
        return val

def getList(expression, iteration):
        group = []
        for x in range(0, iteration):
                group.append(parse(expression))
        return group

if 1:
        
        myBKey = Key('B', Key.MajorKey)
        myCKey = Key('C', Key.MajorKey)
        print myCKey.getScale()
        
        li = getList("((1+5)*x) + 1", 12)
        print li
        sto = generateModValuePair(li)
        print sto
        li2 = [int(i[0]) for i in sto]
        #print [int(i[1]) for i in sto]
        li3 = listToNoteDuration([int(i[1]) for i in sto])
        li2 = createNoteList(li2, myBKey)
        print li2, "\n", li3
        
