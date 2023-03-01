#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2

def add(): 
    a= int(input ("Enter first number: "))
    print(a)
    b= int(input ("Enter second number: "))  
    print(b)
    a1=float(a) 
    b1= float(b)
    return print(a1,"+",b1,"=", a1+b1)


def subtract():
    a= int(input ("Enter first number: "))
    print(a)
    b= int(input ("Enter second number: "))  
    print(b)
    a1=float(a) 
    b1= float(b)
    return print(a1,"-",b1,"=", a1-b1)

def multiply():
    a= int(input ("Enter first number: "))
    print(a)
    b= int(input ("Enter second number: "))  
    print(b)
    a1=float(a) 
    b1= float(b)
    return print(a1,"*",b1,"=", a1*b1)

def divide():
     
  try:
    a= int(input ("Enter first number: "))
    print(a)
    b= int(input ("Enter second number: "))  
    print(b)
    a1=float(a) 
    b1= float(b)
    return print(a1,"/",b1,"=", a1/b1)
  except Exception as e:
    print(e)
    

def power():
    a= int(input ("Enter first number: "))
    print(a)
    b= int(input ("Enter second number: "))  
    print(b)
    a1=float(a) 
    b1= float(b)
    return print(a1,"^",b1,"=", a1**b1)

def reminder():
    a= int(input ("Enter first number: "))
    print(a)
    b= int(input ("Enter second number: "))  
    print(b)
    a1=float(a) 
    b1= float(b)
    return print(a1,"%",b1,"=", a1%b1)

#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3

def select_op(choice):
  if (choice=="#"):
    return -1
  elif( choice=="$"):
    return 0
  elif (choice == "+"):
    add()
    

  elif (choice=="-"):
    subtract()

  elif (choice=="*"):
    multiply()

  elif (choice=="/"):
    divide()
    print(a11,"/",b22"=", a11/b22)
    

  elif (choice=="^"):
    power()

  elif (choice=="%"):
    reminder() 

    




  

  



#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()