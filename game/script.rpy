define a = Character("Augusto")
define d = Character("Dante")
define h = Character("Helena")
define ic = Character("Ícaro")
define isa = Character("Isabel")
define r = Character("Rocha")
define s = Character("Sofia")
define v = Character("Vitória")

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

label start:

    # Capítulo 1
    
    scene quarto-dante

    show dante normal at truecenter

    d "Ócio, finalmente!"

    show dante normal at Position(xpos = 0.3, ypos = 0.5)

    show helena normal at Position(xpos = 0.7, ypos = 0.75)

    h "Olá, Dante?"

    h "Oi, Dante! Sou a Helena, lembra de mim? Achei seu número por acaso na internet. Como estão as coisas?"

    d "Helena?! Quanto tempo! Claro que me lembro de você. Faz tempo mesmo. Estou muito bem, e com você?"

    d "Acabei de entrar de férias, mas confesso que não ando fazendo muita coisa. Por onde você anda?"

    h "Já faz alguns anos vim morar num vilarejo com meus pais. Eles decidiram largar a vida corrida da capital. Eu amo morar aqui, é lindo! Vou te mandar umas fotos."

    d "Uau! Esse lugar é fera demais! Me lembra um pouco aquela viagem que fizemos para Goiás na época de escola, lembra?"

    h "Sim, realmente. Aqui é extremamente calmo e as pessoas são maravilhosas!"
    
    h "Já que está de férias, não gostaria de prestar uma visita? Juro por Deus que você vai amar!"

    return