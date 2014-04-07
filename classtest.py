class symbol_base(object):

	id = None
	value = None
	first = second = None

	def nud(self):
		raise SyntaxError("Syntax error (%r)." % self.id)

	def led(self, left):
		raise SyntaxError("Unknown operator (%r)." % self.id)

	def __repr__(self):
		if self.id == "(name)" or self.id == "(literal)":
			return "(%s %s)" % (self.id[1:-1], self.value)
		out = [self.id, self.first, self.second, self.third]
		out = map(str, filter(None, out))
		return "(" + " ".join(out) + ")"
		
def symbol(id, bp=0):
	try:
		s = symbol_table[id]
	except KeyError:
		class s(symbol_base):
			pass
		s.__name__ = "symbol-" + id # for debugging
		s.id = id
		s.value = None
		s.lbp = bp
		symbol_table[id] = s
	else:
		s.lbp = max(bp, s.lbp)
	return s
