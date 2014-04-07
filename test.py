# see http://effbot.org/zone/simple-top-down-parsing.txt

import sys
import re

class literal_token:
	def __init__(self, value):
		self.value = value
	def nud(self):
		return self.value
		
class variable_token:
	var_map = {"(empty)": 0}
	current = "(empty)"
	def __init__(self):
		print variable_token.var_map[variable_token.current], " ", variable_token.current
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

#30-1 allows for right associativity 1^2^3 such that (1^2)^3
class operator_pow_token:
	lbp = 30
	def led(self, left):
		return left ** expression(30-1)

class end_token:
	lbp = 0

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

print getList("3*x+4**y", 5)
'''token
parse("+1")
parse("-1")
parse("10")
parse("1**2**3")
parse("1+2")
parse("1+2+3")
parse("1+2*3")
parse("1*2+3")
parse("1*2/3")
parse("test*2+3")
parse("test*2+3")
#parse("*1") # invalid syntax
'''
