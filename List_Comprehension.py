groups = [[1, 2], [3, 4]]

for g in groups:
    for elements in g:
        print (elements, end =' ')

c = [elements for g in groups for elements in g]