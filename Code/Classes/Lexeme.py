from decimal import *


class Lexeme:
	def __init__(self, name: str):
		self.Traits: set = set()
		self.Name: str = name
		self.Inners: list = list()


class ValueLexeme(Lexeme):
	def __init__(self, name: str, value):
		super(ValueLexeme, self).__init__(name)
		self.Value = value


class DecimalValueLexeme(Lexeme):
	def __init__(self, name: str, value: Decimal):
		super(DecimalValueLexeme, self).__init__(name)
		self.Value: Decimal = value


class StringValueLexeme(Lexeme):
	def __init__(self, name: str, value: str):
		super(StringValueLexeme, self).__init__(name)
		self.Value: str = value
