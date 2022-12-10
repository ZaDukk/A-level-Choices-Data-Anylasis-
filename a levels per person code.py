import matplotlib.pyplot as plt
from collections import Counter

arr=[]

f=open("everyones a levels.txt","r")

for i in range(69):
    current = f.readline().lower()
    arr.append(current)
    
aLevelDict=Counter(arr)

bars=[]
values=[]
yAxis=[]
for key, value in aLevelDict.items():
    bars.append(key)
    values.append(value)
    
for i in range(0,17):
    yAxis.append(i)
plt.bar(bars,values)
plt.xticks(rotation=30)
plt.yticks(yAxis)
plt.show()