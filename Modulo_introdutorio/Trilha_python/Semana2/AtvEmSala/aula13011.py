#Aula 13/11/2023

#LISTA
P = [ 2, 4, 6, 8, 10]

print("lista original: ", P)

P.append(11)
print("lista com append(11): ", P)

P.insert(4,9)
P.insert(0,1)
print("lista com insert(4,9) e P.insert(0,1): ", P)

P.pop(2)
print("lista com P.pop(2): ", P)

P.reverse()
print("lista com P.reverse(): ", P)


#DICIONARIO
print("\n --- Discionario --- \n")
meuReg = {'Nome': "Manoel", 'SobreNome': "Patrocinio", "Idade":24, "Altura":1.70}
# Acessando um elemento do dicionário
print("Nome: ", meuReg['Nome'])
# Os dicionarios são mutáveis
# Modificando um elemento do dicionario
meuReg['Nome'] = "Juninho"
# Adicionando um novo elemento
meuReg['Peso'] = 66.3
# Imprimindo o dicionário
print("Registro completo: ", meuReg)
print(meuReg.keys())
print(meuReg.values())

