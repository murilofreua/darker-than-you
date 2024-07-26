label capitulo1:
    # Capítulo 1
    
    scene quarto-dante

    $ renpy.music.play("audio/Capitulos/Capitulo 1 - Parece um sonho merecido.mp3", loop=True)
    $ renpy.music.set_volume(.25, channel='music')

    indefinido "..."

    show dante normal at Position(xpos=.5, ypos=.75) with dissolve

    dante "Ócio..."

    dante "Finalmente!"

    play sound "audio/Sound effects/Objetos/Toque_celular_nokia_3310.mp3" volume .5 loop

    telefoneDoDante "*tocando"

    show dante normal at Position(xpos=.35, ypos=.75) with move 
    show smartphone at Position(xpos=.55, ypos=.8) with dissolve

    dante "Inferno!"

    show dante normal at Position(xpos=.35, ypos=.95)
    show smartphone at Position(xpos=.55, ypos=.95) with move

    menu:
        "Atender":
            stop sound fadeout 1.5

    show smartphone at Position(xpos=.85, ypos=.85)
    show dante normal at Position(xpos=.25, ypos=.75)
    with move

    dante "Alô?"

    vozFeminina "Olá, Dante?"  

    dante "Sim, quem fala?"

    show dante normal at Position(xpos=.15, ypos=.75) with move
    hide smartphone
    show helena normal at Position(xpos=.7, ypos=.25):
        xzoom -1
    with dissolve


    vozFeminina " Oi, Dante! Sou a Helena, lembra de mim? Achei seu número por acaso na internet. Tá sumido uai! Como estão as coisas?"

    dante "He... Helena?"   
    dante "Helena?! Quanto tempo! Claro que me lembro de você. Faz tempo mesmo."
    dante "Estou muito bem, e com você? Acabei de entrar de férias, mas confesso que não ando fazendo muita coisa."
    dante "Por onde você anda?"

    helena "Já faz alguns anos que vim morar num vilarejo pacáto com meus pais."
    helena "Eles decidiram largar a vida da capital!"
    helena "Eu amo morar aqui, é lindo! Acabei de te mandar umas fotos, dá uma olhada!"

    show celular at Position(xpos=.42, ypos=.89)

    dante " Uau! Esse lugar é fera demais!"
    dante "Até me lembra um pouco aquela viagem que fizemos para Goiás na época de escola, lembra?"

    helena "Sim, realmente. Aqui é extremamente calmo e as pessoas são maravilhosas "
    helena "Já que está de férias, não gostaria de prestar uma visita?"
    helena "Juro por Deus que você vai amar!"

    dante  "Sim, claro!"

    hide helena normal with dissolve
    hide celular with dissolve

    show dante normal at Position(xpos=.5, ypos=.75) with move

    narrador "Animado por relembrar alguns de seus bons momentos com Helena, após horas de conversas, Dante decide visitar o vilarejo."
    narrador "Após colocar seu tênis de corrida na mala, sai preparado para conhecer o belo vilarejo de Encosta da Saudade e rever Helena."



    hide dante normal with fade

    return