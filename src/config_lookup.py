def find_key(obj, key):
    """
    Recursively search for a key in nested dictionaries, lists, or tuples.
    Returns the first value found in a left-to-right, top-down search.
    Returns None if the key is not found.
    """
    if isinstance(obj, dict):
        if key in obj:
            return obj[key]
        for v in obj.values():
            result = find_key(v, key)
            if result is not None:
                return result
    elif isinstance(obj, (list, tuple)):
        for item in obj:
            result = find_key(item, key)
            if result is not None:
                return result
    # ignore other types
    return None
