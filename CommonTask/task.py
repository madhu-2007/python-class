data = [
    {"name": "AA", "score": [78, 98, 76]},
    {"name": "BB", "score": [67, 56, 45]},
    {"name": "CC", "score": [45, 68, 94]},
]
k=[]
for student in data:
    name = student["name"]
    scores = student["score"]
    average = sum(scores) / len(scores)
    status=""
    if average >90:
        status="excellent"
    elif average >80:
        status="verygood"
    elif average >70:
        status=" good"
    elif average >60:
        status="average"
    else:
        status="poor"      
    
     
    k.append({"name":name,"average":average,"status":status})
print(k)
  

 


    








