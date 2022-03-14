#El siguiente programa creado fue tomado de una clase recibida con moises abajo esta el link del ejemplo de los carros
#Cita: en clase https://uvg.instructure.com/courses/23918/files/3721700

#Aqui se importaran los paquetes
import simpy
import random

print("*************Bienvenidos al programa TimeProgram, es un placer tenerte aqui :)************************* ")
print("-----------------------------------------------------------------------------------")
#Proceso del programa
def Program(Name,env,CPUinicio,CPUfin):
    global TiempoTotalPrograma
    #Aqui nos dara un tiempo ramdom antes de que el programa llegue al CPU
    yield env.timeout(CPUinicio)
    #Aqui sera el tiempo en que el programa llega al CPU
    Tiempoenllegar = env.now
    #Simulacion de la cantidad de tiempo requerido del programa
    Tiempodeinicio = random.randint(1, 10)
    print(f'{Name} llego al CPU en {Tiempoenllegar}, es necesario tener {CPUinicio} instrucciones para que {Name} Pueda salir del CPU')
    
    #Aqui se enviaran los programas cuando esten en el CPU, si ya esta lleno este debe esperar su turno y pornerse en cola
    with CPUfin.request() as turn:
        #Aqui recorrera todo el CPU
        yield turn
        #Aqui se simulara el tiempo en que el programa realizo el proceso
        yield env.timeout(Tiempodeinicio)
        print(f'{Name} Completo el proceso y salio a las {env.now} del CPU')
    
    TiempoTotalFinal = env.now - Tiempoenllegar
    print (f'{Name} se ha tardado {TiempoTotalFinal}')
    TiempoTotalPrograma = TiempoTotalPrograma + TiempoTotalFinal
#Aqui creara el ambiente para la simulacion    
env = simpy.Environment()
#Aqui se crea un procesador con una capasidad establecida
CPUfin = simpy.Resource(env,capacity = 2) 
random.seed(10)
proceso = 25 #cantidad de procesos que se crearan
#Aqui el tiempo iniciara en 0    
TiempoTotalPrograma = 0
#Aqui se estableceran la cantidad de programas que se correran
for i in range(proceso): 
    env.process(Program(f'Programa {i}',env,random.expovariate(1.0/10),CPUfin)) 
env.run()
print("---------------------------------------------------------------------------------------------------------")
print("Acontinuacion se te da el promedio por programa :) ")
print (f'El tiempo promedio por cada programa es: {(TiempoTotalPrograma/proceso)}')
print("----------------------------------------------------------------------------------------------------------")
print("**********Fue un placer tenerte aqui espero regreses pronto :) ")
    
    
    
    