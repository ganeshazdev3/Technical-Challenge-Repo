def getKey(object: dict):
    keys = list(object)
    if len(keys) != 1:
        raise Exception('either multiple keys or empty dict found')
    else:
        return keys[0]


def getNestedValue(object: dict, key: str, isFound = False):
    # print(object, key, isFound)
    if type(object) is not dict and not isFound:
        return None
    if (isFound or (key in object.keys())) :
        if type(object[key]) is dict:
            return getNestedValue(object[key], getKey(object[key]), True)
        else:
            # print(f'object[getKey(object)]: {object[getKey(object)]}')
            return object[getKey(object)]
    else:
        nestedKey = getKey(object)
        return getNestedValue(object[nestedKey], key, False)

if __name__ == '__main__':
    object = {'g': {'h': {'i': 'j'}}}
    value = getNestedValue(object, 'i')
    print(value)
