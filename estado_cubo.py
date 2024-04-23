import numpy as np
import copy
from queue import PriorityQueue

class EstadoCubo:
    def __init__(self, archivo):
        self.cubo = self.leer(archivo)
        self.costo = 0

    def __lt__(self, other):
        return self.costo < other.costo

    def leer(self, archivo):
        cubo = {}
        with open(archivo, 'r') as file:
            lineas = file.readlines()

            if len(lineas) != 6:
                print("El archivo debe contener exactamente 6 lineas")
                return None

            for linea in lineas:
                if len(linea.strip()) != 19:
                    print("Cada línea debe contener la cara y los 9 colores separados por un espacio")
                    return None

                partes = linea.split()
                cara = partes[0]
                colores = partes[1:]

                grupos = []
                for i in range(0, len(colores), 3):
                    grupo = colores[i:i+3]
                    grupos.append(grupo)

                colores_grupo = np.array(grupos)

                cubo[cara] = colores_grupo

        contador_colores = {'W': 0, 'G': 0, 'R': 0, 'Y': 0, 'B': 0, 'O': 0}
        for cara, colores in cubo.items():
            for fila in colores:
                for color in fila:
                    contador_colores[color] += 1

        for color, cantidad in contador_colores.items():
            if cantidad != 9:
                print(f"La cantidad de '{color}' debe ser exactamente 9")
                return None

        return cubo

    def mover(self, movimiento):
        movimientos = {
            "F (Front Derecha)": self.Fd, "F' (Front Izquierda)": self.Fi,
            "B (Back Derecha)": self.Bd,  "B' (Back Izquierda)": self.Bi,
            "L (Left Derecha)": self.Ld,  "L' (Left Izquierda)": self.Li,
            "R (Right Derecha)": self.Rd, "R' (Right Izquierda)": self.Ri,
            "U (Upper Derecha)": self.Ud, "U' (Upper Izquierda)": self.Ui,
            "D (Down Derecha)": self.Dd,  "D' (Down Izquierda)": self.Di
        }

        if movimiento in movimientos:
            movimientos[movimiento]()
        else:
            print("Movimiento Invalido")
        return self.cubo
    
    def Fd(self):
        self.cubo['F'] = np.rot90(self.cubo['F'], -1) 
        tempFd = copy.deepcopy(self.cubo['U'][2])
        self.cubo['U'][2] = self.cubo['L'][:, 2][::-1]
        self.cubo['L'][:, 2] = np.flipud(self.cubo['D'][0][::-1])
        self.cubo['D'][0] = self.cubo['R'][:, 0][::-1]
        self.cubo['R'][:, 0] = tempFd

        return self.cubo

    def Fi(self):  
        self.cubo['F'] = np.rot90(self.cubo['F'])
        tempFi = copy.deepcopy(self.cubo['U'][2][::-1])
        self.cubo['U'][2] = self.cubo['R'][:, 0]
        self.cubo['R'][:, 0] = np.flipud(self.cubo['D'][0])
        self.cubo['D'][0] = self.cubo['L'][:, 2]
        self.cubo['L'][:, 2] = tempFi

        return self.cubo
    
    def Rd(self): 
        self.cubo['R'] = np.rot90(self.cubo['R'], -1)
        tempRd = copy.deepcopy(self.cubo['U'][:, 2][::-1])
        self.cubo['U'][:, 2] = self.cubo['F'][:, 2]
        self.cubo['F'][:, 2] = np.flipud(self.cubo['D'][:, 2][::-1])
        self.cubo['D'][:, 2] = self.cubo['B'][:, 0][::-1]
        self.cubo['B'][:, 0] = tempRd

        return self.cubo

    def Ri(self):  
        self.cubo['R'] = np.rot90(self.cubo['R'])
        tempRi = copy.deepcopy(self.cubo['U'][:, 2])
        self.cubo['U'][:, 2] = self.cubo['B'][:, 0][::-1]
        self.cubo['B'][:, 0] = np.flipud(self.cubo['D'][:, 2])
        self.cubo['D'][:, 2] = self.cubo['F'][:, 2]
        self.cubo['F'][:, 2] = tempRi

        return self.cubo
    
    def Ud(self):
        self.cubo['U'] = np.rot90(self.cubo['U'], -1)
        tempUd = copy.deepcopy(self.cubo['F'][0])
        self.cubo['F'][0] = self.cubo['R'][0]
        self.cubo['R'][0] = self.cubo['B'][0]
        self.cubo['B'][0] = self.cubo['L'][0]
        self.cubo['L'][0] = tempUd
        return self.cubo

    def Ui(self): 
        self.cubo['U'] = np.rot90(self.cubo['U'])
        tempUi = copy.deepcopy(self.cubo['F'][0])
        self.cubo['F'][0] = self.cubo['L'][0]
        self.cubo['L'][0] = self.cubo['B'][0]
        self.cubo['B'][0] = self.cubo['R'][0]
        self.cubo['R'][0] = tempUi
        return self.cubo

    def Bd(self): 
        self.cubo['B'] = np.rot90(self.cubo['B'], -1)
        tempBd = copy.deepcopy(self.cubo['U'][0][::-1])
        self.cubo['U'][0] = self.cubo['R'][:, 2] 
        self.cubo['R'][:, 2] = np.flipud(self.cubo['D'][2])
        self.cubo['D'][2] = self.cubo['L'][:, 0]
        self.cubo['L'][:, 0] = tempBd

        return self.cubo

    def Bi(self):  
        self.cubo['B'] = np.rot90(self.cubo['B'])
        tempBi = copy.deepcopy(self.cubo['U'][0])
        self.cubo['U'][0] = self.cubo['L'][:, 0][::-1]
        self.cubo['L'][:, 0] = np.flipud(self.cubo['D'][2][::-1])
        self.cubo['D'][2] = self.cubo['R'][:, 2][::-1]
        self.cubo['R'][:, 2] = tempBi 

        return self.cubo
    
    def Ld(self): 
        self.cubo['L'] = np.rot90(self.cubo['L'], -1)
        tempLd = copy.deepcopy(self.cubo['U'][:, 0])
        self.cubo['U'][:, 0] = np.flipud(self.cubo['B'][:, 2])
        self.cubo['B'][:, 2] = self.cubo['D'][:, 0][::-1]
        self.cubo['D'][:, 0] = self.cubo['F'][:, 0]
        self.cubo['F'][:, 0] = tempLd

        return self.cubo

    def Li(self): 
        self.cubo['L'] = np.rot90(self.cubo['L'])
        tempLi = copy.deepcopy(self.cubo['U'][:, 0][::-1])
        self.cubo['U'][:, 0] = self.cubo['F'][:, 0]
        self.cubo['F'][:, 0] = self.cubo['D'][:, 0]
        self.cubo['D'][:, 0] = np.flipud(self.cubo['B'][:, 2])
        self.cubo['B'][:, 2] = tempLi

        return self.cubo
    
    def Dd(self): 
        self.cubo['D'] = np.rot90(self.cubo['D'], -1)
        tempDi = copy.deepcopy(self.cubo['F'][2])
        self.cubo['F'][2] = self.cubo['L'][2]
        self.cubo['L'][2] = self.cubo['B'][2]
        self.cubo['B'][2] = self.cubo['R'][2]
        self.cubo['R'][2] = tempDi

        return self.cubo

    def Di(self): 
        self.cubo['D'] = np.rot90(self.cubo['D'])
        tempDd = copy.deepcopy(self.cubo['F'][2])
        self.cubo['F'][2] = self.cubo['R'][2]
        self.cubo['R'][2] = self.cubo['B'][2]
        self.cubo['B'][2] = self.cubo['L'][2]
        self.cubo['L'][2] = tempDd
        return self.cubo

    def estaResuelto(self):
        for cara, color in {'U': 'W', 'D': 'Y', 'F': 'G', 'R': 'R', 'L': 'O', 'B': 'B'}.items():
            if not np.all(self.cubo[cara] == color):
                return False
        return True

    def posiblesMovimientos(self):
        return ["F (Front Derecha)", "F' (Front Izquierda)",
                "B (Back Derecha)", "B' (Back Izquierda)",
                "L (Left Derecha)", "L' (Left Izquierda)",
                "R (Right Derecha)", "R' (Right Izquierda)",
                "U (Upper Derecha)", "U' (Upper Izquierda)",
                "D (Down Derecha)", "D' (Down Izquierda)"]

def mostrar(cubo):
    print("-------------")
    for cara, valor in cubo.items():
        print(f"'{cara}':")
        for fila in valor:
            print(fila)
        print("-------------")

def heuristica(cubo):
    cubo_ordenado = EstadoCubo("cubos\\1linea\\cuboOrdenado.txt").cubo
    distancia_total = 0
    for cara, cara_ordenada in cubo_ordenado.items():
        distancia_total += np.sum(cubo.cubo[cara] != cara_ordenada)
    return distancia_total

def resolver(estado_inicial):
    priority_queue = PriorityQueue()
    priority_queue.put((0, estado_inicial, []))
    visitados = set()

    while not priority_queue.empty():
        costo, estado_actual, movimientos = priority_queue.get()
        if estado_actual.estaResuelto():
            return movimientos,estado_actual

        if estado_actual in visitados:
            continue
        visitados.add(estado_actual)

        for movimiento in estado_actual.posiblesMovimientos():
            nuevo_estado = copy.deepcopy(estado_actual)
            nuevo_estado.mover(movimiento)
            nuevo_costo = len(movimientos) + heuristica(nuevo_estado)
            priority_queue.put((nuevo_costo, nuevo_estado, movimientos + [movimiento]))

    return [], estado_actual

cubo_rubik = EstadoCubo("cubos\\1linea\\cubo5Mov2.txt")
print("CUBO INCIIAL")
mostrar(cubo_rubik.cubo)
movimientos,cubo_rubik = resolver(cubo_rubik)
print("CUBO FINAL")
mostrar(cubo_rubik.cubo)
print(f"Movimientos ({len(movimientos)}):", movimientos)