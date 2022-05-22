# Flags and check in regular expressions
# link to lesson: https://proproprogs.ru/modules/flagi-i-proverki-v-regulyarnyh-vyrazheniyah

import re

# text = "reading, reader, read"
# print(re.findall(r"(read|pleace|check)", text))
# print(re.findall(r"\b(read|pleace|check)\b", text))
# print(re.findall(r"\b(?:read|pleace|check)\b", text))


# text1 = """<!DOCTYPE html>
# <html>
# <head>
# <meta http-equiv="Content-Type " content="text/html; charset=windows-1251">
# <meta name="viewport" content="width=device-width, initial-scale=1.0">
# <title>Уроки по Python</title>
# </head>
# <body>
# <script type="text/javascript">
# let o = document.getElementById('id_div');
# console.log(obj);
# </script>
# </body>
# </html>"""

# print(re.findall(r"<script.*?>([\w\W]*)(?=</script>)", text1))
# print(re.findall(r"<script.*?>([\w\W]*)(?!</script>)", text1))
# print(re.findall(r"<script.*?>([\w\W]*)(?<=</script>)", text1))
# print(re.findall(r"<script.*?>([\w\W]*)(?<!</script>)", text1))
#
# print(re.findall(r"<script.*?>(.*?)(?=</script>)", text1))


# (?P<q>[\"'])

# (?P<q>[\"'])
# (?(id|name)yes_pattern)
# (?(id|name)yes_pattern|no_pattern)

# text2 = """<!DOCTYPE html>
# <html>
# <head>
# <meta http-equiv="Content-Type " content="text/html; charset=windows-1251">
# <meta name="viewport" content="width=device-width, initial-scale=1.0">
# <title>Уроки по Python</title>
# </head>
# <body>
# <p align=center>Hello World!</p>
# </body>
# </html>"""

# print(re.findall(r"([-\w]+)=[\"\']([^\"\']+)(?<![ \t])", text2))
# print(re.findall(r"([-\w]+)=(?P<q>[\"\'])?(?(q)([^\"\']+)(?<![ \t])|([^ \t>]+))", text2))

# print(re.findall(r"""([-\w]+)             #выделяем атрибут
#                    [ \t]*=[ \t]*            #далее, должно идти равно и кавычки
#                    (?P<q>[\"'])?            #проверяем наличие кавычки
#                    (?(q)([^\"']+(?<![ \t]))|([^ \t>]+))     #выделяем значение атрибута
#                    """, text2, re.MULTILINE | re.VERBOSE))


# flags
# (?flags)
# a – то же самое, что и re.ASCII;
# i – соответствует re.IGNORECASE;
# m – для re.MULTILINE;
# s – для re.DOTALL;
# x – для re.VERBOSE.

text3 = "Python, PYTHON, python, pYTHON"

print(re.findall(r"(?i)python", text3))
print(re.findall(r"(?im)python", text3))
print(re.findall(r"(?aimsx)python", text3))
