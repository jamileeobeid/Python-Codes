#Writing a function that uses Python’s csv module to calculate the average 
def line_averages():
    with open("average.csv", "r") as filename:
        avLines=[]
        sum=0
        for line in filename:
            stripped_line= line.strip()
            stripped_line=stripped_line.split(',')
           
            for i in stripped_line:
                sum = sum + float(i)
            line_sum=sum
            print(line_sum) #printing the sum of the current line 
            print(len(stripped_line)) #printing the number of values in the current line
         
            avLines.append(line_sum/len(stripped_line)) #calculting the average and adding it to the list
            
        return avLines #returning the list that contains the average value for each row
     
def main():
    print(line_averages())

main()