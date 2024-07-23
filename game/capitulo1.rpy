label capitulo1:
    # Capítulo 1
    
    scene quarto-dante

    $ renpy.music.play("audio/Capitulo I.mp3", loop=True)
    $ renpy.music.set_volume(0.4, channel='music')

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

    helena "Sim, realmente. Aqui é extremamente calmo e as pessoas são maravilhosas "

    helena "Já que está de férias, não gostaria de prestar uma visita? Juro por Deus que você vai amar!"

    dante  "Sim, claro!"

    hide dante normalmente
    hide helena normal 
    with fade

    narrador "Animado por relembrar alguns de seus bons momentos com Helena, em horas de conversas, Dante decide visitar o vilarejo. Coloca seu tênis de corrida na mala e se prepara para conhecer o belo vilarejo de Encosta da Saudade."

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