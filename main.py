"""
Program to find triangles with right angles and
same sides with a whole number as the hypotenuse....
if its possible
"""
## Dependencies
import math

## Initialization Variables

numbertotryto = 10000000000000
startRange = 1
## Functions





## Engine

def runprogram():
	print("Running\n")

	# validate numbertotryto is greater than start Range
	if numbertotryto > startRange:

		#start loop
		for i in range(startRange, numbertotryto):
			hypotenuse = math.sqrt(i**2 + i**2)

			print("sides are {} hypotenuse is {}".format(i, hypotenuse))

			# Breaks if hypotenuse is a whole number
			if hypotenuse % 1 == 0:
				break
	# hits if numbertotry is not greather than 0
	else:
		print("incorrect number to try to")



	return


## User Output/integration


runprogram()
print("\nprogram Over")