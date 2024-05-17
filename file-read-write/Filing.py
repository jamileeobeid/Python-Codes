# Read File 
def read_file():
    with open("example2.txt", "r") as file1:
                       
        #Lines= file1.readlines()
        Line= file1.readlines()
    return Line
    

# Write in a File
def write_file():

    #taking input from user
    name= input("enter your name: ")

    with open("sample.txt", "w") as file2:
        file2.write("Writing in a file")
        file2.write("\n")
        file2.write("Hello "+name+ "!")
        file2.write("Welcome to GitHub")
    

# Error Handling
def ErrorHandling():
        try:
            with open("NOFILE.txt", "r") as file3:                       
                Line= file3.readlines()
                print(Line)
        except FileNotFoundError:
            print("File is not found.. please create the file")

        print("I am having no issues to be printed")

def main():
    returnedOutput= read_file()
    print(returnedOutput)
    write_file()
    ErrorHandling()
    
main()