a=['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
x, y, z=[input() for i in range(3)]
res=(((a.index(x)*10)+a.index(y))*(10**a.index(z)))
print(res)