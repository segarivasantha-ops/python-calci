while True :
      #defining the first number
      num1=input('enter the 1st num : ')
      if num1=='':  #when empty input is given
         print('your num is not entered')
         continue
      else :
         pass
      #making sure the first number is an integer
      num1=int(num1)

      if num1==0 or num1<0:
         print('your num should above 0')
         continue
      else :
         pass
      #defining the second number
      num2=str(input('enter the 2nd num : '))
      if num2=='':  #when empty input is given
         print('your num is not entered')
         continue
      else :
         pass
      #making sure the second number is an integer
      num2=int(num2)
      if num2==0 or num2<0:
         print('your num should above 0')
         continue
      else :
         pass
      #selecting the operator
      c=input('enter your operator (+,-,*,%,/,q) : ')
      if c=='+':
         print(f'the sum of {num1} and {num2} is {num1+num2}')
      elif c=='-':
         print(f'the sub of {num1} and {num2} is {num1-num2}')
      elif c=='*':
         print(f'the mul of {num1} and {num2} is {num1*num2}')
      elif c=='%':
         print(f'the quo of {num1} and {num2} is {num1%num2}')
      elif c=='/':
         print(f'the div of {num1} and {num2} is {num1/num2}')
      elif c=='':
         print('your operator is not entered')
         continue   
      else:
         break
      print('thank you for using this calculator program')
      #asking the user if they want to do again
      do_again=input('do you want to do again (y/n) : ')  
      if do_again=='y':
         continue 
      else:
         break  