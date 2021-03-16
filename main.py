import simpy
import random
import statistics
from random import randrange
from cola import Cola
from proceso import proceso

env = simpy.Environment() #ambiente de simulación
RAM = simpy.Container(env, init=100, capacity=200) #RAM
CPU = simpy.Resource(env, capacity=1)
CPU2 = simpy.Resource(env, capacity=1)

#colas
cola_new= Cola()
cola_new.new()
cola_ready= Cola()
cola_ready.new()

#varibles
intervalo= 10
procesos = int(random.expovariate(1.0 / intervalo))
contador=0
numeros=[]

"""----------------------------------------------------------------------------------------------------"""

def sumaNum(numeros, procesos):
    
    numerosMax = 0
    print("Con : " + str(len(numeros) + 1) + " cantidad de procesos")
    for i in range (len(numeros)):
        #print(i)
        temp = numeros[i]
        numerosMax = numerosMax + temp

    n = numerosMax/len(numeros)
    print("El promedio es " + str(n))
    print("La desviacion estandar es " + str(statistics.stdev(numeros)))

"""----------------------------------------------------------------------------------------------------"""
def simulador(procesos):
    
    print("Genero la cantidad de procesos:" + str(procesos))

    for i in range(procesos):
        memoria= randrange(1,10)
        instrucciones= randrange(1,10)
        numero= str(i+1)
        p= proceso(instrucciones, memoria, numero, 0, 0, 0)
        cola_new.enqueue(p)
        print("Proceso " + str(p.getNumero()) + " ,memoria: " + str(p.getMemoria()) + " , instrucciones: " + str(p.getInstrucciones()))
        if(i == procesos+1):
            cola_new.enqueue(p)

    print("Genero la cantidad de procesos:" + str(procesos)) 

    """--------------------------------------------------------------------------------------"""    

    conta = 0
    while(cola_new.isEmpty()==False):
        conta = conta + 1
        
        if(conta == procesos+1):
            print("ya esta terminado.")
        else:
            pro= cola_new.dequeue()
            new(pro)
            env.run()
            


"""----------------------------------------------------------------------------------------------------"""

"""Funcion new"""
def new (proceso): 
    print("El proceso " + proceso.getNumero() + " entro al estado new")
    mem= proceso.getMemoria()

    RAMcapacidad = RAM._capacity - mem

    if(RAMcapacidad > 0): #si necesita menos memoria de la que hay lo mete a ready
        RAM.get(mem)
        cola_ready.enqueue(proceso)
        ready(proceso)
        
def ready(proceso):
    print("El proceso " + proceso.getNumero() + " entro al estado ready")

    for i in range(cola_ready.size()-3):
        listo= cola_ready.dequeue()
        #listo2= cola_ready.dequeue()
        env.process(running(listo,env))#se podria ser con entraA
        #env.process(running2(listo2,env))#se podria ser con entraA

"""Funcion running"""
def running(proceso,env):

    with CPU.request() as req:
        yield req
        print("El proceso numero: " + proceso.getNumero() + " ha entrado a running en tiempo: " +str(env.now))

        num = proceso.PrimeroBR() + 1
        proceso.PrimeroB(num)
        if(proceso.PrimeroBR() == 1):
            proceso.setPrimero(env.now)

        yield env.timeout(3)

        print("El proceso numero: " + proceso.getNumero() + " ha salido de running en tiempo: " +str(env.now))

    proceso.setInstrucciones((proceso.getInstrucciones()-3))
    if(proceso.getInstrucciones()<=0):
        terminated(proceso, env)
        
    else:
        waiting(proceso)

"""Funcion running"""
def running2(proceso,env):

    with CPU2.request() as req:
        yield req
        print("El proceso numero: " + proceso.getNumero() + " ha entrado a running en tiempo: " +str(env.now))

        num = proceso.PrimeroBR() + 1
        proceso.PrimeroB(num)
        if(proceso.PrimeroBR() == 1):
            proceso.setPrimero(env.now)

        yield env.timeout(3)

        print("El proceso numero: " + proceso.getNumero() + " ha salido de running en tiempo: " +str(env.now))

    proceso.setInstrucciones((proceso.getInstrucciones()-3))
    if(proceso.getInstrucciones()<=0):
        terminated(proceso, env)
        
    else:
        waiting(proceso)
        


def terminated(proceso, enviroment):
    mem= proceso.getMemoria()
    RAM.put(mem)
    print("El proceso " + proceso.getNumero() + " entro al estado terminated en tiempo: " + str(enviroment.now))
    proceso.setUltimo(enviroment.now)

    h = proceso.resta()
    numeros.append(h)

def waiting(proceso):
    print("El proceso " + proceso.getNumero() + " entro al estado waiting")

    aleatorio= randrange(1,3)

    if(aleatorio==1):
        cola_ready.enqueue(proceso)  
        #print("El proceso " + proceso.getNumero() + " entro a ready")
    

    if(aleatorio==2):
        waiting(proceso)
        #print("El proceso " + proceso.getNumero() + " entro a waiting")
        
"""-----------------------------------------------------------------------------------------------"""
simulador(25)
suma = sumaNum(numeros, procesos)


