with open('input.txt') as inp:
    M = [(int(val),int(num)) for num,val in enumerate(inp.read().split())]
M.pop(0)
C = M.copy()
for ind,val in enumerate(M):
    if ind == len(M)-2:
        if min(C[ind], C[ind+1]) != C[ind]:
            C[ind], C[ind+1] = C[ind+1], C[ind]
            with open('output.txt', 'a') as out:
                out.write('Swap elements at indices '+str(ind+1)+' and '+str(ind+2)+'.\n')
    elif ind == len(M)-1: 
        break    
    temp = min(C[ind+1:])
    if C[ind][0] > temp[0]:
        tempind = C.index(temp)
        C[ind],C[tempind] = C[tempind], C[ind]
        with open('output.txt', 'a') as out:
            out.write('Swap elements at indices '+str(ind+1)+' and '+str(tempind+1)+'.\n')
del(M)
L = []
for i in C:
    L.append(str(i[0]))
with open('output.txt', 'a') as out:
    out.write('No more swaps needed.\n')
    out.write(' '.join(L))
