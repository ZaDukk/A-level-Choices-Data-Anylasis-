import matplotlib.pyplot as plt

f = open("option 4 + epq .txt","r")
unsure4=0
unsureNot4=0
yes4=0
yesNot4=0
no4=0
noNot4=0

for i in range (19):
    x=f.readline().lower()
    if "n/a" in x:
        if "yes" in x:
            yesNot4+=1
        elif "no" in x:
            noNot4+=1
        else:
            unsureNot4+=1
    else:
        if "yes" in x:
            yes4+=1
        elif "no" in x:
            no4+=1
        else:
            unsure4+=1
bars=[unsure4,unsureNot4,yes4,yesNot4,no4,noNot4]
print(bars)
labels=["4 alevels maybe","3 alevels maybe","4 alevels yes","3 alevels yes","4 alevels no","3 alevels no"]
colors=["blue","blue","green","green","red","red"]
plt.title("are you doing an epq?")
plt.bar(labels,bars,color=colors)
plt.show()