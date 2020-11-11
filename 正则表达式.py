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

text = ['“在疫情防控中，残疾人一直是重点保护和关照的对象。”国家卫健委副主任李斌说，国家卫健委正重点研究解决残疾人信息获得、设施配备和专项通道等问题。\n\n弱势群体的人权能否得到有效保障，既是观察一个国家人权状况的主要窗口，也是检验一个国家政治文明程度的重要标准。\n\n奥斯陆城市大学社会工作系教授鲁尼·哈佛森认为，疫情给各类社会成员带来的影响并不均等，需要对特定群体进行更多的关心关爱和社会干预。']
regex = re.compile('“.*?”|‘.*?’|".*?"')
text[0] = regex.sub("ΩΩΩΩ", text[0])

print(text)

list1 = ['新华社', '记者', '高蕾', '王子', '铭', '温馨']
list2 = ['新华社', '记者', '高蕾', '王子', '铭', '温馨']

print(list(set(list1 + list2)))