strin =  open("/home/hamed/data.txt","r")
string = strin.read()


strind =  open("/home/hamed/dictunary.txt","r")
stringd = strind.read()

c = 0
list_ = []
words = string.split()
wordsd = stringd.split()

for allwords in words :
     for allwordsd in wordsd :
          if (allwords == allwordsd):
               #print (allwords)
               list_.append(allwordsd)



output = []
seen = set()
for value in list_:

     if value not in seen:
          output.append(value)
          seen.add(value)
print (output)
