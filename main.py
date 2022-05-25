velocidade = int(input("Usuário digite a velocidade em km/h "))
KmMedio = float(input("Usuário digite a media de consumo de km/L "))

distancia = 5 * velocidade

print("Viajando 5 horas será percorrido a distancia de: ",distancia,"km")
print("Para viajar está distancia será necessario ",distancia / KmMedio, "litros de combustivel ")