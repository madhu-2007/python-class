tuple=(2,3,6,6,3,79)




print(tuple(i for i in tuple  if i not in tuple and tuple.count (i)>1) )      
       