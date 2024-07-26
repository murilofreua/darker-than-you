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

# Personagens neutros

image augusto normal = im.Scale("neutros/augusto.png", 575, 540)
image dante normal = im.Scale("neutros/dante.png", 645, 590)
image helena normal = im.Scale("neutros/helena.png", 575, 540)
image icaro normal = im.Scale("neutros/icaro.png", 575, 540)
image isabel normal = im.Scale("neutros/isabel.png", 680, 420)
image rocha normal = im.Scale("neutros/rocha.png", 680, 540)
image sofia normal = im.Scale("neutros/sofia.png", 635, 440)
image vitoria normal = im.Scale("neutros/vitoria.png", 575, 540)
image padre normal = im.Scale("neutros/padre.png", 745, 740)
image pedro normal = im.Scale("neutros/pedro.png", 780, 620)

# Personagens felizes

# Personagens tristes

# Ⱡคⵡ𝖽αŧℯ

# Variáveis

init python:

    config.rollback_enabled = True #false #setar como false quando for gerar o .exe

    class Historia:
        def __init__(self):
            self.maca = False
            self.livro = False
            self.peso_bom = 0

        def maca_guardada(self):
            self.maca = True

        def livro_lido(self):
            self.livro = True

        def incrementar_peso(self, valor):
            self.peso_bom += valor

        def get_peso_bom(self):
            return self.peso_bom
    
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
    
return