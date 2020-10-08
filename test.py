l = [1,2,3,4,5,6,7]
out = list()
for i in l:
    for j in l:
        if(i + j == 7):
            out.append(tuple([i, j]))

print(out)
