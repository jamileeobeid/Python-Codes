def opener():
    
    #asking the user to input real file name with extension
    filexxx = input("Enter any existing filename with extension:\n")
    var=True
    #opening the file for the first time using open() function
    fileHandler = open(filexxx, "r")

    # Try to open the same file again, so it should raise error
    try:
        with open("filename", "r") as file:
            if var is True: 
                #printing the success message
                print("File has opened for reading.")
                print("True")

    #raising an error if the file is opened before
    except IOError:
        print("File has opened already.")
        print("False")

opener()