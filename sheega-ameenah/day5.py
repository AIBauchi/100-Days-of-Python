# Write a Python script that converts Celsius to Fahrenheit with user input
temperatureInCelcius = int(input("Please enter the temperature you wish to convert: \n"))
temperatureInFahrenheit = (temperatureInCelcius * 1.8) + 32
degreeSign = u"\N{DEGREE SIGN}"
print(f"{temperatureInCelcius }{degreeSign}C is equal to {temperatureInFahrenheit}{degreeSign}F")
