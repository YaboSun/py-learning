import re

title = "中国人民 站起来 了"
str = re.sub(r'[\s+]', '', title)
print(str)

var = lambda d: d[4]
print(var)

print(' '.join(str))
year = re.compile('19[0-9][0-9]|20[0-9][0-9]|wps')
nonchinese = re.compile('[^\u4e00-\u9fa5]')
sentence = "2012wps2012"

if len("".join(year.findall(sentence))) == len(sentence):
    print("true")
else:
    print("false")