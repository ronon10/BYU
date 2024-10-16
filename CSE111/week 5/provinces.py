


def main():

    province_list = read_list("C:/Users/realves/Documents/BYU/CSE111/week 5/provinces.txt")
    print(province_list)

    #remove o primeiro da lista
    province_list.pop(0)

    #remove o ultimo elemento da lista
    province_list.pop()

    # substitui tudo que for AB por Alberta
    for i in range(len(province_list)):
        if province_list[i] == "AB":
            province_list[i] = "Alberta"
    
    count = province_list.count("Alberta")
    print()
    print(f"Alberta aparece {count} vezes na lista")

def read_list(filename):
    text_list = []
    #cria uma lista vazia que ira armazenar os itens do arquivo
    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)


    return text_list


if __name__=="__main__":
    main()