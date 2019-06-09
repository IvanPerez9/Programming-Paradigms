a =[1,2,3,4,5,6,7,8,9]

# a[start:stop:step] # start through not past stop, by step

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items


a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed

l = [1,2,5,4,2,2]
print(l.count(2)) # Veces que aparece
print(l.index(5)) # Posicion
l2 = l[:]
print(l2)