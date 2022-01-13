import networkx as nx
import matplotlib.pyplot as plt
import re

class Grafo:

    # inicio el grafico al crear la clase, y le paso sus nodos y conexiones por parametros
    def __init__(self,enlaces):        
        self.grafico = nx.Graph()       
        self.grafico.add_weighted_edges_from(enlaces)
 
    # Creo el grafico con los nodos y sus aristas
    def emitoGraph(self):
        pos = nx.shell_layout(self.grafico)
        nx.draw_networkx_nodes(self.grafico, pos, node_color='green', node_size=700)
        nx.draw_networkx_labels(self.grafico, pos, font_size=10, font_family='sans-serif')
        nx.draw_networkx_edges(self.grafico, pos, edge_color='black', width=3, arrowstyle= '<|-|>', arrowsize = 10)
        labels = nx.get_edge_attributes(self.grafico, 'weight')
        nx.draw_networkx_edge_labels(self.grafico, pos, edge_labels=labels)
        plt.title("Grafico con Nodos, Aristas y sus Pesos")
        plt.axis('off')
        plt.show()
    
    def vecinos(self, nodo):
        print("\n B) Vecinos de 'b': ",list(self.grafico.neighbors(nodo)))

    def aristas_en_cada_nodo(self):
        print("\n C) Aristas de cada NODO: ",self.grafico.degree())
    
    def convertir_en_diccionario(self):
        print("\n D) Convertir en diccionario: ",dict(self.grafico.degree()))

    def matriz_de_adyacencia(self):
        M = nx.adjacency_matrix(self.grafico)
        print("\n E) Adyacencia: ",M.todense()) 
    
    def matriz_de_incidencia(self):
        I =  nx.incidence_matrix(self.grafico)
        print("\n F) Incidencia: ",I.todense())     
    
    def longitud_hasta_el_objetivo(self,nodo):
        print("\n G) Longitud de Ruta mas corta desde 'a' hasta el objetivo: ",nx.single_source_shortest_path_length(self.grafico, nodo))

    def ruta_mas_corta_floyd_warshal(self):
        print("\n H) Promedio de la ruta mas corta usando Floyd Warshall", nx.algorithms.average_shortest_path_length(self.grafico, method="floyd-warshall"))

    def ruta_mas_corta_Dijkstra(self,nodo1,nodo2):
        print("\n I) Ruta mas corta usando el algoritmo de Dijkstra entre a y g: ", nx.algorithms.dijkstra_path(self.grafico, nodo1, nodo2))

    def longitud_ruta_ponderada_entre_nodos(self,nodo1,nodo2):
        print("\n J) Longitud de Ruta ponderada más corta entre 'a' y 'g' :",nx.dijkstra_path_length(self.grafico,nodo1,nodo2)) 

    def longitud_ruta_de_determinado_nodo(self,nodo):
        print("\n K) Longitud de Ruta más corta desde el nodo 'c':", nx.single_source_dijkstra_path_length(self.grafico,nodo))

    def radio(self):
        print("\n L) Radio: %d" % nx.radius(self.grafico))
    
    def diametro(self):
        print("\n M) Diámetro: %d" % nx.diameter(self.grafico))
    
    def excentricidad(self):
        print("\n N) Excentricidad: %s" % nx.eccentricity(self.grafico))
    
    def centro(self):
        print("\n O) Centro: %s" % nx.center(self.grafico))

    def periferia(self):
        print("\n P) Periferia: %s" % nx.periphery(self.grafico))

    def densidad(self):
        print("\n Q) Densidad: %s" % nx.density(self.grafico))

    # Creo el grafico dirigido a traves de una funcion, definiendo pos y H, lo demas se copia para modificar colores
    # independiente al grafico original
    def emitoGraficodirigido(self):
        H = self.grafico.to_directed()
        pos = nx.shell_layout(H)
        nx.draw_networkx_nodes(H, pos, node_color='purple', node_size=700)
        nx.draw_networkx_labels(H, pos, font_size=10, font_family='sans-serif')
        nx.draw_networkx_edges(H, pos, edge_color='red', width=3, arrowstyle= '<|-|>', arrowsize = 10)
        labels = nx.get_edge_attributes(H, 'weight')
        nx.draw_networkx_edge_labels(H, pos, edge_labels=labels)
        plt.title("Grafico Dirigido")
        plt.axis('off')
        plt.show() 

G = Grafo([('a', 'b', 5),('a', 'd', 6),
           ('b', 'c', 5),('b', 'e', 6),('b', 'g', 7),
           ('c', 'g', 2),
           ('d', 'f', 5),('d','g',9),
           ('e', 'a', 3),('e','d',2),
           ('f','g',9)])

G.vecinos('b')
G.aristas_en_cada_nodo()
G.convertir_en_diccionario()
G.matriz_de_adyacencia()
G.matriz_de_incidencia()
G.longitud_hasta_el_objetivo('a')
G.ruta_mas_corta_floyd_warshal()
G.ruta_mas_corta_Dijkstra('a','g')
G.longitud_ruta_ponderada_entre_nodos('a','g')
G.longitud_ruta_de_determinado_nodo('c')
G.radio()
G.diametro()
G.excentricidad()
G.centro()
G.periferia()
G.densidad()

# Emito Grafico de nodos con sus aristas
G.emitoGraph()

# Emito Grafico DIRIGIDO llamandolo desde su propia funcion
G.emitoGraficodirigido()

# Ejercicio 3
texto = """
1,Ciudad Autónoma de Buenos Aires (CABA),AR-C
2,Buenos Aires,AR-B
3,Catamarca,AR-K
4,Córdoba,AR-X
5,Corrientes,AR-W
6,Entre Ríos,AR-E
7,Jujuy,AR-Y
"""

buscar = r'(?<=,)[^\n]+(?=,)|(?<=-)[A-Z]+(?=\n)'
x = re.findall(buscar,texto)
print("\n Texto obtenido en la busqueda ", x)