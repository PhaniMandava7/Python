print('my_module imported')

test = 'Test String'

def find_index(toSearch, target):
    for index, item in enumerate(toSearch):
        if item == target:
            return index
    return -1