import math

# ask for parameters
width = int(input("Enter the widthof the tire in mm (ex. 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex. 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex. 15): "))

# formula to calculate
# V = π * w^2 * a * (w * a + 2540 * d) / 10,000,000,000
# w = width (in mm), a = aspect, d = diameter (in inches)
volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# round the volume to two decimais
volume = round(volume, 2)

# print the result
print(f"O volume aproximado é de {volume} litros")
