def minmax(data):
    s=data[0]
    g=data[0]
    for n in data:
        if n>s:
         s=n
        elif n<g:
         g=n
    return g,s
print(minmax([6,3,18,23,10,9]))