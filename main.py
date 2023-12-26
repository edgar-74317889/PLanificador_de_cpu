from termcolor import colored, cprint
def firstComeFirstServed(procesos):
    arrEspera = []
    tiempoEspera = 0
    tiempoTotal = 0
    print()
    print("FIRST-COME FIRST-SERVED")
    for k,v in procesos.items():
        t = colored(f"   {k}   ", "yellow", attrs=["reverse", "blink"])
        print(t,end=" ")
        arrEspera.append(tiempoEspera)
        tiempoTotal+=tiempoEspera
        tiempoEspera+=v
    print()
    #Sacar los valores para despues agregar a la lista de tiempos de espera para poder graficar
    valores = list(procesos.values())
    arrEspera.append(valores[-1]+arrEspera[-1])
    for i in range(len(arrEspera)-1):        
        cprint(f"{arrEspera[i]}     {arrEspera[i+1]}","blue",end=" ",attrs=["bold"])
    print()
    cprint(f"Tiempo promedio: {tiempoTotal/len(procesos)}","green") 
        
def shortestJobFirst(procesos):
    #ordenar de menor a mayor
    print()
    print("SHORTEST JOB FIRST")

    tiempoEspera = 0
    arrEspera = []
    tiempoTotal = 0
    procesosOrdenados = {}
    #ordenar por values
    for x in sorted(procesos, key = lambda k: procesos[k]):
        procesosOrdenados[x]=procesos[x]
    for k,v in procesosOrdenados.items():
        t = colored(f"  {k}  ", "red", attrs=["reverse", "blink"])
        print(t,end=" ")
        #print(f"Proceso {k} completado. Tiempo de espera {tiempoEspera}")
        arrEspera.append(tiempoEspera)
        tiempoTotal+=tiempoEspera
        tiempoEspera+=v
    print()
    #Sacar los valores para despues agregar a la lista de tiempos de espera para poder graficar
    valores = list(procesosOrdenados.values())
    arrEspera.append(valores[-1]+arrEspera[-1])
    for i in range(len(arrEspera)-1):        
        cprint(f"{arrEspera[i]}    {arrEspera[i+1]}","blue",end=" ",attrs=["bold"])
    print()
    cprint(f"Tiempo promedio: {tiempoTotal/len(procesos)}","green")           
def planificacionPrioritaria(procesos, prioridad):
    print()
    prioridadOrdenada = {}
    arrEspera = []
    tiempoEspera = 0
    tiempoTotal = 0
    print("PLANIFICACION PRIORITARIA")
    #
    for x in sorted(prioridad, key = lambda k: prioridad[k]):
        prioridadOrdenada[x]=prioridad[x]
    for k, v in prioridadOrdenada.items():
        t = colored(f"  {k}  ", "magenta", attrs=["reverse", "blink"])
        print(t,end=" ")
        arrEspera.append(tiempoEspera)
        tiempoTotal+=tiempoEspera
        tiempoEspera+=procesos[k]
    print()
    arrEspera.append(sum(procesos.values()))
    for i in range(len(arrEspera)-1):        
        cprint(f"{arrEspera[i]}    {arrEspera[i+1]}","blue",end=" ",attrs=["bold"])
    print()
    cprint(f"Tiempo promedio: {tiempoTotal/len(procesos)}","green")   
    
def roundRobin(procesos, quantum):
    print()
    print("ROUND ROBIN")
    tiempo = sum(procesos.values())
    tiempoEspera = 0
    tiempoTotal = 0
    arrEspera = []
    # para cambiar solo el array arrcambiar
    arrCambiar = procesos.copy()
    contador = 0
    for i in range(tiempo+quantum*len(procesos)):          
        aux = contador    
        #l es el limite a partir del contador + el num de procesos
        l = aux + len(procesos)
        #para buscar entre los procesos en orden 
        while(aux<l):
            # x es el proceso P1,P2,P3,etc
            x = "P"+str(int(contador%len(procesos))+1)
            if arrCambiar[x] > 0:
                if arrCambiar[x]<=quantum:
                    t = colored(f"  {x}  ", "cyan", attrs=["reverse", "blink"])
                    print(t,end=" ")
                    arrEspera.append(tiempoEspera)
                    tiempoTotal+=tiempoEspera
                    tiempoEspera+=arrCambiar[x]
                    arrCambiar[x]=0
                    contador+=1
                    break
                else:
                    t = colored(f"  {x}  ", "cyan", attrs=["reverse", "blink"])
                    print(t,end=" ")
                    arrEspera.append(tiempoEspera)
                    tiempoEspera+=quantum
                    arrCambiar[x]-=quantum
                    contador+=1
                    break
            else:
                contador+=1
                break
    print()
    s = sum(procesos.values())
    arrEspera.append(s)
    for i in range(len(arrEspera)-1):        
        cprint(f"{arrEspera[i]}    {arrEspera[i+1]}","blue",end=" ",attrs=["bold"])
    print()
    cprint(f"Tiempo promedio: {tiempoTotal/len(procesos)}","green")             
                      
if __name__ == "__main__":
    procesos={}
    prioridad={}
    
    textMenu = colored("         TIPO DE PLANIFICACION         ", "red", attrs=["reverse", "blink"])
    texto = "1. Round Robin\n2. Planificacion prioritaria\n3. First-Come First-Served\n4. Shortest Job First \n5. Todos"   
    print(textMenu)
    print(texto)
    
    tipoPlanificacion = input("Elige una opcion: ")
    n = int(input("Cantidad de procesos: "))
    if tipoPlanificacion == "1" or tipoPlanificacion=="5":
        quantum = int(input("quantum: "))

    for i in range(n):
        p = "P"+str(i+1)
        print(p)
        tiempoRafaga = int(input("Tiempo de Rafaga: "))
        if tipoPlanificacion == "2" or tipoPlanificacion=="5":
            prioridad[p] = int(input("Prioridad: "))    
        procesos[p] = tiempoRafaga

    if tipoPlanificacion == '1':
        roundRobin(procesos,quantum)
    elif tipoPlanificacion == '2':
        planificacionPrioritaria(procesos,prioridad)    
    elif tipoPlanificacion == '3':
        firstComeFirstServed(procesos)
    elif tipoPlanificacion == '4':
        shortestJobFirst(procesos)
    elif tipoPlanificacion == '5':
        roundRobin(procesos,quantum)
        planificacionPrioritaria(procesos, prioridad)
        firstComeFirstServed(procesos)
        shortestJobFirst(procesos)