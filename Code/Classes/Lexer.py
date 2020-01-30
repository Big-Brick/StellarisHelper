from Code.Classes.Lexeme import *
import Data.Constants.RegExps

from typing import Callable


class Lexer:
	def __init__(self):
		self.LexText: list = list()
		self.LexCons: list = list()

		self.LexText.append(RegExps.TechLexemeR)
		self.LexCons.append(lambda match: TechLexeme(match.group(1)))

		self.LexText.append("[}]")
		self.LexCons.append(ClosingCurlyBracketLexeme().__class__)

		self.LexText.append(RegExps.StringValueLexemeR)
		self.LexCons.append(lambda match: StringValueLexeme(match.group(1), match.group(2)))
