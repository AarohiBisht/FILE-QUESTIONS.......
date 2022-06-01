# files-question2

# Aapne jo pichle question mein (Question 1) file download kari hai,
# usko read karke usme number of lines count kar ke print karein.
# Aapne sirf uss file ki number of lines Count karne ka code likhna hai................

#### USING FOR LOOP...........................................

f=open("people1-exercise.txt","r")
a=f.readlines()
# print(a)
count=0
for i in a:
    count+=1
print(count)

#### USING WHILE LOOP..........................................

f=open("people1-exercise.txt","r")
a=f.readlines()
# print(a)
count=0
i=0
while i<len(a):
    count=count+1
    i=i+1
print(count)

