from typing import Callable

Group: Callable[[str], str] = lambda string: "(" + string + ")"
Whitespaced: Callable[[str], str] = lambda string: r"[\s]*" + string + r"[\s]*"
Characters: Callable[[str, str], str] = lambda string, quantity: "[" + string + "]" + quantity

Word: str = r"[\w]{1,}"
DecimalNumber: str = r"[\d]+(?:\.[\d]+)?"


OpeningLexeme: str = Group(Word) + Whitespaced("=") + "[{]"

TechLexeme: str = "tech_" + Group(Word) + Whitespaced("=") + "[{]"

DecimalValueLexeme: str = ""

StringValueLexeme: str = Group(Word) + Whitespaced("=") + Group(Word)
HasEthicLexeme: str = "has_ethic" + Whitespaced("=") + Group(Word)
HasTraditionLexeme: str = "has_tradition" + Whitespaced("=") + Group(Word)
HasValidCivicLexeme: str = "has_valid_civic" + Whitespaced("=") + Group(Word)
TechAreaLexeme: str = "area" + Whitespaced("=") + Group(Word)
TechCategoryLexeme: str = "category" + Whitespaced("=") + "[{]" + Group(Word) + "[}]"
