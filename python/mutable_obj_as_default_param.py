def f(v = []):
    return v

a = f()
b = f()

a.append(1)

print(a == b) # don't use mutable obj as default param
print(a is b)

c = f()
d = f()

c += [1]
print(id(c))
print(id(d))
print(c == d)
print (c is d)

