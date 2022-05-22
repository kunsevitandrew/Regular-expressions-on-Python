# Object re.Match, methods re.search, re.finditer, re.findall

import re

# block-1

# text = "<font color=#CC0000>"
# match = re.search(r"([\w]+)\s*=\s*(#[A-Za-z0-9]{6})\b", text)

# print(match.group(0))
# print(match.group(1))
# print(match.group(2))
# print(match.group(0,1,2))
#
# print(match.groups())
# print(match.lastindex)
#
# print(match.start(1))
# print(match.end(1))
#
# print(match.span(1))
# print(match.span(2))
#
# print(match.endpos)
# print(match.pos)
#
# print(match.re)
# print(match.string)


# block-2

text = "<font color=#CC0000>"

# match = re.search(r"(?P<key>[\w]+)\s*=\s*(?P<value>#[A-Za-z0-9]{6})\b", text)
#
# print(match.groupdict())
# print(match.lastgroup)
#
# print(match.expand(r"\g<key> === = == = === \g<value>"))
# print(match.expand(r"\1 === = == = === \2"))


iter_match = re.finditer(r"(?P<key>[\w]+)\s*=\s*(?P<value>#[A-Za-z0-9]{6})\b", text)
print(iter_match)
print(next(iter_match))

lst_match = re.findall(r"(?P<key>[\w]+)\s*=\s*(?P<value>#[A-Za-z0-9]{6})\b", text)
print(lst_match)