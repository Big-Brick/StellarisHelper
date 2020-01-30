from decimal import *

TraitOpening = 1
TraitClosing = 2
TraitStringValue = 3
TraitDecimalValue = 4
TraitSetValue = 5


class Lexeme:
	def __init__(self, name: str):
		self.Name: str = name
		self.Traits: set = set()


class TechLexeme(Lexeme):
	def __init__(self, name: str):
		super(TechLexeme, self).__init__("tech_" + name)
		self.Traits.add(TraitOpening)


class OpeningLexeme(Lexeme)
	def __init__(self, name: str):
		super(ClosingLexeme, self).__init__(name)
		self.Traits.add(TraitOpening)


class ClosingLexeme(Lexeme)
	def __init__(self, name: str):
		super(ClosingLexeme, self).__init__(name)
		self.Traits.add(TraitClosing)

class ClosingCurlyBracketLexeme(ClosingLexeme):
	def __init__(self)
		super(ClosingCurlyBracketLexeme, self).__init__("}");


class StringValueLexeme(OpeningLexeme):
	def __init__(self, name: str, value: str):
		super(StringValueLexeme, self).__init__(name)
		self.Value: str = value


class HasEthicLexeme(StringValueLexeme):
	def __init__(self, value: str):
		super(HasEthicLexeme, self).__init__("has_ethic", value)


class HasTraditionLexeme(StringValueLexeme):
	def __init__(self, value: str):
		super(HasTraditionLexeme, self).__init__("has_tradition", value)


class HasValidCivicLexeme(StringValueLexeme):
	def __init__(self, value: str):
		super(HasValidCivicLexeme, self).__init__("has_valid_civic", value)


class TechAreaLexeme(StringValueLexeme):
	def __init__(self, value: str):
		super(TechAreaLexeme, self).__init__("area", value)


class TechCategoryLexeme(StringValueLexeme):
	def __init__(self, value: str):
		super(TechCategoryLexeme, self).__init__("category", value)


class DecimalValueLexeme(Lexeme):
	def __init__(self, name: str, value: Decimal):
		super(DecimalValueLexeme, self).__init__(name)
		self.Value: Decimal = value
		self.Traits.add(TraitDecimalValue)


class TechTierLexeme(DecimalValueLexeme):
	def __init__(self, value: decimal):
		super(TechTierLexeme, self).__init__("tier", value)


class TechWeightModifierLexeme(OpeningLexeme):
	def __init__(self):
		super(TechWeightModifierLexeme, self).__init__("weight_modifier")


class SetValueLexeme(Lexeme):
	def __init__(self, name: str, value: set):
		super(DecimalValueLexeme, self).__init__(name)
		self.Value: set = value
		self.Traits.add(TraitSetValue)


class TechPrerequisitesLexeme(SetValueLexeme):
	def __init__(self, value: set):
		super(TechPrerequisitesLexeme, self).__init__("prerequisites", value)
