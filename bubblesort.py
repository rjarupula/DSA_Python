#Bubble sort Algorithm Using Python Code

# Have a list of elements dynamically
#Create an empty list
data = []

# Get an input from the user for list to be sorted.
#Assign a LENGTH to list
length = int(input('Enter the size of the list'))

#Assign value to the list
for ele in range(length):
  number = input(".. ")
  if number.isdigit():
    data.append(number)
  else:
    print('Please enter numbers only!')

# Before Sort Display the list of item
print(data)

#Duplicate the List to Sort
data_copy = data[:]
#Sort the list Using Bubble Sorting
for n in range(length):
  for j in range(length-n-1):
    if data_copy[j] > data_copy[j+1]:
      data_copy[j],data_copy[j+1] = data_copy[j+1], data_copy[j]

#Print the sorted list of element
print("Port sorting list using Bubble sort \n", data_copy)
