num=int(input())

count=0
sum=0

for i in range(1,num+1):
    if i%3==0:
        count=count+1
        sum=sum+i
print("3배수 개수",count)
print("3배수 총합",sum)