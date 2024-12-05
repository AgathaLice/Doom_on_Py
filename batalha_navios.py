def definir_vida(formato):
    vida = 0
    for linhas in formato:
        for itens in linhas:
            if itens == "H":
                vida += 1
    return vida

class Navio:
    def __init__(self, formato):
        self.formato = formato
        self.vida = definir_vida(formato)
navio1 = Navio([
    ["H"], 
    ["H"], 
    ["H"]
    ])
print(navio1.vida)