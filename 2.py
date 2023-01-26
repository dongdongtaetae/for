num=int(input())

for i in range(2,num+1):
    isPrime=True
    for j in range(2,i):
        if i%j==0: #i>j
            isPrime=False
    if isPrime==True:
        print(i, end=" ")


        
num=int(input())

for i in range(2,num+1):
    isPrime=1
    for j in range(2,i):
        if i%j==0:
            isPrime=0
    if isPrime==1:
        print(i, end=" ")