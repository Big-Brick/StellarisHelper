from Data.Constants import RegExps

from decimal import *
from typing import *
import re

TraitOpening = 1
TraitClosing = 2
TraitStringValue = 3
TraitDecimalValue = 4
TraitSetValue = 5
TraitFixedName = 6

OpeningBracket: str = "{"
ClosingBracket: str = "}"


class LexemeMeta(type):
    def __new__(cls, clsname, superclasses, attributedict):
		superclasses[0].RegExps.append(clsname.get_regex)
		superclasses[0].RegExps.append(clsname.dispatch_lexeme_creation)
		

class SuperLexeme():
	RegExps: List[Callable[['type'], str] = list()
	Handlers: List[Callable[['type', re.Match], Lexeme]] = list()


class Lexeme(SuperLexeme, metaclass = LexemeMeta):
	Traits: set = set()
	def __init__(self, name: str):
		self.Name: str = name

	@staticmethod
	def get_regex(curr_type: 'type') -> str:
		return RegExps.Group(".*")

	@staticmethod
	def create_lexeme(curr_type: 'type', match: re.Match) -> Lexeme:
		return curr_type(match.group(0))

	@staticmethod
	def create_dummy_lexeme(curr_type: 'type') -> Lexeme:
		return curr_type("Dummy")

	@staticmethod
	def dispatch_lexeme_creation(curr_type: 'type', match: re.Match) -> Lexeme:
		for pattern_func in curr_type.RegExps:
			match2 = re.fullmatch(pattern_func(), match.group(0))
			if match2 is not None:
				return curr_type.Handlers[curr_type.RegExps.index(pattern)](match2)
	return curr_type.create_lexeme(match.group(0))


class OpeningLexeme(Lexeme):
	@staticmethod
	def get_regex(curr_type: 'type') -> str:
		res: str = str()
		if TraitFixedName in curr_type.Traits:
			res += RegExps.Group(self.Name)
		else:
			res += RegExps.Group(RegExps.Word)
		res += RegExps.Whitespaced("=")
		res += "[{]"
		return res

OpeningLexeme.Traits.add(TraitOpening)


class ClosingLexeme(Lexeme):
	def __init__(self, name: str):
		super(ClosingLexeme, self).__init__(name)

ClosingLexeme.Traits.add(TraitClosing)


class ClosingCurlyBracketLexeme(ClosingLexeme):
	def __init__(self):
		super(ClosingCurlyBracketLexeme, self).__init__("}")

	@staticmethod
	def get_regex(curr_type: 'type') -> str:
		return "[}]"

	@staticmethod
	def create_lexeme(curr_type: 'type', match: re.Match) -> Lexeme:
		return curr_type()

	@staticmethod
	def create_dummy_lexeme(curr_type: 'type') -> Lexeme:
		return curr_type()


class TechLexeme(OpeningLexeme):
	def __init__(self, name: str):
		super(TechLexeme, self).__init__("tech_" + name)

	@staticmethod
	def get_regex(curr_type: 'type'):
		return "tech_" + OpeningLexeme.get_regex(curr_type)

	@staticmethod
	def create_lexeme(curr_type: 'type', match: re.Match) -> Lexeme:
		return curr_type(match.group(1))

	@staticmethod
	def create_dummy_lexeme(curr_type: 'type') -> Lexeme:
		return curr_type("dummy")


class DecimalValueLexeme(Lexeme):
	def __init__(self, name: str, value: Decimal):
		super(DecimalValueLexeme, self).__init__(name)
		self.Value: Decimal = value

	@staticmethod
	def get_regex(curr_type: 'type') -> str:
		res: str = str()
		if TraitFixedName in curr_type.Traits:
			res += RegExps.Group(curr_type.create_dummy_lexeme().Name)
		else:
			res += RegExps.Group(RegExps.Word)
		res += RegExps.Whitespaced("=")
		res += RegExps.Group(RegExps.DecimalNumber)
		return res

	@staticmethod
	def create_lexeme(curr_type: 'type', match: re.Match) -> Lexeme:
		return curr_type.create_lexeme(match.group(1), match.group(2))

	@staticmethod
	def create_dummy_lexeme(curr_type: 'type') -> Lexeme:
		return curr_type.create_lexeme("dummy", 0)


DecimalValueLexeme.Traits.add(TraitDecimalValue)


class StringValueLexeme(Lexeme):
	def __init__(self, name: str, value: str):
		super(StringValueLexeme, self).__init__(name)
		self.Value: str = value

	@staticmethod
	def get_regex(curr_type: 'type') -> str:
		res: str = str()
		if TraitFixedName in curr_type.Traits:
			res += RegExps.Group(curr_type.create_dummy_lexeme().Name)
		else:
			res += RegExps.Group(RegExps.Word)
		res += RegExps.Whitespaced("=")
		res += RegExps.Group(RegExps.Word)
		return res

	@staticmethod
	def create_lexeme(curr_type: 'type', match: re.Match) -> Lexeme:
		return curr_type.create_lexeme(match.group(1), match.group(2))

	@staticmethod
	def create_dummy_lexeme(curr_type: 'type') -> Lexeme:
		return curr_type.create_lexeme("dummy", "dummy")

StringValueLexeme.Traits.add(TraitStringValue)


class FixedNameStringValueLexeme(StringValueLexeme):
	@staticmethod
	def create_lexeme(curr_type: 'type', match: re.Match) -> Lexeme:
		return curr_type.create_lexeme(curr_type.create_dummy_lexeme().Name, match.group(1))

	@staticmethod
	def create_dummy_lexeme(curr_type: 'type') -> Lexeme:
		return curr_type.create_lexeme("dummy", "dummy")

FixedNameStringValueLexeme.Traits.add(TraitFixedName)


class HasEthicLexeme(FixedNameStringStringValueLexeme):
	def __init__(self, value: str):
		super(HasEthicLexeme, self).__init__("has_ethic", value)

	@staticmethod
	def create_dummy_lexeme(curr_type: 'type') -> Lexeme:
		return curr_type.create_lexeme("dummy")


class HasTraditionLexeme(FixedNameStringStringValueLexeme):
	def __init__(self, value: str):
		super(HasTraditionLexeme, self).__init__("has_tradition", value)

	@staticmethod
	def create_dummy_lexeme(curr_type: 'type') -> Lexeme:
		return curr_type.create_lexeme("dummy")


class HasValidCivicLexeme(StringValueLexeme):
	def __init__(self, value: str):
		super(HasValidCivicLexeme, self).__init__("has_valid_civic", value)

	@staticmethod
	def create_dummy_lexeme(curr_type: 'type') -> Lexeme:
		return curr_type.create_lexeme("dummy")


class TechAreaLexeme(StringValueLexeme):
	def __init__(self, value: str):
		super(TechAreaLexeme, self).__init__("area", value)


class TechWeightModifierLexeme(OpeningLexeme):
	def __init__(self):
		super(TechWeightModifierLexeme, self).__init__("weight_modifier")
		self.Traits.add(TraitFixedName)


class SetValueLexeme(Lexeme):
	def __init__(self, name: str, value: set):
		super(SetValueLexeme, self).__init__(name)
		self.Value: set = value
		self.Traits.add(TraitSetValue)

	def get_regex(self) -> str:
		res: str = str()
		if TraitFixedName in self.Traits:
			res += RegExps.Group(self.Name)
		else:
			res += RegExps.Group(RegExps.Word)
		res += RegExps.Whitespaced("=") + RegExps.Whitespaced("[{]")
		res += RegExps.Group("(?:\"" + RegExps.Word + "\" )" + "*")
		return res


class TechCategoryLexeme(StringValueLexeme):
	def __init__(self, value: str):
		super(TechCategoryLexeme, self).__init__("category", value)

	@staticmethod
	def create_dummy_lexeme(curr_type: 'type') -> Lexeme:
		return curr_type.create_lexeme("dummy")

	def get_regex(self) -> str:
		res: str = RegExps.Group(self.Name) + RegExps.Whitespaced("=")
		res += "[{]"
		res += RegExps.Whitespaced(RegExps.Group(RegExps.Word))
		res += "[}]"
		return res


class TechPrerequisitesLexeme(SetValueLexeme):
	def __init__(self, value: set):
		super(TechPrerequisitesLexeme, self).__init__("prerequisites", value)
		self.Traits.add(TraitFixedName)
