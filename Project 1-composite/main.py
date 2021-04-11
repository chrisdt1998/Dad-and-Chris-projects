import numpy as np
import csv
import math

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

width = to_arr-from_arr
cmg = width*au

# print(width, cmg)

#initialising arrays and variables
cmg_total = 0
cmg_total_arr = []
average = []
width_total = 0
width_total_arr= []
min_value = 1
temp_cmg_total = 0
temp_width_total = 0
borehole_ave = []
from_arr_ave = []
to_arr_ave = []
ave_found = False

# Main for loop
for i in range(1, len(borehole)): 
	if borehole[i - 1] == borehole[i] and from_arr[i] == to_arr[i - 1]:  # checking same hole and there are no gaps between sample current FROM same as previsous TO
		if au[i] >= min_value: # check for minimum Au
			if width_total == 0: # Is this the first over the minimum in this average?
				start_i = i # set start counter
				if au[i - 1] >= min_value: # checked is previous sample is also over the threshold.
					start_i = i - 1
					cmg_total += cmg[i - 1]
					width_total += width[i - 1]
			width_total += width[i]
			cmg_total += cmg[i]
		elif width_total > 0:
			j = i + 1
			#
			temp_cmg_total += cmg[j - 1]
			temp_width_total += width[j - 1]
			while j < len(borehole) and borehole[j - 1] == borehole[j] and from_arr[j] == to_arr[j - 1]:
				temp_cmg_total += cmg[j]
				temp_width_total += width[j]

				if temp_cmg_total/temp_width_total >= min_value:
					print(True, j)
					print(temp_cmg_total/temp_width_total, '\n')
					cmg_total += temp_cmg_total
					width_total += temp_width_total
					ave_found = True
					i = j
					break
				j += 1
			if width_total != 0 and ave_found is False:
				average.append(cmg_total/width_total)
				borehole_ave.append(borehole[start_i])
				from_arr_ave.append(from_arr[start_i])
				to_arr_ave.append(to_arr[i-1])
				width_total_arr.append(width_total)
				cmg_total_arr.append(cmg_total)
				width_total=0
				cmg_total=0
			ave_found = False
			temp_cmg_total = 0
			temp_width_total = 0
			
	elif width_total != 0:
		average.append(cmg_total/width_total)
		borehole_ave.append(borehole[start_i])
		from_arr_ave.append(from_arr[start_i])
		to_arr_ave.append(to_arr[i-1])
		width_total_arr.append(width_total)
		cmg_total_arr.append(cmg_total)
		width_total=0
		cmg_total=0


for i in range(len(borehole_ave)):
	print(borehole_ave[i], from_arr_ave[i], to_arr_ave[i], average[i], width_total_arr[i],cmg_total_arr[i])

print(len(borehole_ave))

