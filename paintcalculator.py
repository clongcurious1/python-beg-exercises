import math
#get room dimensions from user, assumes all 4 walls same size
height = input('In feet, height from floor to ceiling:\n') #10
height = int(height) #need int for math equation
length = input('In feet, length of the wall from corner to corner:\n') #25
length = int(length) #need int for math equation
wallarea = (height * length) * 4
gallonsnec = float(wallarea/350) #allow for decimal, not whole number
gallonsnec = math.ceil(gallonsnec) #round up to nearest whole number
print('1 gallon of paint covers 350 square feet.')
print('We estimate the wall area of your room to be ' + str(wallarea) + ' square feet.')
print('We recommend that you purchase ' + str(gallonsnec) + ' gallons to paint out your room.')

