#increment
'''i=1
while i<=10:
    print(i)
    i=i+1'''

    #decrement
'''i=10
while i>=0:
    print(i)
    i-=1'''

'''i=77
while i<=100:
    print(i)
    i=i+1'''

'''i=150
while i>=100:
    print(i)
    i-=1'''

    #for loop:print 1 to 10
'''for i in range(1,11):
    print(i)'''

    #print 10 to 1
'''for i in range(10,0,-1):
    print(i) '''   

    #print 1 to 100 even number
'''i=1
while i<=100:
    if i%2==0:
        print(i)
    i+=1'''

    #using for loop
'''for i in range(1,101):
    if i%2==0:
        print(i)'''

        #odd number
'''for i in range(1,101):
    if i%2==1:
       print(i)'''

#create table of users input number
'''num=int(input("enter number"))
for i in range(1,11):
    print(num,'x',i,'=',num*i)'''

#create table using while loop
'''i=1
num=int(input("enter number"))
while  i<10:
    print(num,'x',i,'=',num*i)
    i+=1'''

'''num=int(input("enter number"))
for i in range(num,num+11):
    print(i)'''

    #1 to 10 addition
'''res=0
for i in range(1,11):
    res=res+i
    print(res) ''' 

#factorial
'''res=1
num=int(input("enter number"))
for i in range(1,num+1):
    res=res*i
    print(i) '''    

#check prime number
'''num=int(input("enter number"))
cnt=2
while cnt<=num:
    if num%cnt==0:
        break
    cnt+=1
print("counter",cnt)
if(cnt==num):
        print("number is prime")
else:
        print("number is not prime")'''    

  # 1 to 1000 prime
'''for num in range(2,1001):
    prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            prime=False
            break
    if prime:
        print(num)'''      
        