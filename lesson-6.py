# Methods  re.match, re.split, re.sub, re.subn, re.compile
# link: https://proproprogs.ru/modules/metody-match-split-sub-subn-compile

import re

# block-1
# text = "+7(123)456-78-90"
# m = re.match(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", text)
# print(m)
#
# text = " +7(123)456-78-90"  # Because at the beginning of the line is a space
# m = re.match(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", text)
# print(m)


# block-2
# text = """<point lon="40.8482" lat="52.6274" />
# <point lon="40.8559" lat="52.6361" />; <point lon="40.8614" lat="52.651" />
# <point lon="40.8676" lat="52.6585" />, <point lon="40.8672" lat="52.6626" />
# """
# print(re.split(r"[\n;,]", text))


# block-3
#
# re.sub(pattern, repl, string, count, flags)
#
# pattern – регулярное выражение;
# repl – строка или функция для замены найденного выражения;
# string – анализируемая строка;
# count – максимальное число замен (если не указано, то неограниченно);
# flags – набор флагов (по умолчанию не используются).
#
# text = """Moscow
# New-York
# Washington
# Seattle
# Las-Vegas"""
#
# # lst = re.sub(r"([-\w]+)\s*", "<h1>\1</h1>\n", text)
# lst = re.sub(r"([-\w]+)\s*", r"<h1>\1</h1>\n", text)
# print(lst)
#
# count = 0
# def replFind(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# lst = re.sub(r"([-\w]+)\s*", replFind, text)
# print(lst)
#
# lst, n = re.subn(r"([-\w]+)\s*", r"<h1>\1</h1>\n", text)
# print(lst, n, sep="")


# block-4
text = """Moscow
New-York
Washington
Seattle
Las-Vegas"""

rx = re.compile(r"([-\w]+)\s*")
print(rx)

lst = rx.sub(r"<h1>\1</h1>\n", text)
print(rx.findall(text))
print(lst)

# additional properties of the Pattern class
# flags – возвращает список флагов, которые были установлены при компиляции;
# pattern – строка исходного шаблона;
# groupindex – словарь, ключами которого являются имена сохраняющих групп, а значениями – номера групп (пустой, если имена не используются).

print(rx.flags)
print(rx.pattern)
print(rx.groupindex)
