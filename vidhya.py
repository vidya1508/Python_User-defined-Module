def calculator(a,b,str1):
    if str1=='+':
        print("Addition:",end="")
        return a+b
    elif str1=='*':
        print("Multiplicaton:",end="")
        return a*b
    elif str1=="-":
        print("Substraction:",end="")
        return a-b
    elif str1=="/":
        print("Division:",end="")
        return a/b
    else:
        return "enter valid operator"
def nfibonacci(n):
        if n<0:
           print("Invalid")
        elif(n==0):
            return 0
        elif n==1 or n==2:
            return 1
        else:
            return nfibonacci(n-1)+nfibonacci(n-2)
def leapyear(n):
    if((n%4==0 and n%100!=0) or n%400==0):
        return "Leap Year"
    else:
        return "Non Leap Year"
def reverse(n):
        result=0
        while(n!=0):
          digit=n%10
          result=result*10+digit
          n=n//10
        return result
def palindrome(n1):
    result1=0
    while(n1!=0):
     digit1=n1%10
     result1=result1*10+digit1
     n1=n1//10
     if(int(result1)==int(n1)):
         return "Palindrome"
    return "Not Palindrome"
def armstrong(n):
    sum=0
    for i in n:
        sum=sum+int(i)**3
    if(sum==int(n)):
        return "Armstrong"
    else:
        return "Not Armstrong"
def vowels(w):
    v="aeiou"
    c=0
    for i in w:
        if i in v:
            c=c+1
    return c
def nsum(n):
    if n==0:
        return 0
    return n+nsum(n-1) 
def nfact(n):
    if n==0:
        return 1
    return n*nfact(n-1)
def anagram(str1, str2):
    if(sorted(str1.lower()) == sorted(str2.lower())):
        return "Anagram"
    return "Not Anagram"