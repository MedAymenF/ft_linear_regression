import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


def		train(mileage, price, learning_rate, n_epochs):
	m = float(len(mileage))
	theta0, theta1 = 0, 0
	for _ in range(n_epochs):
		price_estimate = mileage * theta1 + theta0
		diff = price_estimate - price
		# print("diff:", diff)
		tmp_theta0 = np.sum(diff)*learning_rate/m
		product = diff*mileage
		# print("product:", product)
		tmp_theta1 = np.sum(product)*learning_rate/m
		theta0 -= tmp_theta0
		theta1 -= tmp_theta1
		# print(theta0, theta1)
	return theta0, theta1


def		main():
	with open("data.csv") as data_file:
		csv_reader = csv.reader(data_file, delimiter=',')
		mileage, price = [], []
		count = 0
		for row in csv_reader:
			if (count):
				mileage.append(int(row[0]))
				price.append(int(row[1]))
			count += 1
	mileage = np.array(mileage)
	price = np.array(price)
	# print(f"Mileage: {mileage}")
	# print(f"Price: {price}")
	# print(count - 1)
	# plt.scatter(mileage, price)
	# plt.show()

	# Data normalization
	mileage_scaler = MinMaxScaler()
	mileage = mileage.reshape(-1, 1)
	mileage_norm = mileage_scaler.fit_transform(mileage)
	# print(mileage_norm)

	price_scaler = MinMaxScaler()
	price = price.reshape(-1, 1)
	price_norm = price_scaler.fit_transform(price)
	# print(price_norm)

	learning_rate = 0.01
	n_epochs = 100000
	theta0_norm, theta1_norm = train(mileage_norm, price_norm, learning_rate, n_epochs)
	# print(theta0_norm, theta1_norm)

	predicted_price_norm = theta1_norm * mileage_norm + theta0_norm
	predicted_price = price_scaler.inverse_transform(predicted_price_norm)
	# print(predicted_price)
	plt.scatter(mileage, price)
	plt.plot(mileage, predicted_price, color='red')
	plt.xlabel("Mileage (in Km)")
	plt.ylabel("Price (in Euros)")
	plt.show()

	# Calculating real values of theta0 and theta1
	theta0 = (theta0_norm - (theta1_norm * mileage.min()) / (mileage.max() - mileage.min())) * (price.max() - price.min()) + price.min()
	theta1 = (theta1_norm / (mileage.max() - mileage.min())) * (price.max() - price.min())

	# print(theta0, theta1)
	f = open("parameters.txt", 'w')
	f.write(f"{theta0}\n{theta1}\n")


if __name__ == "__main__":
    main()
