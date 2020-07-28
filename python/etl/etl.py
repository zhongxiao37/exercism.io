def transform(legacy_data):
    new_data = {}
    for k, v in legacy_data.items():
        for e in v:
            new_data[e.lower()] = k
    
    return new_data
