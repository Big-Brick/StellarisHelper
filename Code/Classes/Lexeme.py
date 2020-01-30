from Data.Constants import RegExps

from decimal import *

TraitOpening = 1
TraitClosing = 2
TraitStringValue = 3
TraitDecimalValue = 4
TraitSetValue = 5
TraitFixedName = 6

OpeningBracket: str = "{"
ClosingBracket: str = "}"


class Lexeme:
	def __init__(self, name: str):
		self.Name: str = name
		self.Traits: set = set()

	def get_regex(self) -> str:
		return self.Name


class OpeningLexeme(Lexeme):
	def __init__(self, name: str):
		super(OpeningLexeme, self).__init__(name)
		self.Traits.add(TraitOpening)

	def get_regex(self) -> str:
		res: str = str()
		if TraitFixedName in self.Traits:
			res += RegExps.Group(self.Name)
		else:
			res += RegExps.Group(RegExps.Word)
		res += RegExps.Whitespaced("=")
		res += "[{]"
		return res


class ClosingLexeme(Lexeme):
	def __init__(self, name: str):
		super(ClosingLexeme, self).__init__(name)
		self.Traits.add(TraitClosing)


class ClosingCurlyBracketLexeme(ClosingLexeme):
	def __init__(self):
		super(ClosingCurlyBracketLexeme, self).__init__("}")

	def get_regex(self) -> str:
		return RegExps.Characters(self.Name, "")


class TechLexeme(OpeningLexeme):
	def __init__(self, name: str):
		super(TechLexeme, self).__init__("tech_" + name)

	def get_regex(self):
		return "tech_" + OpeningLexeme.get_regex(self)


class DecimalValueLexeme(Lexeme):
	def __init__(self, name: str, value: Decimal):
		super(DecimalValueLexeme, self).__init__(name)
		self.Value: Decimal = value
		self.Traits.add(TraitDecimalValue)

	def get_regex(self) -> str:
		res: str = str()
		if TraitFixedName in self.Traits:
			res += RegExps.Group(self.Name)
		else:
			res += RegExps.Group(RegExps.Word)
		res += RegExps.Whitespaced("=")
		res += RegExps.Group(RegExps.DecimalNumber)
		return res


class StringValueLexeme(Lexeme):
	def __init__(self, name: str, value: str):
		super(StringValueLexeme, self).__init__(name)
		self.Value: str = value
		self.Traits.add(TraitStringValue)

	def get_regex(self) -> str:
		res: str = str()
		if TraitFixedName in self.Traits:
			res += RegExps.Group(self.Name)
		else:
			res += RegExps.Group(RegExps.Word)
		res += RegExps.Whitespaced("=")
		res += RegExps.Group(RegExps.Word)
		return res


class HasEthicLexeme(StringValueLexeme):
	def __init__(self, value: str):
		super(HasEthicLexeme, self).__init__("has_ethic", value)
		self.Traits.add(TraitFixedName)


class HasTraditionLexeme(StringValueLexeme):
	def __init__(self, value: str):
		super(HasTraditionLexeme, self).__init__("has_tradition", value)
		self.Traits.add(TraitFixedName)


class HasValidCivicLexeme(StringValueLexeme):
	def __init__(self, value: str):
		super(HasValidCivicLexeme, self).__init__("has_valid_civic", value)
		self.Traits.add(TraitFixedName)


class TechAreaLexeme(StringValueLexeme):
	def __init__(self, value: str):
		super(TechAreaLexeme, self).__init__("area", value)
		self.Traits.add(TraitFixedName)


class TechCategoryLexeme(StringValueLexeme):
	def __init__(self, value: str):
		super(TechCategoryLexeme, self).__init__("category", value)
		self.Traits.add(TraitFixedName)

	def get_regex(self) -> str:
		res: str = RegExps.Group(self.Name) + RegExps.Whitespaced("=")
		res += "[{]"
		res += RegExps.Whitespaced(RegExps.Group(RegExps.Word))
		res += "[}]"
		return res


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


class TechPrerequisitesLexeme(SetValueLexeme):
	def __init__(self, value: set):
		super(TechPrerequisitesLexeme, self).__init__("prerequisites", value)
		self.Traits.add(TraitFixedName)
