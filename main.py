import sys
import itertools
import multiprocessing as mp
import math



PRINTBOOKS = True

def main(infile):

	print(f"start {infile}")

	# class Book:
	# 	def __init__(self, index, score):
	# 		self.index = index
	# 		self.score = score
	# 		self.rarity = 1



	# 	def __repr__(self):
	# 		return self.__str__()
	# 	def __str__(self):
	# 		stuff = dict(vars(self))
	# 		for k in stuff:
	# 			if isinstance(stuff[k], float):
	# 				stuff[k] = round(stuff[k], 2)
	# 		return str(stuff)



	# class Lib:
	# 	def __init__(self, index, signupDays, troughput, books):
	# 		self.originalIndex = index
	# 		self.index = index
	# 		self.signupDays = signupDays
	# 		self.troughput = troughput

	# 		self.books = books
	# 		self.booksMemory = tuple(books)
	# 		# self.booksByIndex = dict()
	# 		# for bookI, book in enumerate(books):
	# 		# 	self.booksByIndex[book.index] = bookI
			

			
	# 	def __repr__(self):
	# 		return self.__str__()
	# 	def __str__(self):
	# 		stuff = dict(vars(self))
	# 		if not PRINTBOOKS:
	# 			stuff["books"] = f"len({len(stuff['books'])}"
	# 		for k in stuff:
	# 			if isinstance(stuff[k], float):
	# 				stuff[k] = round(stuff[k], 2)
	# 		return str(stuff)

	class Street:
		def __init__(self, index, start, end, name, length):
			self.index = index
			self.start = start
			self.end = end
			self.name = name
			self.length = length

		def __repr__(self):
			return self.__str__()
		def __str__(self):
			return str(self.index) + " " + self.name

	class Car:
		def __init__(self, index, path):
			self.index = index
			self.path = path

		def __repr__(self):
			return self.__str__()
		def __str__(self):
			return str(self.index)
			




	with open("in/" + infile, 'r') as inf:

		infoLine = inf.readline().rstrip("\n")
		info = infoLine.split(" ")

		simTime = int(info[0])
		numInters = int(info[1])
		numStreets = int(info[2])
		numCars = int(info[3])
		scorePerCarOnTime = int(info[4])


		streets = []
		streetDict = {}
		for streetI in range(numStreets):
			streetInfo = inf.readline().rstrip("\n").split(" ")
			street = Street(streetI, int(streetInfo[0]), int(streetInfo[1]), streetInfo[2], int(streetInfo[3]))
			streets.append(street)
			streetDict[street.name] = street

		cars = []
		for carI in range(numCars):
			carInfo = inf.readline().rstrip("\n").split(" ")
			path = []
			for i in range(1, len(carInfo)):
				path.append(streetDict[carInfo[i]])
			print(path)
			car = Car(carI, path)
			cars.append(car)

		
	print(streets, cars)




if __name__ == "__main__":
	main("a.txt")