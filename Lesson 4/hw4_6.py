from sys import argv
from itertools import count, cycle 
for i in count(int(argv[1])):
    print(i)
    if i > int(argv[2]):
        break
    i+=1
count=0
for k in cycle(['q','s','c']):
    print(k)
    if count > int(argv[2]):
        break
    count+=1

