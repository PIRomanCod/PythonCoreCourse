"""
Метод: Translate
"""

# str.translate(table)

data = "юаібщ"

symbol_map = {
    ord('ю'): "u",
    ord('а'): "a",
    ord('і'): "i",
    ord('б'): "b",
    ord('щ'): "shch"
}

new_str = data.translate(symbol_map)
print(new_str)