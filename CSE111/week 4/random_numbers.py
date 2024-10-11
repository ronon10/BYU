# team activit
# Como uma equipe, escreva um programa Python chamado random_numbers.py 
# que cria uma lista de números,
# acrescenta mais números à lista e imprime a lista.
# O programa deve ter duas funções chamadas maine append_random_numberscomo segue:
import random

def main():
    numbers = [16.2, 75.1, 52.3] # Cria uma lista chamada numbers
    print(f"Numbers are: {numbers}") # imprime a lista numbers
    
    # Chama a append_random_numbers função com apenas um argumento para adicionar um número aos numbers
    append_random_numbers(numbers)
    print(f"numbers {numbers}") # imprime a lista numbers

    # Chama a append_random_numbers função novamente com dois argumentos para adicionar três números aos numbers
    append_random_numbers(numbers, 3)
    print(f"numbers {numbers}") # # imprime a lista numbers

def append_random_numbers(numbers_list, quantity=1): # Tem dois parâmetros: uma lista chamada numbers_list e um inteiro chamado quantity.
    #O parâmetro quantity tem um valor padrão de 1
    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        rounded = round(random_number, 1)
        numbers_list.append(rounded)

if __name__ == "__main__":
    main()
