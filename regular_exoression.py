import re
s="This is a python program portal"
match=re.search('portal',s)
print('start index',match.start())
print('end index',match.end())
print(match)
