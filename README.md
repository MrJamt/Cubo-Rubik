1. Nombre completo del autor

    Jorge Adrian Montaño Torrico

2. Breve descripción del proyecto

    El presente proyecto es una implementación del algoritmo de búsqueda A* para resolver el Cubo de Rubik de la manera más optima posible. El Cubo Rubik y su configuración esta representado dentro de la clase EstadoCubo. El algoritmo A* devuelve los movimientos que deben realizarse desde el estado inicial del cubo hasta un estado objetivo (el cubo armado). La heurística utilizada es la "distancia de Hamming", la cual mide la cantidad de colores que difieren con un cubo armado. El proyecto genera, aplica y verifica los movimientos hasta que este resuelto.

3. Requerimientos del entorno de programación

    * Lenguaje de Programación Python
    * Entorno de Desarrollo Visual Code
    * Librerias utilizadas: numpy, copy y de queue se importó PriorityQueue.
    * Archivos de estado inicial del Cubo de Rubik, los cuales seran leidos para ser resueltos posteriormente.

4. Manual de uso

4.1.Formato de codificación para cargar el estado de un cubo desde el archivo de texto

    El programa inicializa un Cubo Rubik en la clase EstadoCubo recibiendo cómo parámetro el nombre del archivo que contiene la estructura del cubo que se desea resolver.
    El archivo debe cumplir con los siguientes aspectos:
    •	Debe contener 6 lineas.
    •	Cada línea debe contener 10 caracteres separados por un espacio
    •	Únicamente el primer carácter debe ser la cara del cubo, en el siguiente orden:
    U - Arriba, F - Frente, R - Derecha, D - Abajo, B - Atrás, L – Izquierda.
    •	Seguido de los otros nueve caracteres los cuales son los colores que tiene dicha cara, recorriendo de arriba a abajo de izquierda a derecha.

4.2.Instrucciones para ejecutar el programa

    * Cumplir con los requerimientos de entorno de programacion previamente descritos
    * Escribir la ruta correspondiente de cual será el archivo de texto qué contiene el cubo para ser resuelto.
    * Ejecutar el comando: Python estado_cubo.py
    * Verificar en consola qué se imprimió el ultimo mensaje, es decir la lista con la cantidad y los movimientos que resuelven ese cubo o en caso de no poder resolverlo validar qué existe una lista vacia.

5. Diseño e implementación

5.1.Breve descripción de modelo del problema

    El modelo consiste en la resolución del cubo Rubik haciendo uso del algoritmo A* con heurística de la distancia de Hamming. Representando el cubo como un diccionario de seis caras, cada una con nueve cuadrados de colores diferentes. El objetivo es encontrar la menor cantidad de movimientos que lleve el cubo desde un estado inicial hasta un estado objetivo (el cubo armado) y que todas las caras estén ordenadas correctamente.
    El problema es sobre búsqueda en un espacio de estados, donde cada estado representa una configuración diferente del cubo. Los movimientos válidos son rotaciones de las caras del cubo en sentido horario y antihorario, para lo cual se implementa una cola de prioridad para explorar los estados del cubo de manera inteligente y prioritaria, para trabajar primero con aquellos qué según la heurística esten cerca al estado objetivo.

5.2.Explicación y justificación de algoritmo(s), técnicas, heurísticas seleccionadas.

    El algoritmo utilizado es A* con la heurística de “distancia de Hamming”, de ese modo encontrar la combinación de movimientos optima o subóptima para resolver el cubo Rubik.
    La heurística se encarga de calcular la distancia de Hamming entre el estado actual del cubo y un estado objetivo (cubo armado). La distancia de Hamming es una medida de la diferencia entre dos secuencias de elementos del mismo tamaño, contando el número de elementos en las mismas posiciones que difieren entre las dos secuencias. En este caso, la heurística cuenta el número de cubos en el estado actual que no están en la posición correcta con respecto al cubo ordenado.
    Se optó por hacer uso de esta heurística y obtener rápidamente una estimación de cuan desordenado se encuentra el cubo en comparación del estado objetivo. Además es admisible, es decir qué nunca sobreestima el costo para alcanzar la solución, ya que no puede ser mayor que la distancia real al estado objetivo, garantizando una solución muy cercana a la optima.

5.3.En caso de usar modelos lingüísticos, incluir los prompts clave.

    * Como se puede copiar un array sin perder el formato (para el caso de la librería copy con el método deepcopy)
    * Para hacer uso de heurística en el algoritmo A* es necesario comparar dos objetos (en este caso el EstadoCubo) de qué manera puedo permitir una comparación para una cola de prioridad? (para el caso de la definición de __lt__)
    * En que consiste la distancia de Hamming y cómo puedo aplicarla a este problema, considerando qué la meta es tener el cubo con las 6 caras armadas. (para comprender y codificar el calculo de la heurística)
    * Que lógica debe seguir el movimiento de la cara delantera de un cubo Rubik si lo que se desea es rotarlo 90 grados hacia la derecha y cómo varia la lógica hacia la derecha? (para comprender cómo se debe realizar un movimiento correcto y poder reflejarlo posteriormente con todas las caras)
    Posteriormente se solicito la implementación con numpy para poder facilitar el proceso de rotación y copia de los datos dentro de los arrays.

6. Trabajo Futuro

6.1.Lista de tareas inconclusas y/o ideas para continuar con el proyecto

    * Mejorar la optimización de memoria, especialmente en casos donde se requieren muchos movimientos para resolver el cubo. (cómo ser el recorte de estados redundantes o el uso de algoritmos más eficientes)
    * Buscar otros métodos de búsqueda que sean más eficientes para la optimización de memoria, por ejemplo la búsqueda iterativa en profundidad (IDDFS) o la búsqueda bidireccional.
    * Implementar algoritmos de búsqueda que ocupen menos memoria, cómo hacer uso de heurísticas más sencillas o búsqueda no informada.