from typing import Callable

Group: Callable[[str], str] = lambda string: "(" + string + ")"
Whitespaced: Callable[[str], str] = lambda string: "[\s]*" + string + "[\s]*"

word: str = "[\w]{1,}"

TechLexeme: str = "tech_" + Group(word) + Whitespaced("=") + "[{]"