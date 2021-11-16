import actividad8 as pj

lista_coches = []
while True:
    marca = input('Dime la marca del coche: ')
    if marca == 'fin':
        break
    modelo = input('Dime el modelo del coche: ')
    combustible = input('Dime el combustible del coche: ')
    cilindrada = input('Dime la cilindrada del coche: ')

    # Se crea el diccionario
    linea = {}
    linea['Marca coche'] = marca
    linea['Modelo coche'] = modelo
    linea['Combustible coche'] = combustible
    linea['Cilindrada coche'] = cilindrada

    # Se añade el diccionario a la lista
    lista_coches.append(linea)
print('Lista de coche: \n', lista_coche)

pj.store(lista_coches, 'coches.txt')
lista_coches = []
print('n\lista:\n', lista_coches)
lista_coches = pj.retrieve(coches.txt)
print('n\lista:\n', lista_coches)
