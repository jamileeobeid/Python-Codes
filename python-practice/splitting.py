a_string = "G,T,R,S,-,9,1,1"

tokens = a_string.split(",") #we will split wherever there is a comma

for token in tokens:
    print(token, end=' ')