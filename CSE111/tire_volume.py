import math
from datetime import datetime

# ask for user the parameters of tire
largura = int(input("Enter tire width in mm (ex. 205): "))
proporcao = int(input("Enter tire aspect ratio (ex. 60): "))
diametro = int(input("Enter the wheel diameter in inches (ex. 15): "))

# Calculate tire volume without using a separate function
largura_metros = largura / 1000  
# Convert mm to meters
diametro_total = (proporcao / 100) * largura_metros * 2 + (diametro * 0.0254)  
# Total diameter in meters
volume = (math.pi * (largura_metros ** 2) * proporcao * diametro_total) / 10000000000  
# round to 2 decimals 
volume = round(volume, 2)

# show the volume
print(f"The approximate volume is {volume} liters")

# get only date
data_atual = datetime.now().strftime("%d/%m/%Y")

# opem ou create the volumes.txt's file to add datas
with open("volumes.txt", "at") as arquivo:
    # write in file
    arquivo.write(f"{data_atual}, {largura}, {proporcao}, {diametro}, {volume}\n")

# Aks for user if wants buy the tire
comprar = input("Would you like to buy tires with these dimensions? (yes/no): ").strip().lower()

##### Exceeding the Requirements #######

# if wants to buy, ask forphone and name.
if comprar == "yes":
    telefone = input("Please, enter your phone number: ").strip()
    name = input("What is your name? ")
    # Gravar o número de telefone no arquivo volumes.txt
    with open("volumes.txt", "at") as arquivo:
        arquivo.write(f"Telefone: {telefone} - Name: {name.capitalize()}\n ")

print("Data was saved on volumes.txt")

