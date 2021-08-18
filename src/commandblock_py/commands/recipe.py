def give(selector:str = '@s', recipe:str = '*'):
    return f'recipe give {selector} {recipe}'

def take(selector:str = '@s', recipe:str = '*'):
    return f'recipe take {selector} {recipe}'