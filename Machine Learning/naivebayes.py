# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 01:05:10 2022
naive bayes classifier
@author: starg
"""
import pandas as pd
import matplotlib.pyplot as plt
import dateutil
from scipy.optimize import curve_fit
import numpy as np


def Gauss(x, A, B):
    y = A*np.exp(-1*B*x**2)
    return y

df = pd.read_csv('./data/intraday_5min_IBM.csv')

open_prices = df['open']
close_prices = df['close']
prices = list(zip(open_prices,close_prices))
times = list(df['timestamp'])
times = list(map(lambda x: dateutil.parser.parse(x).timestamp(),times))

parameters, covariance = curve_fit(Gauss, times, open_prices)

fit_A = parameters[0]
fit_B = parameters[1]

fit_y = Gauss(times, fit_A, fit_B)
plt.plot(times, open_prices, 'o', label='data')
plt.plot(times, fit_y, '-', label='fit')
plt.legend()



diff = list(map(lambda x: x[0]-x[1],prices))

plt.plot(times, open_prices, 'g-')
plt.plot(times, close_prices, 'r-')
#plt.plot(times, diff, 'm-')
plt.xlabel('time')
plt.ylabel('open price')
plt.show()


    


def separate_by_class(dataset):
	separated = dict()
	for i in range(len(dataset)):
		vector = dataset[i]
		class_value = vector[-1]
		if (class_value not in separated):
			separated[class_value] = list()
		separated[class_value].append(vector)
	return separated

# Example of summarizing data by class value
from math import sqrt

# Split the dataset by class values, returns a dictionary


# Calculate the mean of a list of numbers
def mean(numbers):
	return sum(numbers)/float(len(numbers))

# Calculate the standard deviation of a list of numbers
def stdev(numbers):
	avg = mean(numbers)
	variance = sum([(x-avg)**2 for x in numbers]) / float(len(numbers)-1)
	return sqrt(variance)

# Calculate the mean, stdev and count for each column in a dataset
def summarize_dataset(dataset):
	summaries = [(mean(column), stdev(column), len(column)) for column in zip(*dataset)]
	del(summaries[-1])
	return summaries

# Split dataset by class then calculate statistics for each row
def summarize_by_class(dataset):
	separated = separate_by_class(dataset)
	summaries = dict()
	for class_value, rows in separated.items():
		summaries[class_value] = summarize_dataset(rows)
	return summaries

# Test summarizing by class
dataset = [[3.393533211,2.331273381,0],
	[3.110073483,1.781539638,0],
	[1.343808831,3.368360954,0],
	[3.582294042,4.67917911,0],
	[2.280362439,2.866990263,0],
	[7.423436942,4.696522875,1],
	[5.745051997,3.533989803,1],
	[9.172168622,2.511101045,1],
	[7.792783481,3.424088941,1],
	[7.939820817,0.791637231,1]]
summary = summarize_by_class(dataset)
for label in summary:
	print(label)
	for row in summary[label]:
		print(row)