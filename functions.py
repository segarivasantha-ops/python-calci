import time
#programs on functions
print("\n======1.GREETINGS=====\n")
name=input("enter your name: ")
age=int(input("enter your age: "))
def greeting(name , age):      #name , age
    print(f"\nHAPPY BIRTHDAY TO YOU {name}\n"
          f" and you're now turned {age} years old")
greeting(name,age)
time.sleep(1)

print("\n======2.SUMMING=====\n")   #summing of two nums using return statement
a = int(input("enter your first number: "))
b = int(input("enter your second number: "))
def summing(a,b):    #num1 , num2
    return a+b
print(f"your sum of {a} and {b} is : " , summing(a,b))
time.sleep(1)

print("\n======3.EVEN OR ODD=====\n")
A=int(input("enter your number: "))
def even_or_odd(A) :    #even or odd with return statement
    if A%2==0 :
        return "EVEN"
    else :
        return "ODD"
print(f" the given num {A} is : " , even_or_odd(A))
time.sleep(1)

print("\n======4.MAXIMUM=====\n")
a = int(input("enter your first number: "))
b = int(input("enter your second number: "))
c = int(input("enter your third number: "))

def maximum(a, b, c): #m1 , m2 , m3 max among entered nums
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:  #though any 2 nums are equal it will return the first one
        return b
    else:
        return c

print(f"the max among the {a} , {b} , {c} is : " , maximum(a, b, c))
time.sleep(1)

print("\n======4.VOWELS=====\n")  #counting of vowels in a string using return statement
string=str(input("enter your string or word : "))
v =['a' , 'e' , 'i' , 'o' , 'u']
def vowels(string) :      
    count = 0
    for i in string :
        if i in v :
            count += 1
    return count 
print(vowels(string))         

    
print("\n=====MINI PROJECT=====\n")   #calcy using functions and return statement
a=int(input("enter your first number: "))
b=int(input("enter your second number: "))
c=int(input("enter your third number: "))
print()
def add(a,b,c) :  #p1 , p2 , p3
    return a+b+c
print(f"ADDITION of {a} , {b} and {c} is :" , add(a,b,c))

time.sleep(1)
print()
def sub(a,b,c) :
    return a-b-c
print(f"SUBSTRACTION of {a} , {b} and {c} is :" , sub(a,b,c))
print()
time.sleep(1)

def mul(a,b,c) :
    return a*b*c
print(f"PRODUCT of {a} , {b} and {c} is : " , mul(a,b,c))
print()
time.sleep(1)

def div(a,b) :
    if b == 0:
        return "infinity"
    else:
       return a/b
print(f"DIVISION of {a} and {b} is : " , div(a,b))
print()
time.sleep(1)
print("=====THANK YOU=====") #thanks....