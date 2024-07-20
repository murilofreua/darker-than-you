define augusto = Character("Augusto")
define dante = Character("Dante")
define helena = Character("Helena")
define icaro = Character("Ícaro")
define isabel = Character("Isabel")
define rocha = Character("Rocha")
define sofia = Character("Sofia")
define vitoria = Character("Vitória")
define indefinido = Character("")
define telefoneDoDante = Character("Telefone do Dante")
define vozFeminina = Character("Voz feminina")
define narrador = Character("Narrador")

# Personagens neutros

image augusto normal = im.Scale("neutros/augusto.png", 575, 540)
image dante normal = im.Scale("neutros/dante.png", 575, 540)
image helena normal = im.Scale("neutros/helena.png", 575, 540)
image icaro normal = im.Scale("neutros/icaro.png", 575, 540)
image isabel normal = im.Scale("neutros/isabel.png", 610, 540)
image rocha normal = im.Scale("neutros/rocha.png", 680, 540)
image sofia normal = im.Scale("neutros/sofia.png", 635, 540)
image vitoria normal = im.Scale("neutros/vitoria.png", 575, 540)

# Personagens felizes

# Personagens tristes

# Ⱡคⵡ𝖽αŧℯ

# Variáveis

init python:

    class Caminho:
        def __init__(self,natureza):
            self.natureza = natureza
            self.pesos_proximo_caminho = {
                "bom" : 0,
                "normal" : 0,
                "ruim" : 0
            }
            if( not (natureza in self.pesos_proximo_caminho) ):
                raise  ValueError("A naturez tem que estar no dicionario")
                

        def chave_maior_peso_prox_caminho(self):
            return max(self.pesos_proximo_caminho, key=self.pesos_proximo_caminho.get)            
            

    class Ato:
        def __init__(self, caminhos,nome):
            self.caminhos = caminhos
            self.nome = nome
            self.caminho_atual = caminhos[0]
        
        def set_caminho_atual(self,natureza):
            for c in self.caminhos:
                if(c.natureza==natureza):
                    self.caminho_atual = c


    class Historia:
        def __init__(self):
            ato1 = Ato([Caminho("ruim"),Caminho("normal"),Caminho("bom")],"Casa do Protagonista")
            ato2 = Ato([Caminho("ruim"),Caminho("normal"),Caminho("bom")],"Conhecendo o Vilarejo")
            ato3 = Ato([Caminho("ruim"),Caminho("normal"),Caminho("bom")],"Assasinato!")
            self.atos = [ato1,ato2,ato3]
            self.ato_atual = self.atos[0]
        
        def passar_ato(self):
            indice_ato_atual = self.atos.index(self.ato_atual)
            chave_proximo_caminho = self.atos[indice_ato_atual].caminho_atual.chave_maior_peso_prox_caminho()
            if indice_ato_atual + 1 < len(self.atos):
                self.ato_atual = self.atos[indice_ato_atual + 1]
                indice_ato_atual+=1
            else:
                raise ValueError("Você já está no último ato")
            self.ato_atual.set_caminho_atual(chave_proximo_caminho)
            return self.ato_atual     
        
        def incr_peso_bom(self):
            self.ato_atual.caminho_atual.pesos_proximo_caminho["bom"]+=1

        def incr_peso_normal(self):
            self.ato_atual.caminho_atual.pesos_proximo_caminho["normal"]+=1

        def incr_peso_ruim(self):
            self.ato_atual.caminho_atual.pesos_proximo_caminho["ruim"]+=1

        def get_natureza_caminho_atual(self):
            return self.ato_atual.caminho_atual.natureza
    
define historia = Historia()


label start:

    #call capitulo1

    call capitulo2

    call capitulo3
    
return