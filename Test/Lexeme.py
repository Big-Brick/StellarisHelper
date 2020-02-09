import unittest
import re
from typing import Match, List

from Code.Classes import Lexeme
from Data.Constants import RegExps


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


class TechPrerequisitesTests(unittest.TestCase):
	@classmethod
	def setUpClass(cls) -> None:
		cls.tested_lexeme: type(Lexeme.Lexeme) = Lexeme.TechPrerequisitesLexeme
		cls.valid_strings: List[str] = list()
		cls.invalid_strings: List[str] = list()
		cls.valid_strings.append('prerequisites = { "tech_starbase_4" "tech_modular_engineering" }')
		cls.valid_strings.append('prerequisites = { "tech_starbase_4" }')
		cls.invalid_strings.append('prerequisites = {  }')
		cls.invalid_strings.append('prerequisites = "tech_starbase_4"')

	def test_regex(self):
		regex_testing(self)

	def test_creation(self):
		creation_testing(self)


class TechCategoryTests(unittest.TestCase):
	@classmethod
	def setUpClass(cls) -> None:
		cls.tested_lexeme: type(Lexeme.Lexeme) = Lexeme.TechCategoryLexeme
		cls.valid_strings: List[str] = list()
		cls.invalid_strings: List[str] = list()
		cls.valid_strings.append('category = { tech_starbase_4 }')
		cls.invalid_strings.append('category = {  }')
		cls.invalid_strings.append('sgffd = "tech_starbase_4"')

	def test_regex(self):
		regex_testing(self)

	def test_creation(self):
		creation_testing(self)


class SetValueTests(unittest.TestCase):
	@classmethod
	def setUpClass(cls) -> None:
		cls.tested_lexeme: type(Lexeme.Lexeme) = Lexeme.SetValueLexeme
		cls.valid_strings: List[str] = list()
		cls.invalid_strings: List[str] = list()
		cls.valid_strings.append('sfgsfg = { "tech_starbase_4" tech_modular_engineering }')
		cls.valid_strings.append('dfgd = { "tech_starbase_4" }')
		cls.invalid_strings.append('sfgsfgsf = {  }')
		cls.invalid_strings.append('sgffd = "tech_starbase_4"')

	def test_regex(self):
		regex_testing(self)

	def test_creation(self):
		creation_testing(self)


class TechAreaTests(unittest.TestCase):
	@classmethod
	def setUpClass(cls) -> None:
		cls.tested_lexeme: type(Lexeme.Lexeme) = Lexeme.TechAreaLexeme
		cls.valid_strings: List[str] = list()
		cls.invalid_strings: List[str] = list()
		cls.valid_strings.append('area = tech_starbase_4')
		cls.invalid_strings.append('category = {  }')
		cls.invalid_strings.append('sgffd = tech_starbase_4')

	def test_regex(self):
		regex_testing(self)

	def test_creation(self):
		creation_testing(self)


class HasValidCivicTests(unittest.TestCase):
	@classmethod
	def setUpClass(cls) -> None:
		cls.tested_lexeme: type(Lexeme.Lexeme) = Lexeme.HasValidCivicLexeme
		cls.valid_strings: List[str] = list()
		cls.invalid_strings: List[str] = list()
		cls.valid_strings.append('has_valid_civic = tech_starbase_4')
		cls.invalid_strings.append('category = {  }')
		cls.invalid_strings.append('sgffd = tech_starbase_4')

	def test_regex(self):
		regex_testing(self)

	def test_creation(self):
		creation_testing(self)


class HasTraditionTests(unittest.TestCase):
	@classmethod
	def setUpClass(cls) -> None:
		cls.tested_lexeme: type(Lexeme.Lexeme) = Lexeme.HasValidCivicLexeme
		cls.valid_strings: List[str] = list()
		cls.invalid_strings: List[str] = list()
		cls.valid_strings.append('has_tradition = tech_starbase_4')
		cls.invalid_strings.append('category = {  }')
		cls.invalid_strings.append('sgffd = tech_starbase_4')

	def test_regex(self):
		regex_testing(self)

	def test_creation(self):
		creation_testing(self)


if __name__ == '__main__':
	unittest.main()
