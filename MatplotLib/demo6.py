# Data Visualization Example
# Reading the File

def read_data(filename, data) :
  
  # Read in data from file line by line
  infile = open(filename, 'r')
  line = infile.readline()
  
  while line :
    line = line.strip()
    data.append(line.split(','))
    line = infile.readline()
    infile.close()
    
  # Convert continuous attributes to float and class labels to integers
  for i in range(0, len(data)) :
    data[i][0] = float(data[i][0])
    data[i][1] = float(data[i][1])
    data[i][2] = float(data[i][2])
    data[i][3] = float(data[i][3])
    data[i][4] = int(data[i][4])
