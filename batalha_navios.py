def definir_vida(formato):
    vida = 0
    for linhas in formato:
        for itens in linhas:
            if itens == "X":
                vida += 1
    return vida

class Navio:
    def __init__(self, formato, quantidade):
        self.formato = formato
        self.vida = definir_vida(formato)
        self.quantidade = quantidade


navio_1x2 = Navio([["X", "X"]], 3)
navio_2x1 = Navio([ ["X"], 
                    ["X"]], 3)
navio_3x1 = Navio([ ["X"], 
                    ["X"], 
                    ["X"]], 2)
navio_4x1 = Navio([ ["X"], 
                    ["X"], 
                    ["X"],
                    ["X"]], 1)
navio_2x2 = Navio([ ["X", "X"], 
                    ["X", "X"]], 1)
navio_T = Navio([  ["X", "X", "X"], 
                        ["X"], 
                        ["X"],
                        ["X"]], 1)
navio_L = Navio([   ["X"], 
                    ["X"], 
                    ["X"],
                    ["X"], ["X"]], 1)

