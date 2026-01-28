# Zipmap should recursively create a dictionary from two lists: one of keys and one of values.
# If either list is empty, it should return an empty dictionary.
# Example: zipmap(['a', 'b', 'c'], [1, 2, 3]) should return {'a': 1, 'b': 2, 'c': 3}.
def zipmap(keys, values):
    if len(keys) == 0 or len(values) == 0:
        return {}
    res = zipmap(keys[1:], values[1:])
    res[keys[0]] = values[0]
    return res