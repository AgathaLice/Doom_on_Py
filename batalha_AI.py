def definir_vida(formato):
        for linhas in formato:
            for itens in linhas:
                if itens == "H":
                    vida += 1

class Navio:
    def __init__(self, formato):
        self.formato = formato
        self.vida = definir_vida(formato)
navio1 = 
print()