#!/usr/bin/env python3

import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from math import sqrt
import argparse


def		train(mileage, price, learning_rate, n_epochs):
	m = float(len(mileage))
	theta0, theta1 = 0, 0
	for _ in range(n_epochs):
		price_estimate = mileage * theta1 + theta0
		diff = price_estimate - price
		tmp_theta0 = np.sum(diff)*learning_rate/m
		tmp_theta1 = np.sum(diff*mileage)*learning_rate/m
		theta0 -= tmp_theta0
		theta1 -= tmp_theta1
	return theta0, theta1


def		main():
	# Parse arguments
	my_parser = argparse.ArgumentParser(description='Train a linear regression model on a univariate dataset.')
	my_parser.add_argument('Path', metavar='path', type=str, help='The path to the csv file containing the data.')
	my_parser.add_argument('-n', '-Number of epochs', type=int, default=1000)
	my_parser.add_argument('-l', '-Learning rate', type=float, default=0.1)
	args = my_parser.parse_args()
	if (args.n < 1):
		print("The number of epochs must be larger than zero.")
		exit(1)
	if (args.l <= 0):
		print("The learning rate must be larger than zero.")
		exit(1)

	# Read csv file
	try:
		with open(args.Path) as data_file:
			csv_reader = csv.reader(data_file, delimiter=',')
			mileage, price = [], []
			count = 0
			for row in csv_reader:
				if (count):
					mileage.append(int(row[0]))
					price.append(int(row[1]))
				count += 1
	except Exception as e:
		print(f"Can't open {args.Path} or it's not a valid csv file.")
		print(e)
		exit(1)
	mileage = np.array(mileage)
	price = np.array(price)

	# Data normalization
	mileage_scaler = MinMaxScaler()
	mileage = mileage.reshape(-1, 1)
	mileage_norm = mileage_scaler.fit_transform(mileage)

	price_scaler = MinMaxScaler()
	price = price.reshape(-1, 1)
	price_norm = price_scaler.fit_transform(price)

	# Training
	theta0_norm, theta1_norm = train(mileage_norm, price_norm, args.l, args.n)
	predicted_price_norm = theta1_norm * mileage_norm + theta0_norm

	# Rescaling
	predicted_price = price_scaler.inverse_transform(predicted_price_norm)

	# Calculating root mean squared error
	rmse = sqrt(np.sum((predicted_price - price) * (predicted_price - price))/(count - 1))
	print(f"RMSE: {rmse}")

	# Plotting
	plt.scatter(mileage, price)
	plt.plot(mileage, predicted_price, color='red')
	plt.xlabel("Mileage (in Km)")
	plt.ylabel("Price (in Euros)")
	plt.show()

	# Calculating real values of theta0 and theta1
	theta0 = (theta0_norm - (theta1_norm * mileage.min()) / (mileage.max() - mileage.min())) * (price.max() - price.min()) + price.min()
	theta1 = (theta1_norm / (mileage.max() - mileage.min())) * (price.max() - price.min())

	# Saving theta0 and theta1 to a file
	f = open("parameters.txt", 'w')
	f.write(f"{theta0}\n{theta1}\n")


if __name__ == "__main__":
    main()
