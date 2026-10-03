#importing the time module to further operations
import time

#importing the system module to further operations
import sys

print("\n-----TIMER AND COUNTER-----")
print("-----press Q or q to quit-----\n") 

#user choice of timer or counter
a = input("enter the type [T , C] : ")

#making it a loop so if any condition is wrong it may continue again
while True :
    #checks if users types t
    if a.lower() == "t" :
        A = int(input("\nenter the starting number: "))
        B = int(input("enter the ending number: "))
        print("\nyour time starts now")
        for i in range(A, B + 1): #b is an exclusive so b+1 is written
            #making for loop to iterate the counter
             print(f'\r timer : {i} seconds ', end="", flush=True)
            #making the output to iterate with 1 sec time gap
             time.sleep(1)
            # breaking the loop
        print ("\n----YOUR TIME IS UP!!!!----")
        break
    # checks if users types C
    elif a.lower() == "c" :
        A = int(input("\nenter the starting number: "))
        B = int(input("enter the ending number: "))
        print("\nyour counter starts now")
        for j in reversed(range(A, B + 1)) :
             #starting the counter in reverse order
             print(f'\r countdown : {j} seconds ', end="", flush=True)  #makes the time to run in one line but not iterations
             time.sleep(1)
        print("\n----TIMES'S UP----")
        break
    
    # checks user is given any nums
    elif a.isnumeric():
        print("enter t or c not integer...\n")
        a = input("enter the type [T , C] : ")
    # checks user is given empty
    elif a == "":
        print("you've entered an empty string...\n")
        a = input("enter the type [T , C] : ")
    # checks user wants to quit
    elif a.lower() == "q":
        print("----THANK YOU-----")
        sys.exit()
        # checks user is given any alpha
    elif a.isalpha():
        print("enter t or c not any other character...\n") 
        a = input("enter the type [T , C] : ")
    else:
        pass

#thank you ....    