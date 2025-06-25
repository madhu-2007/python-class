#print only duplicate elements :
list=[2,3,6,6,3,7]
result=[]
for i in list:
    if i not in result and list.count (i)>1:

        result.append(i)
print(result)       
       
