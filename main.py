import csv
import random
import xml.etree.ElementTree as ET

FILENAME = 'books-en.csv'  
with open(FILENAME, encoding='cp1251') as f:
    rows = list(csv.DictReader(f, delimiter=';'))


TITLE_KEY = 'Book-Title'
AUTHOR_KEY = 'Book-Author'
DATE_KEY = 'Year-Of-Publication'
PRICE_KEY = 'Price'

long_titles = sum(len(r[TITLE_KEY]) > 30 for r in rows)
print("ans1:", long_titles)


author = input("author?:")
filter = []
for r in rows:
    try:
        
        price = float(r[PRICE_KEY])
        if author in r[AUTHOR_KEY] and price <= 200:
            filter.append(r)
    except KeyError:
        pass

print('ans2:', len(filter))
for r in filter[:3]:
    print(r[AUTHOR_KEY], r[TITLE_KEY], r[PRICE_KEY])


bibs = random.sample(rows, 20)
with open('bibliography.txt', 'w') as f:
    for i, b in enumerate(bibs, 1):
        f.write(f"{i}. {b[AUTHOR_KEY]}. {b[TITLE_KEY]} - {b[DATE_KEY]}\n")
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