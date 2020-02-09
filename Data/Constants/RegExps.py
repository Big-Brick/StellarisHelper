from typing import Callable

Group: Callable[[str], str] = lambda string: "(" + string + ")"
Whitespaced: Callable[[str], str] = lambda string: r"[\s]*" + string + r"[\s]*"
Characters: Callable[[str, str], str] = lambda string, quantity: "[" + string + "]" + quantity

Word: str = r"[\w]{1,}"
DecimalNumber: str = r"[\d]+(?:\.[\d]+)?"
