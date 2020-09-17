"""
CP1404 - Practical 6
Rhys Donaldson
"""

from prac_6.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
language_list = [ruby, python, visual_basic]
print(ruby)
print("The dynamically typed languages are: ", [language.name for language in language_list if language.is_dynamic() == True])