#finding factorial using recursion
def factorial(n):

    #BASE CASE
    if n==0 or n==1:
        return 1
    
    return factorial(n-1) * n

print(factorial(5))




#using recursion to search in an array
def SearchRecursively(arr, current_index, target):

    #BASE CASE 
    if current_index < 0:
        return None
    
    if arr[current_index]== target:
        return current_index
    
    return SearchRecursively(arr, current_index-1, target)


def main():

    arr= [10, 20, 30, 40, 50, 60, 70]
    target= 40
    result= SearchRecursively(arr, 6, target)
    
    if result != None:
        print("target found at index:", result)

    else:
        print("target is not found")

main()



#we want to take a string and start reading from it's 2nd index, all even index characters
def evens_only(a_string):

    #BASE CASE
    if a_string == "":
        return ""
    
    return a_string[0] + evens_only(a_string[2:])

print(evens_only("gcis123"))



#drawing 5 circles inside of each other using recursion
import turtle as t

def recursive_circles(radius, n):

    #BASE CASE
    if n == 0:
        return None
    
    else:
        t.penup()
        t.goto(0, -radius)
        t.pendown()
        t.circle(radius)
        t.hideturtle()

        recursive_circles(radius/2, n-1)

recursive_circles(100, 5)
input("press enter to continue") #keeping screen open until user closes it



#sum of a list using recursion
def recursive_addition(a_list):

    #BASE CASE
    if len(a_list) == 0:
        return 0
    
    return a_list[0] + recursive_addition(a_list[1:])

print(recursive_addition([2, 6, 7, 8, 5]))



#finding the power on an integer using recursion
def exponent(n, a):

    if n == 1:
        return a
    
    return exponent(n-1, a) * a

print(exponent(3, 5))