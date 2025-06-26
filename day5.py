'''def add():
    num1=int(input("enter the number : "))
    num2=int(input("enter the number : "))
    res=num1+num2
    return res
result=add()
print("result=",result)
add=result+10
print("result after 10 add=",add)'''

'''def evenodd():
    num1=float(input("enter number"))
    if num1%2==0:
        return "no is even"
    else:
        return "no is odd" 
result=evenodd()   
print(result)
print(type(result))'''

'''#prime number
def primenum():
    num=int(input("enter number"))
    cnt=2
    while cnt<=num:
        if (num%cnt==0):
            break
        cnt +=1
        print(cnt)
    if num==cnt:
        print("number is prime")
    else:
        print("number is not prime")
primenum() '''

'''#with parameter without return type
def add(num1,num2):
    result=num1+num2
    print("result=",result)
n1=int(input("enter number"))
n2=int(input("enter number"))
add(n1,n2)'''

'''#calculate the net salary
def netsalary(bs,hra,da,pf):
    nsal=bs+hra+da-pf
    return nsal
bs=int(input("enter number"))
hra=int(input("enter number"))
da=int(input("enter number"))
pf=int(input("enter number")) 
netsal=netsalary=bs,hra,da,pf  
print("netsalary is",netsal)'''

'''#with parameter with return type
def netsalary(bs,hra,da,pf):
    salary=(bs+hra+da)-pf
    return salary
salary=netsalary(25000,2000,2000,2000) 
print("salary",salary)'''

#calculate calculate
def total(s1,s2,s3):
    sum=s1+s2+s3
    return sum
    def percentage(tot):
        per=tot/3
        return per
s1=int(input("enter subject marak")) 
s2=int(input("enter subject marak"))
s3=int(input("enter subject marak")) 
sum=total(s1,s2,s3)
print("total",sum)
per=percentage(sum)
print("percentage=",per)     