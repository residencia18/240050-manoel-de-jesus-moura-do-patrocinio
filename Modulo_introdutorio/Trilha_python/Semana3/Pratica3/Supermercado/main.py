import os
import json


productList = []

# Reading the .txt file
def readFile():
    lines = []
    global productList
    
    try:
        with open('Semana3/Pratica3/Supermercado/produtos.txt', 'r') as file:
            lines = file.readlines()
            
        productList = [json.loads(line) for line in lines]
    except:
        print("\n\n Não foi possível resgatar os dados !! \nEntre em contato com o suporte do programa.")    
   
# saving on the .txt file
     
def saveOnFile(array):
    try:
        with open('Semana3/Pratica3/Supermercado/produtos.txt', 'w') as file:
            for list_item in array:
                list_in_string = json.dumps(list_item)
                file.write("%s\n" % list_in_string)
    except:
        print("\n\n Não foi possível salvar os dados no arquivo !! \nEntre em contato com o suporte do programa.")    

def addProduct(newProduct):
    productList.append(newProduct)
    print("\nProduto registrada!!!\n")
    saveOnFile(productList)

def listProdutos():
    print("\n\n---Lista de Produtos ---\n")
    sorted_productList = sorted(productList, key=lambda item: item['price'])

    for prod in sorted_productList:
        print("Código: ",prod["code"])
        print("Nome do Produto: ",prod["name"])
        print(f'Preço: R$ {prod["price"]:.2f} \n\n')
        
def deleteProduct(p_cod):
    for prod in productList:
        if prod["code"] == p_cod:
            productList.pop(productList.index(prod))
            saveOnFile(productList)
            print("\nProduto excluido !!! \n\n")
            
        
def checkProductByPrice(p_cod):
    for prod in productList:
        if prod["code"] == p_cod:
            print(f'\nProduto: {prod["name"] }, Preço: R$ {prod["price"]:.2f} \n\n')
    

def main():
    option = ""
    while True:
        print("1 - p/ Inserir um produto")
        print("2 - p/ Excluir um produto")
        print("3 - p/ Listar os produtos")
        print("4 - p/ Consultar preço do produto")
        print("0 - p/ Sair")
        option = int(input("Sua escolha: "))
        
        if option == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            p_cod = input("Informe o código do Produto : ")
            p_name = input("Informe o nome do Produto : ").capitalize()
            try:
                
                p_price = float(input("Informe o peço do Produto : "))
            except:
                print("Erro, digite apenas números para o preço, ex: (20.30).")
            
            newProduct = {
                "code":p_cod,
                "name":p_name,
                "price":p_price
            }
            addProduct(newProduct)
        elif option == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            p_cod = input("Informe o código do Produto que deseja deletar : ")

            deleteProduct(p_cod)
        elif option == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            listProdutos()
        elif option == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            p_cod = input("Informe o código do Produto que deseja consultar o preço : ")

            checkProductByPrice(p_cod)
        elif option == 0:
            break
        else:
            print("\n\nOpcao invalida. Tente novamente.\n\n")
   
    
    
if __name__ == "__main__":
    readFile()
    main()
