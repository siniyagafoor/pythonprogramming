a=input("enter sentence\n")
b=input("\n enter the word to search\n")
list=a.split()
count=0
for w in list:
    if w==b:
       count=count+1
print("count",count)
