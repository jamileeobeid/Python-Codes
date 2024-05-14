def login():

    attempts = 3
    password = "pass"

    while True:
        try:
            int(input("Enter your ID: "))
            user_input = input("Enter your password: ")

            if user_input == password:
                print("correct password")
                break
        
            elif attempts > 0:
                attempts = attempts - 1
                print("Incorrect password. Try again.")

            elif attempts == 0:
                print("maximum number of attempts reached")
                break

            else:
                raise VE
            
        except ValueError as VE:
            print("ID can only be an integer")

login()