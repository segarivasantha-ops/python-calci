import sys                                                   #importing system sys module
print("\n------press q to quit------\n")
                                                             #valuing the 1st num
while True : 
    a=input("enter the first integer : ")                     # entering into loop which is true
    if a.lower() =="q" :                                      #checks user is quiting
        print("-----THANK YOU-----")
        sys.exit()                                            #makes the entire code to end as user wanted
    elif a == "" :                                            #checks if a isn't entered
        print("enter the a integer value ")
        continue                                              #makes the loop to continue 
    elif a.isnumeric() == False:                              #checking user giving as int
        print("enter the a integer value")
        continue
    elif a == "0" :                                           #checking user giving as int
        print("enter the a integer value other than 0")
        continue
    else :
        print(f"your value is {a}")
        break

#selecting the second num
while True :
    b=input("\nenter the second integer : ")
    if b.lower() == "q":
        print("-----THANK YOU-----")
        sys.exit()
    elif b == "" :
        print("enter the b integer value ")       #same as the above input
        continue
    elif b.isnumeric() == False:
        print("enter the b integer value")
        continue
    elif b == "0":
        print("enter the b integer value other than 0")
        continue
    else:
        print(f"your value is {b}")
        break

print("\n----enter your operator (+,-,/,%,*)----")
print(f"-----your nums are a is {a} and b is {b}-----\n")
#operation selection                                                                   
while True :
    A=int(a)                                                          #making the above variables as int
    B=int(b)   
    c = input("enter operator from ['+','-','*','/','%'] : ") 
    if c == "" :
        print("enter your operator from given above...")
        continue
    elif c.lower() == "q":
        print("-----THANK YOU-----")
        sys.exit()
    elif c not in  ['+','-','*','/','%']  :
        print("you have to select only from '+','-','*','/','%' operators only...")
        continue
    elif c=='+':                                          
        print(f"sum of {A} and {B} is , {A+B}")
        print()
        continue
    elif c=='-':
        print(f"sub of {A} and {B} is , {A-B}")
        print()
        continue
    elif c=='*':
        print(f"mul of {A} and {B} is , {A*B}")
        print()
        continue
    elif c=='%':
        print(f"remainder of {A} and {B} is , {A%B}")
        print()
        continue
    else :
        print(f"div of {A}and {B} is {A/B}")
        print()
        continue          

#thank you....
