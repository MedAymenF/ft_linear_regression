import csv
import matplotlib.pyplot as plt


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
	print(f"Mileage: {mileage}")
	print(f"Price: {price}")
	print(len(price), len(mileage))
	plt.scatter(mileage, price)
	plt.show()

if __name__ == "__main__":
    main()
