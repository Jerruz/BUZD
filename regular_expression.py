import re

val = r'mail'

text = 'sd@mail.ru, 3200ыва@mail.com, ###@gmail.ru, bubblok@gmail.com'

res = re.findall(val, text)
print(res)
