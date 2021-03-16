class proceso:

    instrucciones= 0
    memoria=0
    numero=0
    sino = 0
    primero = 0
    ultimo = 0

    def __init__(self, instrucciones, memoria, numero, sino, primero, ultimo):
        self.instrucciones= instrucciones
        self.memoria= memoria
        self.numero= numero
        self.sino = sino
        self.primero = primero
        self.ultimo = ultimo

    def getNumero(self):
        return self.numero
    def setNumero(self, instrucciones):
        self.numero= numero

    def getInstrucciones(self):
        return self.instrucciones
    def setInstrucciones(self, instrucciones):
        self.instrucciones= instrucciones

    def getMemoria(self):
        return self.memoria
    def setMemoria(self, memoria):
        self.memoria= memoria

    def PrimeroB(self, sino):
        self.sino = sino
    def PrimeroBR(self):
        return self.sino

    def getPrimero(self):
        return self.primero
    def setPrimero(self, primero):
        self.primero = primero

    def getUltimo(self):
        return self.ultimo
    def setUltimo(self, ultimo):
        self.ultimo = ultimo

    def resta(self):
        num = self.ultimo - self.primero
        return num