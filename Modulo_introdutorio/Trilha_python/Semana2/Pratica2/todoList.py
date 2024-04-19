import os

# The list to store tasks
tasks = []

# Reading the .txt file
def readFile(string_array):
    with open('./Semana2/Pratica2/output.txt', 'r') as file:
        for line in file:
            # Removing newline character
            line = line.strip()
            
            # Adding line to the array
            string_array.append(line)
            
def saveOnFile(string_array):
# Writing the array back to a new .txt file
    with open('./Semana2/Pratica2/output.txt', 'w') as file:
        for line in string_array:
            # Writing line to the file
            file.write(line + '\n')

def add_task(newTask):
    taskFormated = newTask.capitalize()
    tasks.append(taskFormated)
    print("\nTarefa registrada!!!\n")
    saveOnFile(tasks)
    

def display_tasks():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, task in enumerate(tasks):
        if task.find("[x]") > -1 :
            print(f"{i+1}. {task}")
        else:
            print(f"{i+1}. {task} [ ]")

def mark_completed(index):
    os.system('cls' if os.name == 'nt' else 'clear')

    if 0 < index <= len(tasks):
        tasks.insert(0,f"{tasks[index-1]} [x]")
        tasks.pop(index)
        
        print("Tarefa concluida !!! ")
        saveOnFile(tasks)
    else:
        print("Numero inválido. Tente Novamente.")

def edit_task(index):
    os.system('cls' if os.name == 'nt' else 'clear')
    if 0 < index <= len(tasks):
        editedTask = input("Informe a nova descrição: ")
        if tasks[index-1].find("[x]") > -1 :
            tasks[index-1] = editedTask + " [x]"
            saveOnFile(tasks)
            
        else:
            tasks[index-1] = editedTask 
            saveOnFile(tasks)
            
    else:
        print("Numero inválido. Tente Novamente.")
    
def delete_task(index):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if 0 < index <= len(tasks):
        tasks.pop(index-1)
        print("Tarefa excluida !!! ")
        saveOnFile(tasks)
    else:
        print("Numero inválido. Tente Novamente.")

def main():
    
    while True:
        print("\nTodo List")
        print("---------")
        print("1. Adicionar tarefa")
        print("2. Exibir lista")
        print("3. Marcar tarefa como completa ")
        print("4. Editar tarefa")
        print("5. Deletar tarefa")
        print("6. Sair")

        option = int(input("Sua escolha: "))

        if option == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            task = input("Informe a tarefa: ")
            add_task(task)
        elif option == 2:
            display_tasks()
        elif option == 3:
            index = int(input("Informe o numero da tarefa que deseja completar: "))
            mark_completed(index)
        elif option == 4:
            index = int(input("Informe o numero da tarefa que deseja editar: "))
            edit_task(index)
        elif option == 5:
            index = int(input("Informe o numero da tarefa que deseja deletar: "))
            delete_task(index)
        elif option == 6:
            break
        else:
            print("Opcao invalida. Tente novamente.")

if __name__ == "__main__":
    readFile(tasks)
    main()
   
