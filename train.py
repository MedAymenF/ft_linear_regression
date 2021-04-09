import csv
import numpy as np
import matplotlib.pyplot as plt


def		train(mileage, price, learning_rate, n_epochs):
	m = float(len(mileage))
	print("m:", m)
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
		print(theta0, theta1)
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
	print(f"Mileage: {mileage}")
	print(f"Price: {price}")
	print(count - 1)
	# plt.scatter(mileage, price)
	# plt.show()
	learning_rate = 0.00000000001
	n_epochs = 1000
	theta0, theta1 = train(mileage, price, learning_rate, n_epochs)
	print(theta0, theta1)


if __name__ == "__main__":
    main()
