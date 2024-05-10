class Criterion():
    def calcularImpureza(self,nodo:ArbolN):
        ...
    def mejorParticion(self,datos:pd.DataFrame):
        ...
    def rankingFeatures(self,datos):
        ...

class CriterionContiuous(Criterion):
    def calcularUmbral(self,datos:pd.Dataframe, feature:str):
        ...


class Entropia(CriterionContiuous):
    def mejorParticion(self, datos: pd.DataFrame):
        #para cada feature, evaluo si es continuo o categorico y decido
        '''
        if categorico:
            Entropia(D)
            IG(D) para feature y lo 

        else: contiuo
            IG() SI() -> GR()
        
        A partir de lista de feature + puntaje, elijo max()

        '''

class NodoID3():
    def __init__(self) -> None:
        self.criterio = ...
    def engendrar(self):
        feature_corte = self.criterio.mejorParticion(self.datos)
        ...

class NodoC45():
    def __init__(self) -> None:
        self.criterio = ...
    def engendrar(self):
        feature_corte = self.criterio.mejorParticion(self.datos)
        umbral = self.criterio.calcularUmbral(self.datos,feature_corte)

ArbolDeDecision(datos,criterio,poda)


class ArbolDeDecision():
    def __init__(self,datos,criterio,poda) -> None:
        self.raiz = NodoID3(datos,criterio)
        self.funcDivisionNodos = len

    def getCriterio(self):
        return self.raiz.criterio
    
    def engendrarHijo(self):
        self.raiz.engendrar(self.funcDivisionNodos(self.datos.columns))
    
"""Opociones: investigar RPP (leer el codigo fuente de sklearn) o implementarlo sin RPP (hacerlo por eliminacion de nodos y chau)
Efectivamente, si eliminas una hoja, redistribuis los datos a los hermanos"""

