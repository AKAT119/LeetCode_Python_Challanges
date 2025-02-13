



def duplicateFind(a):
    di = {}
    du = []
    for i in a:
        if i or i.lower() in di:
            di[i]+=1
            if di[i] > 1:
                du.append(i)
        else:
            di[i]=1
    return du



a = [1,"Az",6,7,"az",9,10,20,6,20]
result = duplicateFind(a)
print(result)