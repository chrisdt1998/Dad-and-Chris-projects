import csv

borehole = []
from_arr = []
to_arr = []
au = []

with open('Compositing Data.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	next(reader)
	for row in reader:
		borehole.append(str(row[0]))
		from_arr.append(float(row[1]))
		to_arr.append(float(row[2]))
		au.append(float(row[3]))

total = 0
average = []
counter = 0
min_value = 1

for i in range(1, len(borehole)):
	if borehole[i - 1] == borehole[i] and from_arr[i] == to_arr[i - 1] and au[i] >= min_value:
		counter += 1
		total += au[i]
		if counter == 1 and au[i - 1] >= min_value:
			total += au[i - 1]
			counter += 1
	elif counter != 0:
		average.append(total/counter)
		counter = 0
		total = 0

print(average)
print(len(average))
