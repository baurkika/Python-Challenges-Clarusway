gasGallon = float(input("Enter a number which stands for gallons of gasoline: "))
gasLiter = gasGallon * 3.7854
barrel = gasGallon / 19.5
cost = gasLiter * 0.75

print("{} gallon(s) = {} liter(s).".format(gasGallon, gasLiter))
print("{} barrel(s) of oil required to produce {} gallon(s) of gas".format(barrel,gasGallon))
print("It will cost {} dollar(s)".format(cost))