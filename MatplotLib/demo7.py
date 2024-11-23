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

# Plot of Sepal Length
# Sepal length line plot
plt.plot(setosa_arr[:, 0], color='black', label='Setosa')
plt.plot(versicolor_arr[:, 0], color='red', label='Versicolor')
plt.plot(virginica_arr[:, 0], color='blue', label='Virginica')
plt.legend(loc='upper right')
plt.ylabel('Sepal Length (cm)')
plt.xlabel('Instance')
plt.title('Sepal length of irises by type')
plt.savefig('sepal_length_type.png')
plt.close()

# Petal length and petal width scatter plot
# plt.scatter(setosa_arr[:, 2], setosa_arr[:, 3],
# color='black', label='Setosa', marker='*’)
# plt.scatter(versicolor_arr[:, 2], versicolor_arr[:, 3],
# color='red', label='Versicolor', marker='+’)
# plt.scatter(virginica_arr[:, 2], virginica_arr[:, 3],
# color='blue', label='Virginica', marker='o’)
# plt.legend(loc='upper left')
# plt.ylabel('Petal Width (cm)')
# plt.xlabel('Petal Length (cm)')
# plt.title('Petal length and petal width of irises by type')
# plt.xlim(0,7)
# plt.ylim(0,3)
# plt.savefig('petal_length_width_scatter.png')
# plt.close()
