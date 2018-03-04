#!/usr/bin/env python
import pymysql
import pymysql.cursors
from IPython import embed
from matplotlib import pyplot as plt
import numpy as np

def graph(x_values, y_values, a, x_label, y_label) :
	#needs debug
	plt.plot(x_values, y_values, 'ro')
	maxx=x_values[0]
	for x in x_values: 
		if x > maxx:
			maxx=x
	
	maxy=y_values[0]
	for x in y_values: 
		if x > maxy:
			maxy=x
	
	plt.axis([0, 1.2*maxx, 0, 1.2*maxy])
	save_location = 'static/output/output%d.png' % a
	plt.suptitle(y_label+" vs "+x_label+" graph")
	plt.xlabel(x_label)
	plt.ylabel(y_label)
  	plt.savefig(save_location)
  	plt.show() #this clears the canvas
  	print('Saved image to %s' % save_location)


# Connect to the database
conn = pymysql.connect(host='localhost', user='root', password='12345', db='tracking', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

# convert unicode into a [unicode, int] dictionary
cur.execute("SELECT * FROM test3;")
results = cur.fetchall()
results= [dict([a, int(x)] for a, x in b.items()) for b in results]

# extract number of rows and columns
row_number= len(results)
column_number= len(results[0].items())

# extract names of columns
columns = []
columns.append([a.encode('ascii','ignore') for a, x in results[0].items()])

# extract the entire table, the different sessions (each row)
entire_int_table=[]
for x in range(row_number):
	entire_int_table.append([int(x) for a, x in results[x].items()])

#graph all with "timestamp"
index = -1
for x in range(column_number):
	if columns[0][x]=="timestamp":
		index=x;

for x in range (column_number):
	x_axis = []
	y_axis = []
	if x==index: 
		continue
	for a in range (row_number):
		x_axis.append(entire_int_table[a][index])
	for a in range (row_number):
		y_axis.append( entire_int_table[a][x])
	graph (x_axis, y_axis, x, columns[0][index], columns[0][x])

cur.close()
conn.close()


