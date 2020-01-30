from Code.Classes.Lexeme import *
from Data.Constants import RegExps

from typing import List, Callable
import re


class Lexer:
	def __init__(self):
		self.BasicLexT: List[str] = list()
		self.BasicLexH: List[Callable[[re.match], Lexeme]] = list()

		self.OpeningLexT: List[str] = list()
		self.OpeningLexH: List[Callable[[re.match], OpeningLexeme]] = list()

		self.StringValueLexT: List[str] = list()
		self.StringValueLexH: List[Callable[[re.match], Lexeme]] = list()

		self.StringValueLexT: List[str] = list()
		self.StringValueLexH: List[Callable[[re.match], StringValueLexeme]] = list()

		# Basic Lexemes

		self.BasicLexT.append(RegExps.OpeningLexeme)
		self.BasicLexH.append(self.classify_opening_lexeme)

		self.BasicLexT.append("[}]")
		self.BasicLexH.append(lambda match: ClosingCurlyBracketLexeme())

		self.BasicLexT.append(RegExps.StringValueLexeme)
		self.BasicLexH.append(self.classify_string_value_lexeme)

		self.BasicLexT.append(RegExps.StringValueLexeme)
		self.BasicLexH.append(self.classify_string_value_lexeme)

		# Opening Lexemes

		self.OpeningLexT.append(RegExps.TechLexeme)
		self.OpeningLexH.append(lambda match: TechLexeme(match.group(1)))

		# StringValue Lexemes

		self.StringValueLexT.append(RegExps.HasEthicLexeme)
		self.StringValueLexH.append(lambda match: HasEthicLexeme(match.group(1)))

		self.StringValueLexT.append(RegExps.HasTraditionLexeme)
		self.StringValueLexH.append(lambda match: HasTraditionLexeme(match.group(1)))

		self.StringValueLexT.append(RegExps.HasValidCivicLexeme)
		self.StringValueLexH.append(lambda match: HasValidCivicLexeme(match.group(1)))

		self.StringValueLexT.append(RegExps.TechAreaLexeme)
		self.StringValueLexH.append(lambda match: TechAreaLexeme(match.group(1)))

		self.StringValueLexT.append(RegExps.TechCategoryLexeme)
		self.StringValueLexH.append(lambda match: TechCategoryLexeme(match.group(1)))

	def classify_opening_lexeme(self, match: re.match) -> OpeningLexeme:
		pass

	def classify_decimal_value_lexeme(self, match: re.match) -> DecimalValueLexeme:
		return DecimalValueLexeme(match.group(1), Decimal(match.group(2)))

	def classify_string_value_lexeme(self, match: re.match) -> StringValueLexeme:
		pass
