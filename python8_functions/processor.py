import string


def process_numbers(lista):
    array = []
    if isinstance(lista, list) == False:
        return array

    
    for item in lista:
        if isinstance(item,int):
            array.append(item)
        elif isinstance(item,str):
            if item.isnumeric():
                array.append(int(item))

    array.sort()
    return array


def process_names(lista):
    array = []
    if isinstance(lista,list) == False:
        return array
    for item in lista:
        if isinstance(item,str):
            if item.isnumeric() == False:
                array.append(item)
    array.sort()
    return array