import unittest
import re
from typing import Match, List

from Code.Classes import Lexeme
from Data.Constants import RegExps, LexemeTestStrings


def regex_testing(self) -> None:
	regex: str = self.tested_lexeme.get_regex()
	regex = RegExps.Whitespaced(regex)
	for string in self.valid_strings:
		res = re.fullmatch(regex, string)
		self.assertIsNotNone(res)
	for string in self.invalid_strings:
		res = re.fullmatch(regex, string)
		self.assertIsNone(res)


def creation_testing(self):
	match: Match[str]
	curr_cls: Lexeme.Lexeme = self.tested_lexeme
	while issubclass(type(curr_cls), type(Lexeme.Lexeme)):
		match = re.match(curr_cls.get_regex(), self.valid_strings[0])
		self.assertIsNotNone(
			match,
			msg="re.match for:\nclass: %s\nregex %s\nstring: %s\nFailed!" %
			(str(curr_cls), curr_cls.get_regex(), self.valid_strings[0]))
		self.assertIsInstance(curr_cls.dispatch_lexeme_creation(match), self.tested_lexeme)
		curr_cls = curr_cls.__bases__[0]
	while issubclass(type(curr_cls), type(Lexeme.Lexeme)):
		match = re.match(curr_cls.get_regex(), self.invalid_strings[0])
		self.assertIsNotNone(
			match,
			msg="re.match for:\nclass: %s\nregex %s\nstring: %s\nFailed!" %
			(str(curr_cls), curr_cls.get_regex(), self.invalid_strings[0]))
		self.assertNotIsInstance(curr_cls.dispatch_lexeme_creation(match), self.tested_lexeme)
		curr_cls = curr_cls.__bases__[0]


class FixedNameDecoratorTests(unittest.TestCase):
	def test_creation(self):
		regex: str = Lexeme.HasEthicLexeme.get_regex()
		res = re.fullmatch(regex, "has_ethic = dummy")
		self.assertIsInstance(Lexeme.HasEthicLexeme.create_lexeme(res), Lexeme.HasEthicLexeme)
		self.assertIsInstance(Lexeme.HasEthicLexeme.create_dummy_lexeme(), Lexeme.HasEthicLexeme)


class LexemeTests(unittest.TestCase):
	@classmethod
	def setUpClass(cls) -> None:
		cls.tested_lexeme: type(Lexeme.Lexeme) = Lexeme.Lexeme
		cls.valid_strings: List[str] = list()
		cls.invalid_strings: List[str] = list()

	@classmethod
	def mySetUpClass(cls, lex_type: type(Lexeme.Lexeme), valid_strings: List[str], invalid_strings: List[str]) -> None:
		cls.tested_lexeme = lex_type
		cls.valid_strings = valid_strings
		cls.invalid_strings = invalid_strings

	def test_regex(self) -> None:
		regex_testing(self)

	def test_creation(self) -> None:
		creation_testing(self)


class TechPrerequisitesTests(unittest.LexemeTests):
	@classmethod
	def setUpClass(cls) -> None:
		TechPrerequisitesTests.mySetUpClass(Lexeme.TechPrerequisitesLexeme, LexemeTestStrings.TechPrerequisitesValid, LexemeTestStrings.TechPrerequisitesInvalid)


class TechCategoryTests(unittest.LexemeTests):
	@classmethod
	def setUpClass(cls) -> None:
		TechCategoryTests.mySetUpClass(Lexeme.TechCategoryLexeme, LexemeTestStrings.TechCategoryValid, LexemeTestStrings.TechCategoryInvalid)


class SetValueTests(unittest.LexemeTests):
	@classmethod
	def setUpClass(cls) -> None:
		SetValueTests.mySetUpClass(Lexeme.SetValueLexeme, LexemeTestStrings.SetValueValid, LexemeTestStrings.SetValueInvalid)


class TechAreaTests(unittest.LexemeTests):
	@classmethod
	def setUpClass(cls) -> None:
		TechAreaTests.mySetUpClass(Lexeme.TechAreaLexeme, LexemeTestStrings.TechAreaValid, LexemeTestStrings.TechAreaInvalid)


class HasValidCivicTests(unittest.LexemeTests):
	@classmethod
	def setUpClass(cls) -> None:
		HasValidCivicTests.mySetUpClass(Lexeme.HasValidCivicLexeme, LexemeTestStrings.HasValidCivicValid, LexemeTestStrings.HasValidCivicInvalid)


class HasTraditionTests(unittest.LexemeTests):
	@classmethod
	def setUpClass(cls) -> None:
		HasTraditionTests.mySetUpClass(Lexeme.HasTraditionLexeme, LexemeTestStrings.HasTraditionValid, LexemeTestStrings.HasTraditionInvalid)


class HasEthicTests(unittest.LexemeTests):
	@classmethod
	def setUpClass(cls) -> None:
		HasEthicTests.mySetUpClass(Lexeme.HasEthicLexeme, LexemeTestStrings.HasEthicValid, LexemeTestStrings.HasEthicInvalid)


class StringValueTests(unittest.LexemeTests):
	@classmethod
	def setUpClass(cls) -> None:
		StringValueTests.mySetUpClass(Lexeme.StringValueLexeme, LexemeTestStrings.StringValueValid, LexemeTestStrings.StringValueInvalid)


if __name__ == '__main__':
	unittest.main()
