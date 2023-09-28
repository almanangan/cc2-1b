ONE_POUND_TO_KILOGRAMS = 0.45359237

pounds = float(input("Weight in Pounds (lbs): ")) 

userPoundsToKilograms = pounds * ONE_POUND_TO_KILOGRAMS

print("Weight converted to Kilogograms (kg): ", userPoundsToKilograms)

print("===========================================================")

ONE_MILES_TO_KILOMETERS = 1.609344

miles = float(input("Leght in Miles(mi):"))

userMilesToKilometers = miles * ONE_MILES_TO_KILOMETERS

print("Length in Kilometers (km):", userMilesToKilometers )

print("===========================================================")

fahrenheit = float(input("Temperature in Fahrenheit(°F):"))
ONE_FAHRENHEIT_TO_CELSIUS = (fahrenheit - 32) * 5 / 9 

userFahrenheitToCelsius = fahrenheit * ONE_FAHRENHEIT_TO_CELSIUS

print("Temperature in Celsius(°C): ", userFahrenheitToCelsius)

print("===========================================================")

userInput1 = float(input("Age of student 1: ")) 
userInput2 = float(input("Age of student 2: "))
userInput3 = float(input("Age of student 3: "))
userInput4 = float(input("Age of student 4: "))
userInput5 = float(input("Age of student 5: "))
userInput6 = float(input("Age of student 6 :"))
userInput7 = float(input("Age of student 7 :"))
userInput8 = float(input("Age of student 8 :"))
userInput9 = float(input("Age of student 9 :"))
userInput10 = float(input("Age of student 10: "))
userAverageOfTheStudent = ((userInput1 + userInput2 + userInput3 + userInput4 + userInput5 + userInput6 + userInput7 + userInput8 + userInput9 + userInput10)/10)
print("The average of the student is: ", userAverageOfTheStudent )

print("===========================================================")

Character1 = "Jiwoo"
Character2 = "Subin"
Character3 = "Wooin"
Character4 = "Jisuk"
Character5 = "Kayden"

Ability1 = "Super speed and Electrokinesis"
Ability2 = "Cryokinesis"
Ability3 = "Telekinesis"
Ability4 = "Aerokinesis"
Ability5 = "Electrokinesis"

story =  (f"""The world is a dark and dangerous place, ruled by powerful mages and warlords. In the midst of this chaos, a group of unlikely heroes rise up to fight for justice.
Their names are {Character1}, {Character2}, {Character3}, {Character4} and {Character5}. {Character1} ability is {Ability1}, {Character2} ability is {Ability2} it can manipulate ice,
{Character3} ability is {Ability3}, {Character4} ability is {Ability4} it can manipulate wind and lastly {Character5} ability is {Ability5} it can manipulate electricity. 
Together, they must journey across the land, facing many dangers along the way. They must battle fearsome monsters, overcome treacherous obstacles, and outsmart cunning villains.
But if they succeed, they will save the world from darkness and bring peace to the land.""")

print(story)
