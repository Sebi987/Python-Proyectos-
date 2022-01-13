"""
En una zona del país, se realizó una encuesta de opinión a 1000 personas sobre 3 (tres)
categorías: Economía, Educación y Seguridad, y otras sub-categorías especificadas
sólo para Economía. Los datos se recolectaron en las siguientes estructuras:
"""
# 680 opinaron sobre Ecomomía.
Economia_gastos = {"Gasto_público": 40, "Impuestos": 118, "Política_y_gobierno": 50, "Deuda_externa": 95,"Privilegios": 56, "Corrupción":  131, "Obra_pública": 103, "Planes": 87}
"""
"""
# 320 opinaron sobre Seguridad.
Seguridad = (40, 50, 60, 75, 34, 61)
"""
"""
# 490 opinaron sobre Educación
Educacion = [34, 40, 61, 75, 87, 90, 103]
"""
En relación a los datos obtenidos:
    1) realizar las operaciones correspondientes
    2) realizar el diagrama de venn
    3) Responder en el gráfico las siguientes preguntas:
        a. cuántos opinaron sobre Seguridad, Educación y Economía.
        b. cuántos opinaron sobre sólo Economía y Educación?
        c. cuántos opinaron sobre sólo Economía?
        d. cuántos opinaron sobre solo Seguridad?
        e. cuántos opinaron sobre sólo Educación? 
        f. cuántos opinaron sobre 2 de las 3 categorías?
"""

from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

Universal = 1000

#DIAGRAMA
D = venn3({'111':1,'110':1,"101":1,"100":1,"011":1,"010":1,"001":1},set_labels=('Economia','Seguridad','Educacion'))
for subset in ("111", "110", "101", "100","011", "010", "001"): D.get_label_by_id(subset).set_text(subset)

#Utilizo el set, para poder resolver las intersecciones y cuentas
def set_Economia(Economia_gastos):
    Economia = set()
    for elemento in Economia_gastos.values():
        Economia.add(elemento)
    return Economia

Economia = set_Economia(Economia_gastos)
Seguridad = set(Seguridad)
Educacion = set(Educacion)

#FUNCIONES

#TODAS LAS CATEGORIAS
def todas_categorias(Ec,S,Ed):
    return (Ec & S & Ed)
todasCategorias = todas_categorias(Economia,Seguridad,Educacion);D.get_label_by_id('111').set_text(sum(todasCategorias))

#INTERSECCIONES
def interseccion(P,D,TC):
    return (P & D) - TC
Eco_Seg = interseccion(Economia, Seguridad, todasCategorias);D.get_label_by_id('110').set_text(sum(Eco_Seg))
Eco_Edu = interseccion(Economia, Educacion, todasCategorias);D.get_label_by_id('101').set_text(sum(Eco_Edu))
Seg_Edu = interseccion(Seguridad, Educacion, todasCategorias);D.get_label_by_id('011').set_text(sum(Seg_Edu))

#SOLO CADA CATEGORIA
def categoriaIndividual(L,P,K):
    return (L - P) & (L - K)
solo_Economia = categoriaIndividual(Economia,Seguridad,Educacion);D.get_label_by_id('100').set_text(sum(solo_Economia))
solo_Seguridad = categoriaIndividual(Seguridad,Economia,Educacion);D.get_label_by_id('010').set_text(sum(solo_Seguridad))
solo_Educacion = categoriaIndividual(Educacion, Seguridad,Economia);D.get_label_by_id('001').set_text(sum(solo_Educacion))

#RESPUESTAS
plt.text(-1.60, 0,s="Respuestas " + str(), size=10, ha="left", va="bottom",bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.3),))
plt.text(-1.60, -0.10, s="Opinaron de las 3 categorias = " + str(sum(todasCategorias)), size=10, ha="left", va="bottom",bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(-1.60, -0.20, s="Opinaron solo de Economia y Educacion = " + str(sum(Eco_Edu)), size=10, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(-1.60, -0.30, s="Opinaron solo Economia = " + str(sum(solo_Economia)), size=10, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(-1.60, -0.40, s="Opinaron solo Seguridad = " + str(sum(solo_Seguridad)), size=10, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(-1.60, -0.50, s="Opinaron solo Educacion = " + str(sum(solo_Educacion)), size=10, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(-1.60, -0.60, s="Opinaron 2 de las 3 categorias = " + str(sum(Eco_Edu) + sum(Eco_Seg) + sum(Seg_Edu)), size=10, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.26, -0.70, s="Personas = " + str(Universal), size=10, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.1, 0.8),))

#DIAGRAMA POR FUERA
venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1),color="#000000", alpha=1, linestyle="-",linewidth=3)
plt.title("CATEGORIAS")
plt.axis('on')
plt.show()