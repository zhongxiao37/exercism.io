def largest(min_factor, max_factor):
    check_parameters(min_factor, max_factor)
    products = {}
    for i in range(max_factor, min_factor -1, -1):
        for j in range(i, min_factor - 1, -1):
            k = i * j
            if len(products.keys()) > 0 and k < list(products.keys())[0]:
                break
            if list(str(k)) == list(reversed(str(k))):
                if k in products:
                    products[k].append([i, j])
                else:
                    products[k] = [[i, j]]
    
    product_factors = sorted([(k, v) for k, v in products.items()])
    return product_factors[-1] if len(product_factors) > 0 else [None, []]

def smallest(min_factor, max_factor):
    check_parameters(min_factor, max_factor)
    products = {}
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            k = i * j
            if len(products.keys()) > 0 and k > list(products.keys())[0]:
                break
            if list(str(k)) == list(reversed(str(k))):
                if k in products:
                    products[k].append([i, j])
                else:
                    products[k] = [[i, j]]
    
    product_factors = [(k, v) for k, v in products.items()]
    return product_factors[0] if len(product_factors) > 0 else [None, []]

def check_parameters(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError('invalid factors')