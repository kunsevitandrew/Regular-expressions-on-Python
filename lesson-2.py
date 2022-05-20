# Regular expression quantifiers
# {m} – повторение выражения ровно m раз (эквивалент {m,m});
# {m,} – повторения от m и более раз;
# {, n} – повторения не более n раз.
#
# {m,}? {,n}? - минорные формыю
#
# ? – от нуля до одного (аналог {0,1});
# * – от нуля и до «бесконечности» (в действительности, большого числа – от 32767), соответствует квантификатору {0,};
# + – от единицы и до «бесконечности» (также большого числа – от 32767), соответствует квантификатору {1,}.
#
# ?? *? +? - минорный режим.


import re

text = "I'm reading \t\t\"English Rrread guide\" \t\t for up my read skill. \nP.S. (Read) is good 123123! \n(ID of massage: 345 25555351 35 567 34523 34536)"

# print(re.findall(r"5{2,4}",text))
# print(re.findall(r"[Rr]{2,}", text))
# print(re.findall(r"5\d{,2}", text))

print(re.findall(r"5\d+?", text))
print(re.findall(r"5\d+", text))

print(re.findall(r"5\d*", text))
print(re.findall(r"5\d*?", text))

text2 = "Autor = \"Lupsik Zalupsik\", title =\"Titele\", name = \"Krumka Pumka\""
print(re.findall(r"(\w+)\s*=\s*\"([^,\"]+)", text2))

# You need to take url address from img tag
text3 = """
<p>Картинка <img alt='картинка' src='bg.jpg'> в тексте</p>
<p>Картинка <img src='bg.jpg'> в тексте</p>
<p>Картинка <img src='bg.jpg' title='картинка'> в тексте</p>

<img>
<p>Картинка <img src2='bg.jpg'> в тексте</p>
<p>Картинка <img alt='картинка'> в тексте</p>
"""

res = re.findall(r"<\s*img\s+[^>]*?\s*src=[^>]+?>", text3)
print(res)