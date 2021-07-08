import re
f = open(r'cheque.txt', 'r', encoding='utf-8')
data = f.read()
name = re.search(r'Филиал\sТОО\s\w+\s\w+', data)
bin = re.search(r'[0-9]{12}', data)
date = re.search(r'\d{2}\.\d{2}\.\d{4}\s\d{2}\:\d{2}\:\d{2}', data)
address = re.search(r'г\.\s[\w\-]+\,\w+\,\s[\w\s]+\,\d+\,\s\w+\-\d', data)
item_titles = re.findall(r'\d+\.\n(.*)', data)
item_count = re.findall(r'(\d)\,\d{3}', data)
item_price = re.findall(r'x\s([\d\s]+\,\d+)', data)
item_total_price = re.findall(r'Стоимость\n([\d\s]+\,\d+)', data)

print('1.Name of the company: ' + name.group(0))
print('2.BIN number: ' + bin.group(0))
print('3.For each item:')

for i in range(len(item_titles)):
    print('\t1.Title——(' + item_titles[0] + ')')
    print('\t2.Cout——(' + item_count[0] + ')')
    print('\t3.Unit price——(' + item_price[0] + ')')
    print('\t4.Total price——' + item_total_price[0] + ')\n')

print('4.Date——(' + date.group(0) + ')')
print('5.Address——(' + address.group(0)+ ')')