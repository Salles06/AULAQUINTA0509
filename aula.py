# Exemplo de string
texto = "Olá, Mundo"

# Fatiar do inicio até um indice especifico
print(texto [:5])   #Saída:"Olá,"

# Fatiar do inicio até um indice especifico até o final
print(texto[6:])     #Saída: "Mundo"

# Fatiar do inicio até o final, com um passo especifico
print(texto[::2])    # Saída: "O ,ud"

# Fatiar com inicio e fim especifico
print(texto [4:9])  #Saída: ", Mun"

#Fatiar com passo negativo para inverter uma substring
print(texto[::-1])   # Saída "odnuM, Olá"