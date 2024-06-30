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
                    show helena normal at Position(xpos = 0.7, ypos = 0.75) with dissolve
                    helena "Beleza, iremos visitar a Grande Igreja primeiro!"

                "Padaria":
                    call retomarMenuDante
                    show helena normal at Position(xpos = 0.7, ypos = 0.75) with dissolve
                    helena "Beleza, iremos visitar a deliciosa Padaria primeiro!"

                "Entrada da Floresta":
                    call retomarMenuDante
                    show helena normal at Position(xpos = 0.7, ypos = 0.75) with dissolve
                    helena "Beleza, iremos visitar a aconchegante Floresta primeiro!"


        "Não sei, é muito longe?":
            call retomarMenuDante
            show helena normal at Position(xpos = 0.7, ypos = 0.75) with dissolve
            helena "Tem um ônibus direto daí para o vilarejo! Sai todo domingo"
            dante "Ahh sim! Então posso ir tranquilamente"
            helena "Todo domingo tem a missa aqui e catedral é muito linda! Quando chegar aqui eu te mostro ela"
            dante "Tudo bem, combinado!"  
            
  
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