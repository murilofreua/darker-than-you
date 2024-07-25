label capitulo1:
    # Capítulo 1
    
    scene quarto-dante

    $ renpy.music.play("audio/Capitulos/Capitulo 1 - Parece um sonho merecido.mp3", loop=True)
    $ renpy.music.set_volume(0.25, channel='music')

    indefinido "Amanhecer do 1° dia"

    show dante normal at truecenter with dissolve

    dante "Ócio..."

    play sound "audio/Sound effects/Objetos/Toque_celular_nokia_3310.mp3" volume 0.5 loop
    
    dante "Finalmente!"

    telefoneDoDante "*tocando"

    dante "Inferno"

    show dante normal at Position(xpos = 0.15, ypos = 0.8) with move

    menu:
        "Atender":
            stop sound

    show dante normal at Position(xpos = 0.5, ypos = 0.5) with move

    dante "Alô?"

    vozFeminina "Olá, Dante?"  

    dante "Sim, quem fala?"

    show dante normal at Position(xpos = 0.15, ypos = 0.5) with move

    show helena normal at Position(xpos = 0.7, ypos = 0.25):
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

    narrador "Dante Olha a notificação e visualiza as fotos rapidamente"

    # adicionar fotos do local, pode ser um celular na galeria ou umas 4 fotos daquelas de camera de revelação instantânea sobrepostas.

    dante " Uau! Esse lugar é fera demais!"
    dante "Até me lembra um pouco aquela viagem que fizemos para Goiás na época de escola, lembra?"

    helena "Sim, realmente. Aqui é extremamente calmo e as pessoas são maravilhosas "
    helena "Já que está de férias, não gostaria de prestar uma visita?"
    helena "Juro por Deus que você vai amar!"

    dante  "Sim, claro!"

    hide helena normal with dissolve

    show dante normal at Position(xpos = 0.5, ypos = 0.5) with move

    narrador "Animado por relembrar alguns de seus bons momentos com Helena, após horas de conversas, Dante decide visitar o vilarejo."
    narrador "Após colocar seu tênis de corrida na mala, sai preparado para conhecer o belo vilarejo de Encosta da Saudade e rever Helena."
    
    hide dante normal with fade

    return