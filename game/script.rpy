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

# Personagens neutros

image augusto normal = im.Scale("augusto.png", 575, 540)
image dante normal = im.Scale("dante.png", 575, 540)
image helena normal = im.Scale("helena.png", 575, 540)
image icaro normal = im.Scale("icaro.png", 575, 540)
image isabel normal = im.Scale("isabel.png", 610, 540)
image rocha normal = im.Scale("rocha.png", 680, 540)
image sofia normal = im.Scale("sofia.png", 635, 540)
image vitoria normal = im.Scale("vitoria.png", 575, 540)

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
    
    # Capítulo 1

    
    scene quarto-dante

    indefinido "..."

    show dante normal at truecenter with dissolve

    dante "Ócio..."

    dante "Finalmente!"

    play sound "audio/ringtone.mp3"

    telefoneDoDante "*tocando"

    dante "Inferno"

    call entrarMenuDante

    menu:
        "Atender":
            stop sound

    call retomarMenuDante
    #hide dante normal  

    #show dante normal at left:
    #    yalign 0.5
    #    xalign 0.1
    

    dante "Alô?"

    vozFeminina "Olá, Dante?"  

    dante "Sim, quem fala?"   

    show helena normal at Position(xpos = 0.7, ypos = 0.75) with dissolve

    vozFeminina " Oi, Dante! Sou a Helena, lembra de mim? Achei seu número por acaso na internet. Tá sumido uai! Como estão as coisas?"

    dante "He... Helena?"   

    dante "Helena?! Quanto tempo! Claro que me lembro de você. Faz tempo mesmo. Estou muito bem, e com você? Acabei de entrar de férias, mas confesso que não ando fazendo muita coisa. Por onde você anda?"  

    helena "Já faz alguns anos vim morar num vilarejo com meus pais. Eles decidiram largar a vida da capital!"

    helena "Eu amo morar aqui, é lindo! Acabei de te mandar umas fotos, dá uma olhada!"

    dante "*Olha a notificação e visualiza as fotos rapidamente"

    dante " Uau! Esse lugar é fera demais! Me lembra um pouco aquela viagem que fizemos para Goiás na época de escola, lembra?"

    helena "Sim, realmente. Aqui é extremamente calmo e as pessoas são maravilhosas..."

    helena "Já que está de férias, não gostaria de vir me visitar?"

    hide helena normal 
    
    call entrarMenuDante

    menu:
        "Sim, claro!":
            call retomarMenuDante
            show helena normal at Position(xpos = 0.7, ypos = 0.75) with dissolve
            helena "Ótimo, aqui tem muios lugares bonitos, qual deles você quer ver primeiro?"
            dante "*Checa a notificação e olha novamente as fotos para escolher"
            hide helena normal 
            call entrarMenuDante
            menu:
                
                "Igreja":
                    call retomarMenuDante
                    $ historia.incr_peso_ruim()
                    show helena normal at Position(xpos = 0.7, ypos = 0.75) with dissolve
                    helena "Beleza, iremos visitar a Grande Igreja primeiro!"

                "Padaria":
                    call retomarMenuDante
                    $ historia.incr_peso_bom()
                    show helena normal at Position(xpos = 0.7, ypos = 0.75) with dissolve
                    helena "Beleza, iremos visitar a deliciosa Padaria primeiro!"

                "Entrada da Floresta":
                    call retomarMenuDante
                    $ historia.incr_peso_normal()
                    show helena normal at Position(xpos = 0.7, ypos = 0.75) with dissolve
                    helena "Beleza, iremos visitar a aconchegante Floresta primeiro!"


        "Não sei, é muito longe?":
            call retomarMenuDante
            show helena normal at Position(xpos = 0.7, ypos = 0.75) with dissolve
            helena "Tem um ônibus direto daí para o vilarejo! Sai todo domingo"
            dante "Ahh sim! Então posso ir tranquilamente"
            helena "Todo domingo tem a missa aqui e catedral é muito linda!"
            dante "Então vou querer ver a ver primeiro!"
            helena "Combinado!"  
            
  
    return



label entrarMenuDante:

    hide dante normal
    
    show dante normal:
        yalign 0.95
        xalign 0.5
    return    

label retomarMenuDante:

    hide dante normal  

    show dante normal at left:
        yalign 0.5
        xalign 0.1
    return    