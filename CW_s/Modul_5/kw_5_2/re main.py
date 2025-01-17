# . - один будь-який символ, крім рядка \n
# ? - 0 або 1 входження шаблону зліва, тобто він ставиться після чогось (після виразу)
# + - 1 і більше входжень шаблону зліва, він теж ставиться після виразу
# * - 0 і більше входжень шаблону зліва
# \w - будь-яка цифра або буква [a-zA-Z0-9_] (\W - все, крім букви або цифри [^a-zA-Z0-9_])   \ - це екранований символ
# \d - будь-яка цифра [0-9] (\D - все, крім цифри [^0-9])
# \s - будь-який символ пробілу [\t\n\r\f\v] (\S - все, крім не пробельного символу [^\t\n\r\f\v])
# \b - межа слова (границя слова)
# [..] - один із символів у дужках ([^..] - будь-який символ, крім тих, що у дужках)
# \ - екранування спец.символів (приклад: \. - означає точку або \+ - знак "плюс"),
# тобто використовується для пошуку символів які вже зайняті
# ^ і $ - початок і кінець рядка відповідно (^ це не те саме що і [^])
# {n,m} - від n до m входжень (приклад: {,m} - від 0 до m), приклад {\d,3} - буде шукати 3 цифри 
# a|b - відповідає a або b
# () - групує вираз і повертає знайдений текст, використовуються для пошуків ссилок, email. З ними все складно
# \t, \n, \r - символ табуляції, нового рядка та повернення каретки
