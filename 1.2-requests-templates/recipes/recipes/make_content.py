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


def make_content(DATA, recipe_name, qty):
    """
    На вход получает словарь с рецептами, название блюда
    и количество порций, а возвращает словарь для указанного названия блюда
    с расчетом инградиентов с учетом количества порций.
    """

    if recipe_name in DATA.keys():
        dict_recipe = {key: round(value * int(qty), 2) for key, value in DATA[recipe_name].items()}
        return dict_recipe
    else:
        dict_empty = {}
        return dict_empty
