import csv

with open('Compositing Data.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	next(reader)
	for row in reader:
		print(row[3])