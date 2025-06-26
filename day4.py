#without parameter without returns
'''def add():
    num=int(input("enter number"))
    num1=int(input("enter number"))
    result=num+num1
    print("result:",result)
add()'''

    #seperate the digits  of number
'''def digit():
    num=int(input("enter number"))
    rem=0
    while num>0:
        rem=num%10
        print(rem)
        num=int(num/10)
digit()'''    

#reverse number
'''def digits():
    num=int(input("enter number"))
    rem=0
    sum=0
    while num>0:
        rem=num%10
        sum=(sum*10)+rem
        print(sum)
        num=int(num/10)
        print(sum)
digits()'''  

#palindrome number
'''def digits():
    num=int(input("enter number"))
    temp=num
    res=0
    sum=0
    while num>0:
        res=num%10
        sum=(sum*10)+res
        num=int(num/10)
        if(temp==sum):
            print("number is palindrome")
        else:
            print("number is not palindrome")
digits()'''   

#armstrong number
'''def digits():
    num=int(input("enter number"))
    temp=num
    rem=0
    sum=0
    while num>0:
        rem=num%10
        sum+=(rem*rem*rem)
        print(sum)
        num=int(num/10)
        if(temp==sum):
            print("number is armstrong number")
        else:
            print("number is not armstrong number")
digits()'''  

#calculate the power
'''def digits():
    num=int(input("enter number"))
    num1=int(input("enter number"))
    while num>0:
        print(num*num)
    print(num)
digits()'''   

def powercalculation():
    num=int(input("enter number"))
    p=int(input("enter number"))
    sum=1
    while p>0:        
        sum*=num
        print(sum)
        p-=1
    print("Sum : ",sum)
powercalculation()    
