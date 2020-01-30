from decimal import *


class Tag:
	def __init__(self, name: str):
		self.Name: str = name
		self.Inners: list = list()
		self.Traits: set = set()


class StringValueTag(Tag):
	def __init__(self, name: str, value: str):
		super(StringValueTag, self).__init__(name)
		self.Value: str = value


class HasEthicTag(StringValueTag):
	def __init__(self, value: str):
		super(HasEthicTag, self).__init__("has_ethic", value)


class HasTraditionTag(StringValueTag):
	def __init__(self, value: str):
		super(HasTraditionTag, self).__init__("has_tradition", value)


class TechAreaTag(StringValueTag):
	def __init__(self, value: str):
		super(TechAreaTag, self).__init__("area", value)


class DecimalValueTag(Tag):
	def __init__(self, name: str, value: Decimal):
		super(DecimalValueTag, self).__init__(name)
		self.Value: Decimal = value


class TechTierTag(DecimalValueTag):
	def __init__(self, value: decimal):
		super(TechTierTag, self).__init__("tier", value)


class ListValueTag(Tag):
	def __init__(self, name: str, value: list):
		super(ListValueTag, self).__init__(name)
		self.Value: list = value


class TechWeightModifierTag(ListValueTag):
	def __init__(self, value: list):
		super(TechWeightModifierTag, self).__init__("weight_modifier", value)


class SetValueTag(Tag):
	def __init__(self, name: str, value: set):
		super(DecimalValueTag, self).__init__(name)
		self.Value: set = value


class TechTag(SetValueTag):
	def __init__(self, name: str, value: set):
		super(TechTag, self).__init__(name, value)


class TechCategoryTag(SetValueTag):
	def __init__(self, value: set):
		super(TechCategoryTag, self).__init__("category", value)


class TechPrerequisitesTag(SetValueTag):
	def __init__(self, value: set):
		super(TechPrerequisitesTag, self).__init__("prerequisites", value)
