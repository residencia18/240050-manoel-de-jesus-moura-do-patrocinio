import os
import json
from datetime import datetime


employeeList = []

# Reading the .txt file
def readFile():
    lines = []
    global employeeList
    
    try:
        
        with open('Semana3/Pratica3/exercicio2/funcionarios.txt', 'r') as file:
            lines = file.readlines()
            
        employeeList = [json.loads(line) for line in lines]
    except:
        print("\n\n Não foi possível resgatar os dados !! \nEntre em contato com o suporte do programa.")    
     
def saveOnFile(array):
# Writing the array back to a new .txt file
    try :
        with open('Semana3/Pratica3/exercicio2/funcionarios.txt', 'w') as file:
            for dict_item in array:
                dict_string = json.dumps(dict_item)
                file.write("%s\n" % dict_string)
    except:
        print("\n\n Não foi possível salvar os dados no arquivo !! \nEntre em contato com o suporte do programa.")    
        

def addEmployee(newEmployee):
    employeeList.append(newEmployee)
    print("\n Funcionário registrada!!!\n")
    saveOnFile(employeeList)

def listEmployee():
    print("\n\n---Lista de Funcionários ---\n")
    sorted_EmployeeList = sorted(employeeList, key=lambda item: item['salary'])

    for func in sorted_EmployeeList:
        print("Nome: ",func["name"])
        print("RG:: ",func["rg"])
        print("Data de Nascimento: ",func["birthDate"])
        print("Data de Admissão: ",func["birthDate"])
        print(f'Salario: R$ {func["salary"]:.2f} \n\n')
        
def deleteEmployee(f_rg):
    for func in employeeList:
        if func["rg"] == f_rg:
            employeeList.pop(employeeList.index(func))
            saveOnFile(employeeList)
            print("\nFuncionário excluído !!! \n\n")
            
        
def findEmployeeByRg(f_rg):
    for func in employeeList:
        if func["rg"] == f_rg:
            print("Nome: ",func["name"])
            print("RG:: ",func["rg"])
            print("Data de Nascimento: ",func["birthDate"])
            print("Data de Admissão: ",func["birthDate"])
            print(f'Salario: R$ {func["salary"]:.2f} \n\n')
    
def Reajusta_dez_porcento(arrayList):
    for func in arrayList:
        func["salary"] += (func["salary"] * 10) // 100
        print(f'Salario: R$ {func["salary"]:.2f} \n\n')
        
def main():
    option = ""
    while True:
        print("1 - p/ Cadastrar um funcionário")
        print("2 - p/ Excluir um funcionário")
        print("3 - p/ Listar os funcionários")
        print("4 - p/ Consultar por RG")
        print("5 - p/ Reajustar 10% do salário")
        print("0 - p/ Sair")
        option = int(input("Sua escolha: "))
        
        if option == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            f_name = input("Informe nome do funcionário : ").capitalize()
            f_lastName = input("Sobrenome: ").capitalize()
            f_dateBirth = input("Data de nascimento (Dia/Mes/Ano): ")
            f_rg = input("RG: ")
            f_yearAdmission = input("Ano de admissão: ")
            try:
                f_salary = float(input("Salario: "))
            except:
                print("Erro, digite apenas números para o salario, ex: (1320.30).")
            
            newEmployee = {
                "name": f"{f_name} {f_lastName}",
                "birthDate": f_dateBirth,
                "rg": f_rg,
                "admissionYear": f_yearAdmission,
                "salary": f_salary,
            }
            addEmployee(newEmployee)
        elif option == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            f_rg = input("Informe o RG do funcionário que deseja deletar : ")

            deleteEmployee(f_rg)
        elif option == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            listEmployee()
        elif option == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            f_rg = input("Informe o RG do funcionário que deseja consultar salário : ")

            findEmployeeByRg(f_rg)
        elif option == 5:
            Reajusta_dez_porcento(employeeList)
        elif option == 0:
            break
        else:
            print("\n\nOpção invalida. Tente novamente.\n\n")
   
    
    
if __name__ == "__main__":
    readFile()
    main()


