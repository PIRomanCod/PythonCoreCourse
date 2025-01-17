'''
Задача
'''

import re

string = "Нільс Бор народився в родині професора фізіології Копенгагенського університету Християна Бора (1858—1911), "\
         "й Еллен Адлер (1860—1930). Батьки Бора одружилися 1881 року. Батька Нільса Бора двічі висували кандидатом "\
         "на Нобелівську премію з фізіології або медицини[6]. Мати була донькою впливового та вельми заможного "\
         "єврейського банкіра і парламентаря-ліберала Давида Баруха Адлера[da] (1826—1878) і Дженні Рафаел (1830—1902) "\
         "із британської єврейської банкірської династії Raphael Raphael & sons[en][7]."


# Знайти перші дві букви кожного слова
# result = re.findall(r'\w{2}', string)
result = re.findall(r'\b[A-ZА-Яа-яa-zіЇ]{2}', string)
print(result)

# Знайти пари років хххх-хххх
# result = re.findall(r'[\d]{4}—[\d]{4}', string)
result = re.findall(r'\d{4}—\d{4}', string)
print(result)

result = re.findall(r"(\d{4})—(\d{4})", string)  # все що в дужках е захват групи
print(result)
result = re.findall(r"(\d{4})(—)(\d{4})", string)  # все що в дужках е захват групи
print(result)