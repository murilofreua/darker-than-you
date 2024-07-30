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
define pedro = Character("Pedro")
define padre = Character("Padre Iohann")

# Personagens realizando ações

image augusto lendo = im.Scale("personagens/ações/augusto-lendo.png", 575, 540)
image helena sorridente = im.Scale("personagens/ações/helena-roupa-festa.png", 575, 540)
image icaro sentado = im.Scale("personagens/ações/icaro-sentado.png", 575, 540)
image padre orando = im.Scale("personagens/ações/padre-orando.png", 745, 700)
image padre orando pequeno = im.Scale("personagens/ações/padre-orando.png", 225, 170)
image policial = im.Scale("personagens/ações/rocha-uniforme.png", 645, 540)

# Personagens felizes

image dante feliz = im.Scale("personagens/felizes/dante-feliz.png", 625, 570)
image helena feliz = im.Scale("personagens/felizes/helena-feliz.png", 575, 540)
image isabel feliz = im.Scale("personagens/felizes/isabel-feliz.png", 735, 440)
image pedro feliz = im.Scale("personagens/felizes/pedro-feliz.png", 780, 620)
image rocha feliz = im.Scale("personagens/felizes/rocha-feliz.png", 575, 540)
image sofia feliz = im.Scale("personagens/felizes/sofia-feliz.png", 635, 440)
image vitoria feliz = im.Scale("personagens/felizes/vitória-feliz.png", 575, 540)

# Personagens neutros

image dante = im.Scale("personagens/neutros/dante-neutro.png", 645, 590)
image helena = im.Scale("personagens/neutros/helena-neutro.png", 575, 540)
image icaro = im.Scale("personagens/neutros/icaro-neutro.png", 575, 540)
image padre = im.Scale("personagens/neutros/padre-neutro.png", 745, 700)
image pedro = im.Scale("personagens/neutros/pedro-neutro.png", 780, 620)
image rocha = im.Scale("personagens/neutros/rocha-neutro.png", 680, 540)
image sofia = im.Scale("personagens/neutros/sofia-neutro.png", 635, 440)
image vitoria = im.Scale("personagens/neutros/vitória-neutro.png", 575, 540)

# Personagens preocupados

image dante preocupado = im.Scale("personagens/preocupados/dante-preocupado.png", 645, 590)
image helena preocupado = im.Scale("personagens/preocupados/helena-preocupado.png", 575, 540)
image icaro preocupado = im.Scale("personagens/preocupados/icaro-preocupado.png", 575, 540)
image padre preocupado = im.Scale("personagens/preocupados/padre-preocupado.png", 745, 700)
image sofia preocupado = im.Scale("personagens/preocupados/sofia-preocupado.png", 635, 440)
image vitoria preocupado = im.Scale("personagens/preocupados/vitória-preocupado.png", 575, 540)

# Personagens tristes

image helena triste = im.Scale("personagens/tristes/helena-triste.png", 575, 540)
image rocha triste = im.Scale("personagens/tristes/rocha-triste.png", 680, 540)
image vitoria triste = im.Scale("personagens/tristes/vitória-triste.png", 575, 540)

# Personagens dormindo

image dante dormindo = im.Scale("personagens/dormindo/dante-dormindo.png", 645, 590)
image helena dormindo = im.Scale("personagens/dormindo/helena-dormindo.png", 575, 540)

# Variáveis

init python:

    config.rollback_enabled = True 

    class Historia:
        def __init__(self):
            self.maca = False
            self.livro = False
            self.peso_bom = 0
            self.luz = False

        def maca_guardada(self):
            self.maca = True

        def get_maca_guardada(self):
            return self.maca

        def livro_lido(self):
            self.livro = True

        def get_livro_lido(self):
            return self.livro

        def incrementar_peso(self, valor):
            self.peso_bom += valor

        def get_peso_bom(self):
            return self.peso_bom

        def luzes(self):
            self.luz = True

        def get_luzes(self):
            return self.luzes
    
define historia = Historia()

default persistent.finalOtimo = False
default persistent.finalBom = False
default persistent.finalMedio = False
default persistent.finalRuim = False

label start:

    call capitulo1

    call capitulo2

    call capitulo3
    
    call capitulo4

    call capitulo5

    call capitulo6

    call capitulo7

    # call finalOtimo

    # call finalBom

    # call finalMedio

    # call finalRuim

    call creditos
    
return