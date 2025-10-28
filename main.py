import csv
import random
import xml.etree.ElementTree as ET

filename = 'books-en.csv'  
with open(filename, encoding='cp1251') as f:
    rows = list(csv.DictReader(f, delimiter=';'))


title_key = 'Book-Title'
author_key = 'Book-Author'
date_key = 'Year-Of-Publication'
price_key = 'Price'

long_titles = sum(len(r[title_key]) > 30 for r in rows)
print("ans1:", long_titles)


author = input("author?:")
filter = []
for r in rows:
    try:
        
        price = float(r[price_key])
        if author in r[author_key] and price <= 200:
            filter.append(r)
    except:
        pass

print('ans2:', len(filter))
for r in filter[:3]:
    print(r[author_key], r[title_key], r[price_key])


bibs = random.sample(rows, 20)
with open('bibliography.txt', 'w', encoding='utf-8') as f:
    for i, b in enumerate(bibs, 1):
        f.write(f"{i}. {b[author_key]}. {b[title_key]} - {b[date_key]}\n")
input("press enter")

tree = ET.parse('currency.xml')
root = tree.getroot()

# Создаем словарь NumCode -> CharCode
num_code_to_char_code = {}
for val in root.findall('.//Valute'):
    num_code = int(val.find('NumCode').text)
    char_code = val.find('CharCode').text
    # Заполняем словарь
    num_code_to_char_code[num_code] = char_code

print('NumCode - CharCode:')
for n, c in num_code_to_char_code.items():
    print(f"{n} - {c}")