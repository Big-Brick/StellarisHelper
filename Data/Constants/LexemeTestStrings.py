from typing import List

TechPrerequisitesValid: List[str] = ['{ "tech_starbase_4" "tech_modular_engineering" }', 'prerequisites = { "tech_starbase_4" }']
TechPrerequisitesInvalid: List[str] = ['prerequisites = {  }', 'prerequisites = "tech_starbase_4"']

TechCategoryValid: List[str] = ['category = { tech_starbase_4 }']
TechCategoryInvalid: List[str] = ['category = {  }', 'sgffd = "tech_starbase_4"']

SetValueValid: List[str] = ['sfgsfg = { "tech_starbase_4" tech_modular_engineering }', 'dfgd = { "tech_starbase_4" }']
SetValueInvalid: List[str] = ['sfgsfgsf = {  }', 'sgffd = "tech_starbase_4"']

TechAreaValid: List[str] = ['area = tech_starbase_4']
TechAreaInvalid: List[str] = ['category = {  }', 'sgffd = tech_starbase_4']

HasValidCivicValid: List[str] = ['has_valid_civic = tech_starbase_4']
HasValidCivicInvalid: List[str] = ['category = {  }', 'sgffd = tech_starbase_4']

HasTraditionValid: List[str] = ['has_tradition = tech_starbase_4']
HasTraditionInvalid: List[str] = ['category = {  }', 'sgffd = tech_starbase_4']

HasEthicValid: List[str] = ['has_ethic = ethic_militarist']
HasEthicInvalid: List[str] = ['has_dsfsfd = ethic_militarist', 'has_ethic = {ethic_militarist}', 'has_ethic = "ethic_militarist"']

StringValueValid: List[str] = ['foo = bar']
StringValueInvalid: List[str] = ['foo = ', ' = bar', 'foo = {"bar", "baz"}']
