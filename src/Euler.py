import math        

'''
Created on Sep 14, 2011

@author: srinivas reddy thatiparthy
'''
"""
    generates the fibonacci numbers until upper limit
"""
def genfibo(upper):
    i,j=1,2    
    while i<upper:        
        yield i
        i,j=j,(i+j)
    
"""
the trianle number sequence is .. 1 3  6 10 15 21
"""
def gentrianglenum():
    yield 1
    summation=1
    i=2
    while True:
        summation,i=summation+i,(i+1)       
        yield summation

"""def calnoofdivisors(n):        
    count=1
    """
    
        
def sumofprimesbelow2million():
    summation=0
    for i in genprime():
        if(i<2000000):
            summation+=i
    return summation

"""
function to generate infinite prime numbers!!!
"""
def genprime():
    yield 1
    yield 2
    x=3
    while True:
        if(no_of_multipliers(x)):
            yield x
        x=x+2


def no_of_multipliers(x):
    count=0
    for i in range(1,int(math.sqrt(x))+1,2):
        if(x%i==0):
            count=count+1
    if(count>1):
        return False
    return True
    
"""
The lcm and gcd functions 
"""
def lcm(a,b):
    return a*b/gcd(a,b)

def gcd(a,b):
    while b>0:
        a,b =b,a%b
    return a

"""
A function to check whether a number is a palindrome or not!!!
"""
def ispalindrome(num):
    resultnum=0
    temp = num
    while num !=0:
        x,y = divmod(num,10)
        resultnum=resultnum*10+y
        num=x
    return temp == resultnum

"""
smallest divisor for numbers between 1 ,2,3,.....20.
"""
def min_divisor():
    x=1
    for i in range(1,21):
        x=lcm(x,i)
    print x
    

"""

"""
def diff_squaresofsum_and_sumofsquares(n):
    sumofsquares = (n*(n+1)*(2*n+1))/6
    sumofnum = (n*(n+1))/2
    squaresofsum = sumofnum*sumofnum
    return  squaresofsum- sumofsquares


def tenthousandonethprime():
    count=0
    for i in genprime():
        count=count+1
            #print i
        if(count==10001):
            print "10001th prime is :" ,i
            break
         
"""
 problem #1
"""    
def sumbyfilter():    
    return sum([i for i in range(1,1000) if i%5==0 or i%3==0])

"""
problem #2
"""        
def fibo_sum():
    return sum(filter(lambda a: a%2==0, genfibo(4000000)))

def gen_prime_reverse(num):
    if(num%2==0):
        num=num-1     
    for x in range(num-1,1,-2):        
        if(num%x==0 and no_of_multipliers(num/x)):
            yield x

"""
is there a better way to do it,other than this seemingly brute force way?
"""        
def largest_three_digit_palindrome():
    import itertools
    listing = itertools.product(range(999,500,-1),repeat=2)
    palindrome,tempx,tempy=0,0,0 
    for x,y in listing:
        temp=x*y        
        if(ispalindrome(temp)):
            if(temp>palindrome):
                palindrome,tempx,tempy=temp,x,y
    print palindrome,tempx,tempy
    

def product_of_five_digits(largestring):
    import itertools
    largest=0
    window=0
    temp=1
    for i in largestring[0+window:5+window]:
        temp=temp*int(i)
        if(largest<temp):
            largest=temp
        window+=5
    return largestring

  
      
        
    


if __name__ == '__main__':
   print product_of_five_digits("1234567899") 
    
        