import numpy as np
import copy

class CuboRubik:
    def __init__(self):

        # self.cuboOrdenado = {
        #     'U': [['W']*3 for _ in range(3)],
        #     'D': [['Y']*3 for _ in range(3)],
        #     'F': [['G']*3 for _ in range(3)],
        #     'B': [['B']*3 for _ in range(3)],
        #     'L': [['O']*3 for _ in range(3)],
        #     'R': [['R']*3 for _ in range(3)]
        # }

        self.cubo2 = {
            'U': np.array([['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']]),  # Upper (arriba)
            'D': np.array([['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]),  # Down (abajo)
            'F': np.array([['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']]),  # Front (frente)
            'B': np.array([['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']]),  # Back (atrás)
            'L': np.array([['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]),  # Left (izquierda)
            'R': np.array([['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']])   # Right (derecha)
        }

        # self.cubo2 = { #L
        #     'U': np.array([['B', 'W', 'W'], ['B', 'W', 'W'], ['B', 'W', 'W']]),  # Upper (arriba)
        #     'D': np.array([['G', 'Y', 'Y'], ['G', 'Y', 'Y'], ['G', 'Y', 'Y']]),  # Down (abajo)
        #     'F': np.array([['W', 'G', 'G'], ['W', 'G', 'G'], ['W', 'G', 'G']]),  # Front (frente)
        #     'B': np.array([['B', 'B', 'Y'], ['B', 'B', 'Y'], ['B', 'B', 'Y']]),  # Back (atrás)
        #     'L': np.array([['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]),  # Left (izquierda)
        #     'R': np.array([['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']])  # Right (derecha)
        # }

        # self.cubo2 = {
        #     'U': np.array([['B', 'W', 'W'], ['B', 'W', 'W'], ['B', 'W', 'W']]),  # Upper (arriba)
        #     'D': np.array([['G', 'G', 'G'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]),  # Down (abajo) #En el Down debe ir al reves???
        #     'F': np.array([['W', 'G', 'G'], ['W', 'G', 'G'], ['O', 'O', 'O']]),  # Front (frente)
        #     'B': np.array([['B', 'B', 'Y'], ['B', 'B', 'Y'], ['R', 'R', 'R']]),  # Back (atrás)
        #     'L': np.array([['O', 'O', 'O'], ['O', 'O', 'O'], ['B', 'B', 'Y']]),  # Left (izquierda)
        #     'R': np.array([['R', 'R', 'R'], ['R', 'R', 'R'], ['W', 'G', 'G']])  # Right (derecha)
        # }

    def leer(self, file_path):
        with open(file_path, 'r') as file:
            lineas = file.readlines()
            if len(lineas) != 18:
                print("El archivo debe contener 18 líneas")

            contador_colores = {'W': 0, 'G': 0, 'R': 0, 'Y': 0, 'B': 0, 'O': 0}

            for i in range(len(lineas)):
                linea = lineas[i].strip()
                if len(linea) != 7:
                    print(f"Línea {i+1} no tiene el formato correcto")

                cara = linea[0]
                colores = linea[2:].split()
                if len(colores) != 3:
                    print(f"Línea {i+1} no tiene el formato correcto")

                for color in colores:
                     contador_colores[color] += 1

                for j in range(3):
                    self.cubo2[cara][i % 3][j] = colores[j]

            for count in contador_colores.values():
                if count != 9:
                    print("No existen 9 letras de cada color")

        return self.cubo2

    def Fd_movimiento(self): #OK
        self.cubo2['F'] = np.rot90(self.cubo2['F'], -1)
        tempFd = copy.deepcopy(self.cubo2['U'][2])
        self.cubo2['U'][2] = self.cubo2['L'][:, 2][::-1]
        self.cubo2['L'][:, 2] = np.flipud(self.cubo2['D'][0][::-1])
        self.cubo2['D'][0] = self.cubo2['R'][:, 0][::-1]
        self.cubo2['R'][:, 0] = tempFd

        return self.cubo2

    def Fi_movimiento(self): #OK
        self.cubo2['F'] = np.rot90(self.cubo2['F'])
        tempFi = copy.deepcopy(self.cubo2['U'][2][::-1])
        self.cubo2['U'][2] = self.cubo2['R'][:, 0]
        self.cubo2['R'][:, 0] = np.flipud(self.cubo2['D'][0])
        self.cubo2['D'][0] = self.cubo2['L'][:, 2]
        self.cubo2['L'][:, 2] = tempFi

        return self.cubo2
    
    def Rd_movimiento(self): #OK
        self.cubo2['R'] = np.rot90(self.cubo2['R'], -1)
        tempRd = copy.deepcopy(self.cubo2['U'][:, 2][::-1])
        self.cubo2['U'][:, 2] = self.cubo2['F'][:, 2]
        self.cubo2['F'][:, 2] = np.flipud(self.cubo2['D'][:, 2][::-1])
        self.cubo2['D'][:, 2] = self.cubo2['B'][:, 0][::-1]
        self.cubo2['B'][:, 0] = tempRd

        return self.cubo2

    def Ri_movimiento(self): #OK
        self.cubo2['R'] = np.rot90(self.cubo2['R'])
        tempRi = copy.deepcopy(self.cubo2['U'][:, 2])
        self.cubo2['U'][:, 2] = self.cubo2['B'][:, 0][::-1]
        self.cubo2['B'][:, 0] = np.flipud(self.cubo2['D'][:, 2])
        self.cubo2['D'][:, 2] = self.cubo2['F'][:, 2]
        self.cubo2['F'][:, 2] = tempRi

        return self.cubo2
    
    def Ud_movimiento(self): #OK.
        self.cubo2['U'] = np.rot90(self.cubo2['U'], -1)
        tempUd = copy.deepcopy(self.cubo2['F'][0])
        self.cubo2['F'][0] = self.cubo2['R'][0]
        self.cubo2['R'][0] = self.cubo2['B'][0]
        self.cubo2['B'][0] = self.cubo2['L'][0]
        self.cubo2['L'][0] = tempUd
        return self.cubo2

    def Ui_movimiento(self): #OK
        self.cubo2['U'] = np.rot90(self.cubo2['U'])
        tempUi = copy.deepcopy(self.cubo2['F'][0])
        self.cubo2['F'][0] = self.cubo2['L'][0]
        self.cubo2['L'][0] = self.cubo2['B'][0]
        self.cubo2['B'][0] = self.cubo2['R'][0]
        self.cubo2['R'][0] = tempUi
        return self.cubo2

    def Bd_movimiento(self): #OK
        self.cubo2['B'] = np.rot90(self.cubo2['B'], -1)
        tempBd = copy.deepcopy(self.cubo2['U'][0][::-1])
        self.cubo2['U'][0] = self.cubo2['R'][:, 2] 
        self.cubo2['R'][:, 2] = np.flipud(self.cubo2['D'][2])
        self.cubo2['D'][2] = self.cubo2['L'][:, 0]
        self.cubo2['L'][:, 0] = tempBd

        return self.cubo2

    def Bi_movimiento(self): #OK
        self.cubo2['B'] = np.rot90(self.cubo2['B'])
        tempBi = copy.deepcopy(self.cubo2['U'][0])
        self.cubo2['U'][0] = self.cubo2['L'][:, 0][::-1]
        self.cubo2['L'][:, 0] = np.flipud(self.cubo2['D'][2][::-1])
        self.cubo2['D'][2] = self.cubo2['R'][:, 2][::-1]
        self.cubo2['R'][:, 2] = tempBi 

        return self.cubo2
    
    def Ld_movimiento(self): #OK
        self.cubo2['L'] = np.rot90(self.cubo2['L'], -1)
        tempLd = copy.deepcopy(self.cubo2['U'][:, 0][::-1])
        self.cubo2['U'][:, 0] = np.flipud(self.cubo2['B'][:, 2])
        self.cubo2['B'][:, 2] = self.cubo2['D'][:, 0][::-1]
        self.cubo2['D'][:, 0] = self.cubo2['F'][:, 0]
        self.cubo2['F'][:, 0] = tempLd

        return self.cubo2

    def Li_movimiento(self): #OK
        self.cubo2['L'] = np.rot90(self.cubo2['L'])
        tempLi = copy.deepcopy(self.cubo2['U'][:, 0][::-1])
        self.cubo2['U'][:, 0] = self.cubo2['F'][:, 0]
        self.cubo2['F'][:, 0] = self.cubo2['D'][:, 0]
        self.cubo2['D'][:, 0] = np.flipud(self.cubo2['B'][:, 2])
        self.cubo2['B'][:, 2] = tempLi

        return self.cubo2
    
    def Dd_movimiento(self): #OK
        self.cubo2['D'] = np.rot90(self.cubo2['D'], -1)
        tempDi = copy.deepcopy(self.cubo2['F'][2])
        self.cubo2['F'][2] = self.cubo2['L'][2]
        self.cubo2['L'][2] = self.cubo2['B'][2]
        self.cubo2['B'][2] = self.cubo2['R'][2]
        self.cubo2['R'][2] = tempDi

        return self.cubo2

    def Di_movimiento(self): #REVISAR
        print(self.cubo2['D'])
        self.cubo2['D'] = np.rot90(self.cubo2['D'])
        print(self.cubo2['D'])

        tempDd = copy.deepcopy(self.cubo2['F'][2])

        print(self.cubo2['F'][2]," ",self.cubo2['R'][2])
        self.cubo2['F'][2] = self.cubo2['R'][2]

        print(self.cubo2['R'][2], " ",self.cubo2['B'][2]) #Validar con RD
        self.cubo2['R'][2] = self.cubo2['B'][2]

        print(self.cubo2['B'][2], " ", self.cubo2['L'][2])
        self.cubo2['B'][2] = self.cubo2['L'][2]

        print(self.cubo2['L'][2]," ", tempDd)
        self.cubo2['L'][2] = tempDd

        return self.cubo2

    def Xd_movimiento(self): #OK
        self.Ud_movimiento()
        self.Di_movimiento()
        return self.cubo2
    
    def Xi_movimiento(self): #OK
        self.Ui_movimiento()
        self.Dd_movimiento()
        return self.cubo2
    
    def Yd_movimiento(self): #OK
        self.Ld_movimiento()
        self.Ri_movimiento()
        return self.cubo2
    
    def Yi_movimiento(self): #OK
        self.Li_movimiento()
        self.Rd_movimiento()
        return self.cubo2
    
    def Zd_movimiento(self): #OK
        self.Fi_movimiento()
        self.Bd_movimiento()
        return self.cubo2
    
    def Zi_movimiento(self): #OK
        self.Fd_movimiento()
        self.Bi_movimiento()
        return self.cubo2
    

cubo_rubik = CuboRubik()
# movimientos = [cubo_rubik.Fd_movimiento(),
#                cubo_rubik.Fi_movimiento(),
#                cubo_rubik.Rd_movimiento(),
#                cubo_rubik.Ri_movimiento(),
#                cubo_rubik.Ud_movimiento(),
#                cubo_rubik.Ui_movimiento(),
#                cubo_rubik.Bd_movimiento(),
#                cubo_rubik.Bi_movimiento(),
#                cubo_rubik.Ld_movimiento(),
#                cubo_rubik.Li_movimiento(),
#                cubo_rubik.Dd_movimiento(),
#                cubo_rubik.Di_movimiento(),
#                cubo_rubik.Xd_movimiento(),
#                cubo_rubik.Xi_movimiento(),
#                cubo_rubik.Yd_movimiento(),
#                cubo_rubik.Yi_movimiento(),
#                cubo_rubik.Zd_movimiento(),
#                cubo_rubik.Zi_movimiento()
#                ]

cubo = cubo_rubik.cubo2
print("Cubo Inicial")
print(cubo)

cubo = cubo_rubik.Dd_movimiento()
cubo = cubo_rubik.Ld_movimiento()
cubo = cubo_rubik.Bi_movimiento()
cubo = cubo_rubik.Rd_movimiento()
cubo = cubo_rubik.Ud_movimiento()
cubo = cubo_rubik.Fi_movimiento()
cubo = cubo_rubik.Li_movimiento()
cubo = cubo_rubik.Fd_movimiento()
cubo = cubo_rubik.Bi_movimiento()
cubo = cubo_rubik.Di_movimiento()
print("Di")
print(cubo)

# cubo = cubo_rubik.Di_movimiento()


# cubo = cubo_rubik.Li_movimiento()
# print("Li")
# print(cubo)



# cubo = cubo_rubik.Bi_movimiento()
# print("B prima")
# print(cubo)
# cubo = cubo_rubik.Ud_movimiento()
# print("U")
# print(cubo)
# cubo = cubo_rubik.Rd_movimiento()
# print("R")
# print(cubo)


# cubo = cubo_rubik.Fi_movimiento()
# print("Cubo con Fi Movimiento")
# print(cubo)

# cubo = cubo_rubik.Rd_movimiento()
# print("Cubo con Rd Movimiento")
# print(cubo)

# cubo = cubo_rubik.Ri_movimiento()
# print("Cubo con Ri Movimiento")
# print(cubo)

# cubo = cubo_rubik.Ud_movimiento()
# print("Cubo con Ud Movimiento")
# print(cubo)

# cubo = cubo_rubik.Ui_movimiento()
# print("Cubo con Ui Movimiento")
# print(cubo)

# cubo = cubo_rubik.Bd_movimiento()
# print("Cubo con Bd Movimiento")
# print(cubo)

# cubo = cubo_rubik.Bi_movimiento()
# print("Cubo con Bi Movimiento")
# print(cubo)

# cubo = cubo_rubik.Ld_movimiento()
# print("Cubo con Ld Movimiento")
# print(cubo)

# cubo = cubo_rubik.Li_movimiento()
# print("Cubo con Li Movimiento")
# print(cubo)

# cubo = cubo_rubik.Dd_movimiento()
# print("Cubo con Dd Movimiento")
# print(cubo)

# cubo = cubo_rubik.Di_movimiento()
# print("Cubo con Di Movimiento")
# print(cubo)

# cubo = cubo_rubik.Xd_movimiento()
# print("Cubo con Xd Movimiento")
# print(cubo)

# cubo = cubo_rubik.Xi_movimiento()
# print("Cubo con Xi Movimiento")
# print(cubo)

# cubo = cubo_rubik.Yd_movimiento()
# print("Cubo con Yd Movimiento")
# print(cubo)

# cubo = cubo_rubik.Yi_movimiento()
# print("Cubo con Yi Movimiento")
# print(cubo)

# cubo = cubo_rubik.Zd_movimiento()
# print("Cubo con Zd Movimiento")
# print(cubo)

# cubo = cubo_rubik.Zi_movimiento()
# print("Cubo con Zi Movimiento")
# print(cubo)