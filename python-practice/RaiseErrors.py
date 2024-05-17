# raising value error

def raise_error1():
    try:
        rollNum= int(input("Please enter a number: "))

        # Extra Condition checking on the user input Value
        # We want to restrict the user to input a number greater than zero
        if(rollNum<=0):
            raise ValueError()
    except ValueError:
        print("Value Exception thrown")

    print("This is normal statement outside try-except")



#password should be between 10 and 20 characters long
def raise_error2():
    try:
   
        password= input("Please enter your Password: ")
        length=len(password)
        print("The password you wrote is " , length , " characters long")
        if(length>10 and length< 20):
        #if(20>len(password)>10):
            print(password)
            print("correct length of password entered")
        else:
            raise ValueError()
    except ValueError:
        print("password should be 10 to 20 chracters long")



'''ReRaising Value Error'''

#make validate() method detailed 
def validate(userid, password):
    if(userid=="1234" and password=="pass"):
        print("user id and password are validated")
        return True
    else:
        return False


def login_reraise():
      
    attempts = 4
    while True:
       userid = input("Enter userid: ")
       passwd = input("Enter password: ")
       try:
          if(validate(userid, passwd)):
              print('true')
          else:
              raise ValueError
       except ValueError as ve:
          #attempts -= 1
          attempts=attempts-1
          if attempts > 0:
            print("Invalid.", attempts,"attempts remaining...")
          else:
            raise ve
             
     


def main():
    raise_error1()
    raise_error2()
    #login_reraise()
main()