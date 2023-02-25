import re

file = open(file='radio_stations.txt', mode='r', encoding='utf-8')
text = file.read()

print(re.findall(r'(?<=\/)(?:[a-z\d]+\.)+[a-z]+(?=:)', text))
