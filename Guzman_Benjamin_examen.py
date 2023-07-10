from os import system
system("cls")

asientos=list(range(1,101))
reservar=[None]*100
asistentes=[None]*30
registro=[]
total=[]
platinum=120000
gold=80000
silver=50000

def menu():
    """Bienvenido compra tu entrada:
    -Valores de entradas=

    -Platinum 120000(Asientos del 1 al 20)
    -Gold 80000 (Asientos del 21 al 50)
    -Silver 50000 (Asientos del 51 al 100)
    
    

    Opciones:
    1.Comprar entrada
    2.Mostrar asientos
    3.ver listado de asistentes 
    4.ganancias totales
    5.Cerrar programa
    """
def pausa():
    input("Presione una tecla para continuar...")
    limpiar("cls")

def limpiar():
    from os import system
    system("cls")
    

def comprar_entrada(nom:str):
    while True:
        print("seleccione el tipo de entrada que desea comprar:")
        pausa
        print("1.-Platinum 120000(Asientos del 1 al 20) ","2.Gold 80000 (Asientos del 21 al 50)","3.Silver 50000 (Asientos del 51 al 100)")
        op=input()
        match op:
  
             
             case "1":
                asiento=input("Indique el número de asiento para comprar y X para salir: ")
        if asiento.lower()=="x":
                return
        else:
            if asiento in reservar and len(asiento)==range (1, 20)and reservar[(int(asiento))-1]!="X":
                reservar[(int(asiento))-1]="X"
                registro[(int(asiento))-1]=nom
                valor_entrada=1*120000
                cant_entradas=input("ingrese cuantas entradas de este tipo desea:".isnumeric)
                valor_ingreso=valor_entrada*cant_entradas
                total.append(valor_ingreso)
                print(valor_entrada)
                print("entrada comprada exitosamente!!!.....")             
            else:
                print("Número de auto no válido o ocupado")
                pass
            case "2":
            asiento=input("Indique el número de asiento para comprar y X para salir: ")
        if asiento.lower()=="x":
                return
        else:
            if asiento in reservar and len(asiento)==range (21, 50)and reservar[(int(asiento))-1]!="X":
                reservar[(int(asiento))-1]="X"
                registro[(int(asiento))-1]=nom
                valor_entrada=1*80000
                cant_entradas=input("ingrese cuantas entradas de este tipo desea:".isnumeric)
                valor_ingreso=valor_entrada*cant_entradas
                total.append(valor_ingreso)
                print(valor_entrada)
                print("entrada comprada exitosamente!!!.....")
                
            else:
                print("Número de auto no válido o ocupado")
            case "3":
            asiento=input("Indique el número de asiento para comprar y X para salir: ")
        if asiento.lower()=="x":
                return
        else:
            if asiento in asientos and len(asiento)==range (51, 100)and asientos[(int(asiento))-1]!="X":
                asientos[(int(asiento))-1]="X"
                registro[(int(asiento))-1]=nom
                valor_entrada=1*50000
                cant_entradas=input("ingrese cuantas entradas de este tipo desea:")
                valor_ingreso=valor_entrada*cant_entradas
                total.append(valor_ingreso)
                print(valor_entrada)
                print("entrada comprada exitosamente!!!.....")
                
            else:
                print("Número de auto no válido o ocupado")
            
def disponibilidad_asientos():
        for a in asientos:
            print("|", end="")
            print(a, end="| ")        
def asistentes_ingresados():
     
     

def ganancias_totales(total):
    suma = 0
    for valor_ingreso in total:
        suma += valor_ingreso
    return suma
    
while True:
    menu()
    op=input("ingrese una opcion:")
    match op:
         
        case "1":
              nom=input("ingrese nombre del comprador".isalpha)
              comprar_entrada()
              pass
        case "2":
              disponibilidad_asientos()
              pass
        case "3":
              print(asistentes_ingresados)
        case "4":
              print("las ganacias totales son:"),total
        case "5":
                print("FIN DEL PROGRAMA")
                pausa()
                