DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}
qty = 20
recipe = 'omlet'
print(DATA['omlet'])
for key, value in DATA['omlet'].items():
    print(key, value * qty)

dict_e = {key: value * qty for key, value in DATA[recipe].items()}
print(dict_e)
context = {recipe: dict_e}

print(context)