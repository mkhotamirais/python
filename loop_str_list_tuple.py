# STR, LIST, TUPLE
# String dan tuple itu ordered immutable/unchangeable allow duplicate value, list itu mutable
# Ketiganya punya kemiripan, yaitu: len, in, concat + *, not in, indexing, slicing, methods
# Kalau mau ubah value string atau tuple, ubah dulu tipenya jadi list.

x = "Hello World!"
x1 = "Hello"
x2 = "World!"
y = ('One', 'Two', 'Three', 'Four', 'Five')
z = ['six', 'seven', 'eight', 'nine', 'Ten']
xx = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = [len(x), len(y), len(z)]
b = ['Hello' in x, 'One' in y, 'Six' in z, 'Hello' not in x]
# Slicing x[start:end:step]
# default start = 0, default end = len, default step = 1
c = [xx[2], xx[2:5], xx[8:], xx[5::2], xx[-2], xx[-5:-2], xx[2:-2:2]] # indexing dan slicing

# LOOP dengan bentuk biasa dan list comprehension
# loop_comprehension = [expression for item in iterable if condition == True] # condition optional

## Loop through the items
for i in x:
    pass
    # print(i)
# [print(i) for i in x]
loop_items = [i for i in x]

## Loop through the index numbers
for i in range(len(z)):
    pass
    # print(z[i])
# [print(z[i]) for i in range(len(z))]
loop_index = [z[i] for i in range(len(z))]

# Loop with condition.
for i in z:
    if 'i' in i:
        pass
        # print(i)
# [print(i) for i in z if 'i' in i]
loop_condition = [i for i in z if 'i' in i]
loop_condition_upper = [i.upper() for i in z if 'i' in i]

# break & continue
for i in xx:
    if i == 4: break
    pass
    # print(i)            # 0 1 2 3
for i in xx:
    pass
    # print(i)            # 0 1 2 3 4 
    if i == 4: break
for i in xx:
    if i >= 4: continue
    pass
    # print(i)            # 0 1 2 3

## Using a while loop
w = 0
while w < len(z):
    print(z[w])
    w +=1
# While loop with break and continue

# range(start, end, step)
for i in range(5):    # 0 1 2 3 4
    pass
    # print(i)
for i in range(2, 5): 
    pass
    # print(i)           # 2 3 4
for i in range(2, 10, 2): 
    pass
    # print(i)          # 2 4 6 8

# else di loop
for i in z:
    pass
    # print(i)
else:
    pass
    # print('Done')

# nested loop
for i in x1:
    for j in x2:
        pass
        # print(i, j)

# Concat + dan * berlaku untuk str, list, tuple
# .append dan .extend hanya untuk list
list_concat = z.extend(['six', 'seven'])  # menambah item list dari list lain
for i in z:
    pass
    # z.append(i)  # menambah item list di akhir
# [z.append(['eight', 'nine']) for y in [z]]  # menambah item list di akhir

# match expression:
#     case 1:
#         # code
#         pass
#     case 2:
#         # code
#         pass

