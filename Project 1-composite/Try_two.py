import numpy as np
import csv
import math

# Initializing array and reading csv file

borehole = []
from_arr = np.array([])
to_arr = np.array([])
au = np.array([])
cmg =np.array([]) #au x width
width = np.array([]) #to minus from
with open('Compositing Data.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	next(reader)
	for row in reader:
		borehole.append(str(row[0]))
		from_arr = np.append(from_arr, float(row[1]))
		to_arr = np.append(to_arr, float(row[2]))
		au = np.append(au, float(row[3]))

# Calculating Sample Width and Width x Grade

width = to_arr-from_arr
cmg = width*au

# Set the minimum Au for the average
min_value = 1

# Function to checks the current sample is above threshold
def check_sample(i):
	if borehole[i - 1] == borehole[i] and from_arr[i] == to_arr[i - 1]:  # checking same hole and there are no gaps between sample current FROM same as previsous TO
		if au[i] >= min_value: # check for minimum Au
			return True
	return False

#test for loop
for i in range(1, len(borehole)):
	print(check_sample(i))
	