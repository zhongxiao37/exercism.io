def flatten(iterable):
    flattened = []
    for e in iterable:
        if isinstance(e, list) or isinstance(e, tuple):
            flattened += flatten(e)
        else:
            if not e == None:
                flattened.append(e)
    return flattened