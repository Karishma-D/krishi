print("welcome to python")
list=[1,2,3,4,5,6]
list2=[]
list3=[]
for i in list: 
  p=i*2
  list2.append(p)
  
print(list2)  


for j in list2:
  l=j/2
  list3.append(l)
  
print(list3) 

if list2==list3:
  print("Kya chutiyapa hai")
else:
  print("mand buddhi saala")
  
