import matplotlib.pyplot as plt


slices=[]
mathsOnly=0
mathsAndSci=0
neither=0
f = open("a levels per person.txt","r")

for i in range(19):
    x=f.readline().lower()
    if "maths" in x:
        if "biology" in x or "chemistry" in x or "physics" in x:
            mathsAndSci+=1
        else:
            mathsOnly+=1
    elif "biology" in x or "chemistry" in x or "physics" in x:
        sciOnly+=1
    else:
        neither+=1


slices.append(mathsOnly)
slices.append(mathsAndSci)
slices.append(neither)
labels = ["maths only","maths and a science","neither",]
colors = ["orange","red","green"]

plt.title("A levels of each person")
plt.pie(slices,labels=labels,colors=colors,wedgeprops={"edgecolor":"black"})
plt.show()