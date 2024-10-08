

def saudacao():
    print ("ola marcos")
    print("temos 5 laptops")

saudacao()


def somar():
    numero1 = 20
    numero2 = 30
    resultado = numero1 + numero2

    print(resultado)

somar()

def bem_vindo(sobrenome, nome):
    print(f"bem vindo {sobrenome}, {nome} - bem vindo")

bem_vindo("Alves", "Renan")


for name in ['Renan', 'Sharon']:
    print(name)

for index in range (0, 5):
    print(index)

print()

# Vários argumentos dentro da função - o * significa que podem haver vários argumentos
def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    
    return resultado

x = soma(4,2,9,34,23,12)
print(x)

print()

# com dois * dentro do parâmetro, da pra colocar vario argumentos dentro do print
def agencia(**carro):
    return carro

print(agencia(marca= 'Gol', cor= 'Branco', motor=1.0, placa=12345))


def main():
    #create a list that contains five strings.
    colors = ['yellow', 'red', 'green', 'yellow', 'blue']
    #call the buit-in len function
    #and print the length of the list
    print(colors[2])
    #change the element that is stored at
    #index 3 from "yellow" to "purple"
    colors[3] = "purple"
    #print the entire colors list
    print(colors)
#call main to start this program
if __name__=="__main__":
    main()


# criar uma lista, adicionar, encontrar e remover itens de uma lista
def main():
    # create an empty list taht will hold fabric names
    fabrics = []
    # add three elements at the end of the fabrics list
    fabrics.append("velvet")
    fabrics.append("denim")
    fabrics.append("gingham")
    # insert an element at the begiming of the fabrics list.
    fabrics.insert(0, "chiffon")
    print(fabrics)
    # determine if gingham is in the fabrics list.
    if "gingham" in fabrics:
        print ("gingham is in the list")
    else:
        print("gingham is NOT in the list")
    # get the index where velvet is stored in the fabrics list.
    i = fabrics.index("velvet")
    # replace velvet with  taffeta.
    fabrics[i] = "taffeta"
    # remove the last element from the fabrics list.
    fabrics.pop()
    # remove denim from the fabrics list.
    fabrics.remove("denim")
    # get the length of the fabrics list and print it.
    n = len(fabrics)
    print(f"The fabrics list contains {n} elements.")
    print(fabrics)

# call main to start this program
if __name__=="__main__":
    main()

print()
# Example 4
def main():
    # Count from zero to nine by one.
    for i in range(10):
        print(i)
    print()
    # Count from five to nine by one.
    for i in range(5, 10):
        print(i)
    print()
    for i in range(0, 10, 2):
        print(i)
    print()
    # Count from 100 down to 70 by three.
    for i in range(100, 69, -3):
        print(i)

# Call main to start this program.
if __name__ == "__main__":
    main()


# Example 5
def main():
    # Create a list of color names.
    colors = ["red", "orange", "yellow", "green", "blue"]
    # Use a for loop to print each element in the list.
    for color in colors:
        print(color)
    print()
    # Use a different for loop to
    # print each element in the list.
    for i in range(len(colors)):
        # Use the index i to retrieve
        # an element from the list.
        color = colors[i]
        print(color)
# Call main to start this program.
if __name__ == "__main__":
    main()


# Example 6
def main():
    sum = 0
    # Get ten or fewer numbers from the user and
    # add them together.
    for i in range(10):
        number = float(input("Please enter a number: "))
        if number == 0:
            break
        sum += number
    # Print the sum of the numbers for the user to see.
    print(f"sum: {sum}")
# Call main to start this program.
if __name__ == "__main__":
    main()

print()
# Example 7
def main():
    list1 = ["red", "orange", "yellow", "green", "blue"]
    list2 = ["red", "orange", "green", "green", "blue"]
    index = compare_lists(list1, list2)
    if index == -1:
        print("The contents of list1 and list2 are equal")
    else:
        print(f"list1 and list2 differ at index {index}")
def compare_lists(list1, list2):
    """Compare o conteúdo de duas listas. Se o conteúdo
    das duas listas não são iguais, retorne o índice de
    a primeira diferença. Se o conteúdo das duas listas
    são iguais, retorne -1.
    Parâmetros
        lista1: uma lista
        lista2: outra lista
        Retorno: um índice ou -1"""
    # Get the length of the shortest list.
    length1 = len(list1)
    length2 = len(list2)
    limit = min(length1, length2)
    """Comece no primeiro índice (0) e repita até o
    # computador encontra dois elementos que não são iguais ou
    # até que o computador chegue ao final do menor
    # lista, o que ocorrer primeiro."""
    i = 0
    while i < limit:
        # Retrieve one element from each list.
        element1 = list1[i]
        element2 = list2[i]
        # If the two elements are not
        # equal, quit the while loop.
        if element1 != element2:
            break
        # Add one to the index variable.
        i += 1
    # If the length of both lists are equal and the
    # computer verified that all elements are equal,
    # set i to -1 to indicate that the contents of
    # the two lists are equal.
    if length1 == length2 == i:
        i = -1
    return i
# Call main to start this program.
if __name__ == "__main__":
    main()

print()
# Example 8
def main():
    # These are the indexes of each
    # element in the inner lists.
    YEAR_PLANTED_INDEX = 0
    HEIGHT_INDEX = 1
    GIRTH_INDEX = 2
    FRUIT_AMOUNT_INDEX = 3
    # Create a compound list that stores inner lists.
    apple_tree_data = [
        # [year_planted, height, girth, fruit_amount]
        [2012, 2.7, 3.6, 70.5],
        [2012, 2.4, 3.7, 81.3],
        [2015, 2.3, 3.6, 62.7],
        [2016, 2.1, 2.7, 42.1]
    ]
    # Retrieve one inner list from the compound list.
    one_tree = apple_tree_data[2]
    # Retrieve one value from the inner list.
    height = one_tree[HEIGHT_INDEX]
    # Print the tree's height.
    print(f"height: {height}")
# Call main to start this program.
if __name__ == "__main__":
    main()

print()
# Example 9
def main():
    # These are the indexes of each
    # element in the inner lists.
    YEAR_PLANTED_INDEX = 0
    HEIGHT_INDEX = 1
    GIRTH_INDEX = 2
    FRUIT_AMOUNT_INDEX = 3
    # Create a compound list that stores inner lists.
    apple_tree_data = [
        # [year_planted, height, girth, fruit_amount]
        [2012, 2.7, 3.6, 70.5],
        [2012, 2.4, 3.7, 81.3],
        [2015, 2.3, 3.6, 62.7],
        [2016, 2.1, 2.7, 42.1]
    ]
    total_fruit_amount = 0
    # This loop will repeat once for each inner list
    # in the apple_tree_data compound list.
    for inner_list in apple_tree_data:
        # Retrieve the fruit amount from
        # the current inner list.
        fruit_amount = inner_list[FRUIT_AMOUNT_INDEX]
        # Print the fruit amount for the current tree.
        print(fruit_amount)
        # Add the current fruit amount to the total.
        total_fruit_amount += fruit_amount
    # Print the total fruit amount.
    print(f"Total fruit amount: {total_fruit_amount:.1f}")
# Call main to start this program.
if __name__ == "__main__":
    main()

print()
# Example 10
def main():
    x = 17
    y = x
    print(f"Before changing x: x {x}  y {y}")
    x += 1
    print(f"After changing x:  x {x}  y {y}")
# Call main to start this program.
if __name__ == "__main__":
    main()


print()
# Example 11
def main():
    lx = [7, -2]
    ly = lx
    print(f"Before changing lx: lx {lx}  ly {ly}")
    lx.append(5)
    print(f"After changing lx:  lx {lx}  ly {ly}")
# Call main to start this program.
if __name__ == "__main__":
    main()

# Example 12
def main():
    print("main()")
    x = 5
    lx = [7, -2]
    print(f"Before calling modify_args(): x {x}  lx {lx}")
    # Pass one integer and one list
    # to the modify_args function.
    modify_args(x, lx)
    print(f"After calling modify_args():  x {x}  lx {lx}")
def modify_args(n, alist):
    """Demonstrate that the computer passes a value
    for integers and passes a reference for lists.
    Parameters
        n: A number
        alist: A list
    Return: nothing
    """
    print("   modify_args(n, alist)")
    print(f"   Before changing n and alist: n {n}  alist {alist}")
    # Change the values of both parameters.
    n += 1
    alist.append(4)
    print(f"   After changing n and alist:  n {n}  alist {alist}")
# Call main to start this program.
if __name__ == "__main__":
    main()

print()

