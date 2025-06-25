# #split all the datatype in a different list
p=["name","DOB","hello",90.0,"false",78.2]
string=[]
integer=[]
fl=[]
boo=[]
for i in p:

    if type(i)==str:
        string.append(i)
        
    if type(i)==int:
        integer.append(i)
        
    if type(i)==float:
        fl.append(i)
         
    if type(i)== bool:
        boo.append(i)
        
print(string)
print(integer)
print(fl)
print(boo)





p=["name","DOB","hello",90.0,False,78.2]
string=[]
integer=[]
fl=[]
boo=[]
count_str=0
count_int=0
count_fl=0
count_boo=0
for i in p:

    if type(i)==str:
        string.append(i)
        count_str+=1
        
    if type(i)==int:
        integer.append(i)
        conut_int+=1

        
    if type(i)==float:
        fl.append(i)
        count_fl+=1
         
    if type(i)== bool:
        boo.append(i)
        count_boo+=1
        
# print(string,"string")
# print(integer,"int")
# print(fl,"float")
# print(boo,"bool")
print(count_str)
print(count_int)
print(count_fl)
print(count_boo)