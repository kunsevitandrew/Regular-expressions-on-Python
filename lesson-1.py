# Why do you need regular expressions
# 1) проверка фрагмента текста заданному шаблону (например, формат записи номера телефона);
# 2) поиск подстрок по указанному шаблону в тексте;
# 3) поиск и замена регулярного выражения на заданную строку;
# 4) разбиение строки по найденным шаблонам, записанного в виде регулярного выражения
# (например, данные записанные в строке как ключ=значение разбиваются отдельно на ключи и значения).

# Special symbols: \.^$?+*{}[]()|


# Literals and Character classes
import re

text = "I'm reading \t\t\"English read guide\" \t\t for up my read skill. \nP.S. (Read) is good 123123! \n(ID of massage: 345 2351 35 567 34523 34536)"
# res = re.findall(r"read", text)
# res = re.findall(r"\(read\)", text)
# res = re.findall(r"[Rr]ead", text)
# res = re.findall(r"[Rr]ead", text)
# res = re.findall(r"[0-5] [4-9]", text)
# res = re.findall(r"[^0-9]", text)
# print(res)

# print(re.findall(r"[.]", text))
# print(re.findall(r".", text))

# print(re.findall(r"\d", text))
# print(re.findall(r"\D", text))
# print(re.findall(r"\d", text) == re.findall(r"[^\D]", text) == re.findall(r"[0-9]", text))
# print(re.findall(r"[\d]", text))


# print(re.findall(r"\s", text))
# print(re.findall(r"\S", text))

print(re.findall(r"\w", text))
print(re.findall(r"\W", text))
print(re.findall(r"\W", text, re.ASCII))