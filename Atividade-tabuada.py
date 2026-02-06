while True:
    tabuada = int(input("selecione o numero: "))
    contador = int(input("selecione ate onde vai: "))
 
    if tabuada < 0  or contador < 0:
        print("Para de tentar usar números negativos")
        continue

    i = 0
    while i <= contador:
        print(tabuada, "x", i, "=", tabuada * i)
        i += 1

    print("s = Sim \n n = Não")
    decisao = input("selecione se deseja colocar uma nova tabuada").lower()

    if  decisao == "s":
        print("calma ta reiniciando")
         
    elif decisao == "n":
        print("Beleza mano até")
        exit()
    else :
        print("Só tem 2 letras mano")
        break



