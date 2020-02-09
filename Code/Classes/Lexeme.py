from Data.Constants import RegExps

from decimal import Decimal
from typing import List, Callable, Match
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
	def __new__(mcs, clsname, superclasses, attributedict):
		res = type.__new__(mcs, clsname, superclasses, attributedict)
		res.RegExps: List[Callable[[type], str]] = list()
		res.Handlers: List[Callable[[type, Match[str]], 'Lexeme']] = list()
		if len(superclasses) != 0:
			res.Traits: set = set(superclasses[0].Traits)
			superclasses[0].RegExps.append(res.get_regex)
			superclasses[0].Handlers.append(res.dispatch_lexeme_creation)
		return res


class SuperLexeme:
	Traits: set = set()
	RegExps: List[Callable[[type], str]] = list()
	Handlers: List[Callable[[type, Match[str]], 'Lexeme']] = list()


class Lexeme(SuperLexeme, metaclass=LexemeMeta):

	def __init__(self, name: str):
		self.Name: str = name

	@classmethod
	def get_value_regex(cls) -> str:
		res: str = str()
		if TraitFixedName in cls.Traits:
			res += cls.create_dummy_lexeme().Name
		else:
			res += RegExps.Group(RegExps.Word)
		res += RegExps.Whitespaced("=")
		return res

	@classmethod
	def get_regex(cls) -> str:
		return RegExps.Group(".*")

	@classmethod
	def create_lexeme(cls, match: Match[str]) -> 'Lexeme':
		return cls(match.group(0))

	@classmethod
	def create_dummy_lexeme(cls) -> 'Lexeme':
		return cls("Dummy")

	@classmethod
	def dispatch_lexeme_creation(cls, match: Match[str]) -> 'Lexeme':
		for pattern_func in cls.RegExps:
			match2 = re.fullmatch(pattern_func(), match.group(0))
			if match2 is not None:
				return cls.Handlers[cls.RegExps.index(pattern_func)](match2)
		return cls.create_lexeme(match)


class OpeningLexeme(Lexeme):
	Traits: set = set()
	@classmethod
	def get_regex(cls) -> str:
		res: str = cls.get_value_regex()
		res += "[{]"
		return res


OpeningLexeme.Traits.add(TraitOpening)


class ClosingLexeme(Lexeme):
	def __init__(self):
		super(ClosingLexeme, self).__init__("}")

	@classmethod
	def get_regex(cls) -> str:
		return "[}]"

	@classmethod
	def create_lexeme(cls, match: Match[str]) -> Lexeme:
		return cls()

	@classmethod
	def create_dummy_lexeme(cls) -> Lexeme:
		return cls()


ClosingLexeme.Traits.add(TraitClosing)


class TechLexeme(OpeningLexeme):
	def __init__(self, name: str):
		super(TechLexeme, self).__init__("tech_" + name)

	@classmethod
	def get_regex(cls):
		return "tech_" + OpeningLexeme.get_regex()

	@classmethod
	def create_lexeme(cls, match: Match[str]) -> Lexeme:
		return cls(match.group(1))

	@classmethod
	def create_dummy_lexeme(cls) -> Lexeme:
		return cls("dummy")


class TechWeightModifierLexeme(OpeningLexeme):
	def __init__(self):
		super(TechWeightModifierLexeme, self).__init__("weight_modifier")

	@classmethod
	def create_lexeme(cls, match: Match[str]) -> Lexeme:
		return cls()

	@classmethod
	def create_dummy_lexeme(cls) -> Lexeme:
		return cls()


TechWeightModifierLexeme.Traits.add(TraitFixedName)


class DecimalValueLexeme(Lexeme):
	def __init__(self, name: str, value: Decimal):
		super(DecimalValueLexeme, self).__init__(name)
		self.Value: Decimal = value

	@classmethod
	def get_regex(cls) -> str:
		res: str = cls.get_value_regex()
		res += RegExps.Group(RegExps.DecimalNumber)
		return res

	@classmethod
	def create_lexeme(cls, match: Match[str]) -> Lexeme:
		return cls(match.group(1), Decimal(match.group(2)))

	@classmethod
	def create_dummy_lexeme(cls) -> Lexeme:
		return cls("dummy", Decimal(0))


DecimalValueLexeme.Traits.add(TraitDecimalValue)


class StringValueLexeme(Lexeme):
	def __init__(self, name: str, value: str):
		super(StringValueLexeme, self).__init__(name)
		self.Value: str = value

	@classmethod
	def get_regex(cls) -> str:
		res: str = cls.get_value_regex()
		res += RegExps.Group(RegExps.Word)
		return res

	@classmethod
	def create_lexeme(cls, match: Match[str]) -> Lexeme:
		return cls(match.group(1), match.group(2))

	@classmethod
	def create_dummy_lexeme(cls) -> Lexeme:
		return cls("dummy", "dummy")


StringValueLexeme.Traits.add(TraitStringValue)


def fixed_name_decorator(cls: type(Lexeme)):
	cls.Traits.add(TraitFixedName)

	@classmethod
	def create_fn_lexeme(curr_type, match: Match[str]) -> Lexeme:
		return curr_type(match.group(1))

	@classmethod
	def create_dummy_fn_lexeme(curr_type) -> Lexeme:
		return curr_type("dummy")
	cls.create_lexeme = create_fn_lexeme
	cls.create_dummy_lexeme = create_dummy_fn_lexeme
	return cls


@fixed_name_decorator
class HasEthicLexeme(StringValueLexeme):
	def __init__(self, value: str):
		super(HasEthicLexeme, self).__init__("has_ethic", value)


@fixed_name_decorator
class HasTraditionLexeme(StringValueLexeme):
	def __init__(self, value: str):
		super(HasTraditionLexeme, self).__init__("has_tradition", value)


@fixed_name_decorator
class HasValidCivicLexeme(StringValueLexeme):
	def __init__(self, value: str):
		super(HasValidCivicLexeme, self).__init__("has_valid_civic", value)


@fixed_name_decorator
class TechAreaLexeme(StringValueLexeme):
	def __init__(self, value: str):
		super(TechAreaLexeme, self).__init__("area", value)


class SetValueLexeme(Lexeme):
	def __init__(self, name: str, value: set):
		super(SetValueLexeme, self).__init__(name)
		self.Value: set = value

	@classmethod
	def get_regex(cls) -> str:
		res: str = cls.get_value_regex()
		res += RegExps.Whitespaced("[{]")
		res += RegExps.Group("(?:[\"]?" + RegExps.Word + "[\"]? )" + "+") + RegExps.Whitespaced("[}]")
		return res

	@classmethod
	def create_lexeme(cls, match: Match[str]) -> Lexeme:
		return cls(match.group(1), {w for w in match.group(2).split(" ")})

	@classmethod
	def create_dummy_lexeme(cls) -> Lexeme:
		return cls("dummy", {"dummy"})


SetValueLexeme.Traits.add(TraitSetValue)


class TechCategoryLexeme(SetValueLexeme):
	def __init__(self, value: str):
		super(TechCategoryLexeme, self).__init__("category", value)

	@classmethod
	def create_lexeme(cls, match: Match[str]) -> Lexeme:
		return cls(match.group(1))

	@classmethod
	def create_dummy_lexeme(cls) -> Lexeme:
		return cls("dummy")


TechCategoryLexeme.Traits.add(TraitFixedName)


class TechPrerequisitesLexeme(SetValueLexeme):
	def __init__(self, value: set):
		super(TechPrerequisitesLexeme, self).__init__("prerequisites", value)

	@classmethod
	def create_lexeme(cls, match: Match[str]) -> Lexeme:
		return cls({w for w in match.group(1).split(" ")})

	@classmethod
	def create_dummy_lexeme(cls) -> Lexeme:
		return cls({"dummy"})


TechPrerequisitesLexeme.Traits.add(TraitFixedName)
