# Data Visualization Example
# Creating the Arrays

# make an empty data List
data = []
read_data('iris.csv', data)

# Divide up the data set by type of iris
setosa = []
versicolor = []
virginica = []

for instance in data :
  if(instance[4] == 1) :
    setosa.append(instance)
    elif(instance[4] == 2) :
    versicolor.append(instance)
  else :
    virginica.append(instance)
    # convert to numpy arrays
    setosa_arr = np.array(setosa)
    versicolor_arr = np.array(versicolor)
    virginica_arr = np.array(virginica)
