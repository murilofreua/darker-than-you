label capitulo4:

    play sound "audio/Sound effects/Objetos/Sinos_tocando_vento_batendo_passaros_fundo.mp3" volume 0.045

    scene quarto-helena with fade
    show dante at Position(xpos=.85, ypos=.75)

    $ renpy.music.play("audio/Capitulos/Capitulo 4 - estranhezas não espantam a alegria.mp3", loop=True)
    $ renpy.music.set_volume(0.02, channel='music')

    narrador "Novamente Dante é acordado pelo soar do sino da igreja."
    
    show dante at Position(xpos=.85, ypos=.75) with dissolve

    dante "Mais um dia abençoado de férias."

    show dante at Position(xpos=.165, ypos=.75):
        xzoom -1
    with move
    
    stop sound
    scene cozinha with fade
    show vitoria at Position(xpos=.75, ypos=.25):
        xzoom -1
    show helena at Position(xpos=.55, ypos=.25):
        xzoom -1
    with dissolve

    show dante at Position(xpos=.165, ypos=.75) with dissolve

    narrador "Os dias que antecedem o festival são intensos e cheios de atividades."
    
    stop sound fadeout 2.0

    play sound "audio/Sound effects/pessoas/Pessoa_bebendo_café_xicará_garganta.mp3" fadein 1.0 loop

    narrador "Dante, Helena e Vitória se voluntariaram para ajudar nos preparativos, e o vilarejo fervilha de excitação."
    narrador "Após terminar suas xicaras, saem apressados em direção a praça."

    stop sound

    show vitoria at Position(xpos=.95, ypos=.25):
        xzoom 1
    with move
    hide vitoria with dissolve
    show helena at Position(xpos=.75, ypos=.25):
        xzoom 1
    with move
    hide helena with dissolve
    show dante at Position(xpos=.75, ypos=.75) with move
    hide dante with dissolve

    scene praca-principal with fade
    play sound "audio/Sound effects/Lugares/Vilarejo_passaros_cachorro_sem_tecnologia.mp3" loop

    narrador "A praça principal se transforma em um colorido cenário festivo, com bandeirolas, barracas de comida e atividades sendo organizadas."
    narrador "Na manhã do primeiro dia de preparativos, Dante se encontra com Padre Iohann na Praça principal."

    show dante at Position(xpos=.15, ypos=.75) with dissolve
    show padre at Position(xpos=.9, ypos=.75) with dissolve
    
    padre "Bom dia, Dante. Estamos muito agradecidos por sua ajuda com o festival."

    show dante at Position(xpos=.15, ypos=.95)
    show padre at Position(xpos=.9, ypos=.95)
    with move

    menu:
        "Feliz em ajudar":
            show dante at Position(xpos=.15, ypos=.75)
            show padre at Position(xpos=.9, ypos=.75)
            with move

            dante "Estou feliz em ajudar, Padre Iohann."
            dante "O que precisa ser feito?"

        "Feliz por ter a festa":
            show dante at Position(xpos=.15, ypos=.75)
            show padre at Position(xpos=.9, ypos=.75)
            with move

            dante "É um prazer estar aqui."
            dante "Mesmo que ajudando com a preparação da festa."
            dante "Tomara que isso deixe todas as comidas mais saborosas."

            show padre preocupado at Position(xpos=.9, ypos=.75) with dissolve

            narrador "O padre não gosta da motivação de Dante, mas seus sermões são guardados para o culto apenas."

            show padre at Position(xpos=.9, ypos=.75) with dissolve

    padre "Temos muitas coisas para organizar."
    padre "As barracas de comida, as decorações da praça, e precisamos preparar a procissão."
    padre "Qualquer coisa que você possa fazer será de grande valor."

    hide padre normal
    hide dante normal
    with dissolve

    stop sound
    $ renpy.music.play("audio/Capitulos/Capitulo 4.mp3", loop=True)
    scene festival-dia

    narrador "Dante, Helena e Vitória se envolvem nas tarefas, conhecendo mais moradores do vilarejo durante o processo."
    narrador "Isabel, Sofia e Seu Pedro estão todos presentes, contribuindo de diferentes maneiras para os preparativos."
    narrador "Dante encontra Isabel ajudando nas barracas de comida."

    show dante at Position(xpos=.5, ypos=.75) with dissolve
    show dante at Position(xpos=.15, ypos=.75) with move
    show isabel feliz at Position(xpos=.5, ypos=.75) with dissolve
    show isabel feliz at Position(xpos=.9, ypos=.75) with move

    dante "Este festival é realmente importante para todos aqui, não é?"

    isabel "Sim, é a alma da nossa cidade. Ele une todos nós e mantém viva a nossa história."

    hide isabel with dissolve

    narrador "Logo em seguida sofia aparece."

    show sofia at Position(xpos=.5, ypos=.75) with dissolve
    show sofia at Position(xpos=.9, ypos=.75) with move

    sofia "Dante, você sabia que o festival começou como uma celebração para agradecer a boa colheita?"
    sofia "Ao longo dos anos, ele evoluiu, mas nunca perdeu seu significado."

    show dante at Position(xpos=.165, ypos=.95)
    show sofia at Position(xpos=.9, ypos=.95)
    with move

    $ livro_lido = historia.get_livro_lido() 

    if livro_lido:
        menu:
            "Não sabia disso.":
                show dante at Position(xpos=.165, ypos=.75)
                show sofia at Position(xpos=.9, ypos=.75)
                with move

                dante "Não sabia disso."
                dante "É fascinante como a história do vilarejo está entrelaçada com o festival."

            "livro de registros.":
                show dante at Position(xpos=.165, ypos=.75)
                show sofia at Position(xpos=.9, ypos=.75)
                with move
                
                dante "Eu li algo sobre no livro de registros da igreja."
                dante "Mas muito obrigado me dizer com mais detalhes!"
    else:
        menu:
            "Não sabia disso.":

                show dante at Position(xpos=.165, ypos=.75)
                show sofia at Position(xpos=.9, ypos=.75)
                with move

                dante "Não sabia disso."
                dante "É fascinante como a história do vilarejo está entrelaçada com o festival."        

    hide sofia normal
    hide dante normal
    with dissolve

    scene festival-noite with fade
    show dante feliz at Position(xpos=.55, ypos=.75)
    show helena feliz at Position(xpos=.4, ypos=.77)
    show vitoria feliz at Position(xpos=.35, ypos=.75)
    with dissolve
    show dante feliz at Position(xpos=.45, ypos=.75)
    show helena feliz at Position(xpos=.3, ypos=.77)
    show vitoria feliz at Position(xpos=.15, ypos=.75)
    with move

    narrador "Finalmente, a noite do festival chega."
    narrador "A praça está iluminada com lanternas coloridas, e a música tradicional enche o ar."
    narrador "As barracas de comida oferecem delícias típicas da região, e as pessoas dançam e celebram com alegria."
    narrador "Dante, Helena e Vitória circulam pelo festival, absorvendo a atmosfera vibrante."
    narrador "Eles experimentam comidas típicas, participam de jogos e danças, e se envolvem na celebração."
    narrador "Dante se sente cada vez mais conectado com a cidade e seus habitantes."
    narrador "Enquanto caminham pela praça, encontram-se com o Padre Iohann."

    show padre at Position(xpos=.7, ypos=.75) with dissolve
    show padre at Position(xpos=.8, ypos=.75) with move
    

    padre "Boa noite, filhos. Espero que estejam aproveitando o festival."

    helena "Está maravilhoso, Padre Iohann. Obrigada por todo o trabalho duro."

    padre "O mérito é de todos nós. Amanhã, temos a procissão e outras atividades importantes. Espero vê-los lá."

    narrador "Dante olha para Helena e Vitória, ambos concordando em ajudar novamente."

    show dante feliz at Position(xpos=.45, ypos=.95)
    show helena feliz at Position(xpos=.3, ypos=.97)
    show vitoria feliz at Position(xpos=.15, ypos=.95)
    show padre at Position(xpos=.85, ypos=.9)
    with move

    menu:
        "Confirmar presença":
            show dante feliz at Position(xpos=.45, ypos=.75)
            show helena feliz at Position(xpos=.3, ypos=.77)
            show vitoria feliz at Position(xpos=.15, ypos=.75)
            show padre at Position(xpos=.85, ypos=.75)
            with move

            dante "Estaremos lá, Padre."

            padre "Que otimo meu cordeirinho"

            $ renpy.music.play("audio/Sound effects/pessoas/Celebração_católica_latim_padre_falando_amem_final.mp3", loop=True)
            scene igreja-dentro
            show padre orando pequeno at Position(xpos=.57, ypos=.64) with dissolve 
            $ renpy.music.set_volume(0.2, channel='music')

            narrador "O grupo participa da procissão"

            pause 10

            narrador "Todos se reencontram após a procissão novamente na praça."
            $ renpy.music.play("audio/Capitulos/Capitulo 4.mp3", loop=True)
            $ renpy.music.set_volume(0.02, channel='music') 


        "não ir a procissão":
            $ historia.luzes()
            $ historia.incrementar_peso(1)
            $ renpy.music.set_volume(0.01, channel='music')

            show dante feliz at Position(xpos=.45, ypos=.75)
            show helena feliz at Position(xpos=.3, ypos=.77)
            show vitoria feliz at Position(xpos=.15, ypos=.75)
            show padre at Position(xpos=.85, ypos=.75)
            with move

            dante "Lamento informar, mas não será possível que eu compareça, Padre."

            hide padre 
            hide vitoria feliz
            with dissolve
            show dante feliz at Position(xpos=.15, ypos=.75)
            show helena feliz at Position(xpos=.85, ypos=.77):
                xzoom -1
            with move

            helena "Nossa, por que Dante?"

            dante "As comidas estão deliciosas mas estou passando mal, volto em pouco tempo."

            show dante feliz at Position(xpos=.4, ypos=.75)
            show helena feliz at Position(xpos=.25, ypos=.77):
                xzoom 1
            with move
            show vitoria feliz at Position(xpos=.15, ypos=.75)
            show padre at Position(xpos=.85, ypos=.75)
            with dissolve

            padre "Fico triste em ouvir isso meu pequeno."

            play sound "audio/Sound effects/Lugares/Natureza_clima_pesado_suspense.mp3" volume .15
            scene igreja-fora-noite with fade
            $ renpy.music.play("audio/Sound effects/pessoas/Celebração_católica_latim_padre_falando_amem_final.mp3", loop=True)
            $ renpy.music.set_volume(0.05, channel='music')

            show dante at Position(xpos = 0.15, ypos = 0.75) with dissolve

            narrador "Enquanto todos estão na procissão, Dante usa esse tempo para investigar melhor os arredores."

            show luzes at Position(xpos=.6, ypos=.85) with dissolve
            show luzes at Position(xpos=.65, ypos=.65) with dissolve
            show luzes at Position(xpos=.7, ypos=.85) with dissolve
            show luzes at Position(xpos=.75, ypos=.65) with dissolve
            show luzes at Position(xpos=.8, ypos=.85) with dissolve
            show luzes at Position(xpos=.85, ypos=.65) with dissolve
            show luzes at Position(xpos=.9, ypos=.85) with dissolve
            hide luzes with dissolve

            narrador "Dante vê novamente as luzes estranhas perto da igreja, similares a velas vermelhas."

            show dante at Position(xpos = 0.55, ypos = 0.75) with move

            narrador "Ele tenta investigar, mas elas desaparecem antes que ele possa se aproximar."
            narrador "A sensação de que algo está fora do comum continua a perturbá-lo, mas ele decide manter suas preocupações para si por enquanto e retorna ao festival."

            hide dante with dissolve

            narrador "Todos se reencontram, após a procissão, novamente na praça."
            $ renpy.music.play("audio/Capitulos/Capitulo 4.mp3", loop=True)
            $ renpy.music.set_volume(0.02, channel='music')            

    stop sound
    scene festival-noite with fade

    show dante feliz at Position(xpos=.68, ypos=.225):
        xzoom -1
    show helena feliz at Position(xpos=.35, ypos=.77)
    show vitoria feliz at Position(xpos=.15, ypos=.75)
    with move

    narrador "Enquanto os três amigos conversam sobre a festa, Rocha, o policial, aproxima-se."
    show dante at Position(xpos=.35, ypos=.21):
        xzoom 1
    show helena feliz at Position(xpos=.3, ypos=.77)
    show vitoria feliz at Position(xpos=.15, ypos=.75)
    with move
    show rocha at Position(xpos = 0.85, ypos = 0.75) with dissolve

    rocha "Boa noite, pessoal. Aproveitando o festival?"

    vitoria "Sim, Rocha. Está tudo incrível."

    rocha "Recebi mais relatos de luzes estranhas perto da igreja."
    rocha "Se virem algo, por favor, nos avisem."

    $ luz = historia.get_luzes()
    if luz :
        hide helena feliz
        hide vitoria feliz
        hide rocha
        with dissolve
        show dante preocupado at Position(xpos=.35, ypos=.21) with dissolve

        narrador "Dante sente um arrepio, mas decide não contar o que viu aos presentes."

        show helena feliz at Position(xpos=.3, ypos=.77)
        show vitoria feliz at Position(xpos=.15, ypos=.75)
        show rocha at Position(xpos = 0.85, ypos = 0.75)
        show dante at Position(xpos=.35, ypos=.21)
        with dissolve

    dante "Claro, Rocha. Manteremos os olhos abertos."

    hide rocha with dissolve

    narrador "Após brincarem e comerem de tudo, os três amigos decidem ir para casa descansar."
    
    hide helena normal
    hide vitoria normal
    hide dante normal
    with dissolve

    scene quarto-helena-noite
    
    show dante at Position(xpos=.15, ypos=.75) with dissolve
    show dante at Position(xpos=.85, ypos=.75) with move
    show helena at Position(xpos=.15, ypos=.75) with dissolve
    show helena at Position(xpos=.35, ypos=.75) with move

    helena "Boa noite Dante, até amanhã, estarei no quarto ao lado."

    show dante at Position(xpos=.85, ypos=.75):
        xzoom -1
    with move

    dante "Boa noite helena, foi otimo passar o dia com voces."

    show helena at Position(xpos=0, ypos=.75):
        xzoom -1
    with move
    hide helena with dissolve
    
    menu:
        "Dormir":
            dante "zZzZzZzZz"

    $ renpy.music.play("audio/Sound effects/Lugares/Natureza_clima_tensao.mp3", loop=True)
    $ renpy.music.set_volume(0.05, channel='music')
    scene quarto-helena with fade
    show dante at Position(xpos=.85, ypos=.75) with dissolve

    show vitoria triste at Position(xpos=0, ypos=.75) with dissolve
    show vitoria triste at Position(xpos=.3, ypos=.75) with move

    vitoria "Dante! Dante!, não consigo achar a Helena em lugar nenhum."

    show dante preocupado at Position(xpos=.85, ypos=.75):
        xzoom -1
    with dissolve
    show dante preocupado at Position(xpos=.85, ypos=.95)
    show vitoria triste at Position(xpos=.3, ypos=.95)
    with move
    
    menu:
        "levantar rapidamente":
            show vitoria triste at Position(xpos=0, ypos=.95):
                xzoom -1
            with move
            hide vitoria with dissolve
            show dante preocupado at Position(xpos=0, ypos=.95) with move
            hide dante with dissolve

            narrador "Dante grita o nome de Helena pela casa."
            scene cozinha
            show dante preocupado at Position(xpos=.5, ypos=.95) with dissolve
            menu:
                "Chamar pela Helena":
                    show dante  at Position(xpos=.5, ypos=.75) with move
                    
                    dante "Helena?"

                    narrador "sem respostas pela casa."
                    show dante preocupado at Position(xpos=.5, ypos=.95) with move
                    menu:
                        "Chamar fervorosamente pela Helena":
                            show dante preocupado at Position(xpos=.5, ypos=.75) with move
                            dante "Helenaaa!!!"
                            narrador "... ainda sem resposta."

    show dante preocupado at Position(xpos=.85, ypos=.75):
        xzoom -1
    with move
    show vitoria triste at Position(xpos=.15, ypos=.75) with dissolve

    vitoria "Ela pode ter ido a igreja."

    dante "Espero que sim!"

    show dante preocupado at Position(xpos=1., ypos=.75):
        xzoom 1
    with move
    hide dante with dissolve
    show vitoria triste at Position(xpos=1., ypos=.75) with move
    hide vitoria with dissolve

    scene centro
    play sound "audio/Sound effects/Lugares/Natureza_ventania_leve.mp3" volume 0.75 loop

    show dante preocupado at Position(xpos=0, ypos=.75) with dissolve
    show dante preocupado at Position(xpos=.35, ypos=.75) with move
    show vitoria triste at Position(xpos=0, ypos=.75) with dissolve
    show vitoria triste at Position(xpos=.15, ypos=.75) with move

    narrador "Dante e Vitória começam a procurá-la por toda a cidade, perguntando aos moradores se a viram."

    narrador "Eles vão até a igreja, onde encontram Padre Iohann."

    hide dante normal
    hide vitoria normal
    with dissolve

    scene igreja-fora-dia with fade
    play sound "audio/Sound Effects/Objetos/Sinos_tocando_vento_batendo_passaros_fundo.mp3" volume .05
    
    show dante preocupado at Position(xpos=.55, ypos=.75)
    show vitoria triste at Position(xpos=.35, ypos=.75)
    with dissolve

    show dante preocupado at Position(xpos=.35, ypos=.75)
    show vitoria triste at Position(xpos=.15, ypos=.75)
    with move
    
    show padre at Position(xpos=.5, ypos=.75) with dissolve
    show padre at Position(xpos=.85, ypos=.75)
    with move

    show dante preocupado at Position(xpos=.35, ypos=.95)
    show vitoria triste at Position(xpos=.15, ypos=.95)
    show padre at Position(xpos=.85, ypos=.95)
    with move    

    menu:
        "Perguntar para o Padre":
            show dante preocupado at Position(xpos=.35, ypos=.75)
            show vitoria triste at Position(xpos=.15, ypos=.75)
            show padre at Position(xpos=.85, ypos=.75)
            with move
            dante "Padre Iohann, você viu Helena esta manhã?"
    
    show padre preocupado at Position(xpos=.85, ypos=.75) with dissolve

    narrador "O padre pensa por um momento."

    padre "Sim, a vi mais cedo."
    padre "Ela disse que ia ajudar na montagem da procissão da manhã a algumas horas."

    show padre at Position(xpos=.85, ypos=.75) with dissolve

    scene igreja-corredor with fade

    show vitoria triste at Position(xpos=.35, ypos=.75)
    show dante preocupado at Position(xpos=.55, ypos=.75)
    with dissolve

    narrador "Dante e Vitória procuram pela igreja, mas não encontram sinal de Helena."
    narrador "Conforme o dia avança, a preocupação aumenta."

    hide vitoria normal
    hide dante normal
    with dissolve

    play sound "audio/Sound effects/Lugares/Natureza_ventania_leve.mp3" volume 1.0 loop
    scene praca-principal with fade

    show vitoria triste at Position(xpos=.15, tpos=.75)
    show dante preocupado at Position(xpos=.35, tpos=.75)
    with dissolve

    narrador "Eles voltam para a praça, onde encontram Rocha."

    show policial at Position(xpos=.5, ypos=.75) with dissolve
    show policial at Position(xpos=.85, ypos=.75) with move

    vitoria "Rocha, precisamos da sua ajuda. Helena desapareceu."

    narrador "Rocha fica sério imediatamente."

    rocha "Vamos organizar uma busca."

    hide rocha normal
    hide vitoria normal
    hide dante normal
    with dissolve

    scene centro with fade

    show dante preocupado at Position(xpos=.55, ypos=.75)
    show vitoria triste at Position(xpos=.35, ypos=.75)
    with dissolve
    show dante preocupado at Position(xpos=.35, ypos=.75)
    show vitoria triste at Position(xpos=.15, ypos=.75)
    with move

    narrador "A busca se intensifica, Dante e Vitória se sentem cada vez mais desesperados."
    narrador "Eles vasculharam cada canto da cidade, perguntando a todos que encontram."

    vitoria "Helena estava tão animada com o festival."

    show dante preocupado at Position(xpos=.85, ypos=.75) with move
    show dante preocupado at Position(xpos=.85, ypos=.75):
        xzoom -1
    with dissolve

    vitoria "Ela não desapareceria assim."

    show dante preocupado at Position(xpos=.85, ypos=.95)
    show vitoria triste at Position(xpos=.15, ypos=.95)
    with move

    menu:
        "Confirmar":
            show vitoria triste at Position(xpos=.15, ypos=.75)
            show dante preocupado at Position(xpos=.85, ypos=.75)
            with move
            
            dante "Eu sei. Isso não faz sentido."

            show dante preocupado at Position(xpos=.35, ypos=.75):
                xzoom 1
            with move

            show padre at Position(xpos=.85, ypos=.75) with dissolve

            padre "Precisamos manter a fé e continuar procurando."
            padre "Avé maria, cheia de graça, o senhor esteja convosco ..."

            narrador "Padre Iohann dispara para acalmar os cordeirinhos"

        "Discordar":
            $ historia.incrementar_peso(1)

            show vitoria triste at Position(xpos=.15, ypos=.75)
            show dante preocupado at Position(xpos=.85, ypos=.75)
            with move

            dante "A Helena já fez isso antes?"

            show dante preocupado at Position(xpos=.35, ypos=.75):
                xzoom 1
            with move

            show padre at Position(xpos=.85, ypos=.75) with dissolve
            
            padre "Precisamos manter a fé e continuar procurando."
            padre "Avé maria, cheia de graça, o senhor esteja convosco ..."

            show dante preocupado at Position(xpos=.35, ypos=.75) with dissolve

            narrador "Padre Iohann tenta instaurar calma aos cordeirinhos, mas Dante percebe que ele está suando frio."

    hide padre with dissolve
    hide vitoria normal
    hide dante normal
    with dissolve

    scene festival-noite with fade
    $ renpy.music.set_volume(0.075, channel="music")
    play sound "audio/Capitulos/Capitulo 4 - estranhezas não espantam a alegria.mp3" volume 0.005 loop

    narrador "A noite cai e Helena ainda não foi encontrada."
    narrador "A atmosfera do festival muda, tornando-se mais tensa e preocupada."
    narrador "Dante, Vitória e os outros se reúnem, discutindo os próximos passos."

    show pedro at Position(xpos=.1, ypos=.1):
        xzoom -1
    show dante preocupado at Position(xpos=.45, ypos=.75)
    show vitoria triste at Position(xpos=.15, ypos=.75)
    show sofia preocupado at Position(xpos=.3, ypos=.75)
    with dissolve

    dante "Ela não pode ter ido longe. Alguém deve ter visto algo."

    show policial at Position(xpos=.85, ypos=.75) with dissolve

    rocha "Vamos continuar a busca pela manhã. Precisamos de mais luz."
    rocha "Dispersem e vão descansar gente."


    stop sound
    scene quarto-helena-noite
    play sound "audio/Sound effects/Lugares/Natureza_ventania_leve.mp3" volume 1.0 loop
    show dante at Position(xpos=.85, ypos=.75) with dissolve

    narrador "Naquela noite, Dante tem um sonho estranho."

    $ renpy.music.set_volume(0.075, channel='music')
    scene igreja-fora-noite with fade
    play sound "audio/Sound effects/Lugares/Natureza_ventania_leve.mp3" volume 3.0 loop

    show helena triste at Position(xpos=.5, ypos=.75) with dissolve

    narrador "Ele vê Helena perto da igreja, cercada pelas mesmas luzes misteriosas que ele viu antes."
    
    show luzes at Position(xpos=.4, ypos=.4) with dissolve
    show luzes at Position(xpos=.6, ypos=.8) with dissolve
    show luzes at Position(xpos=.2, ypos=.8) with dissolve
    show luzes at Position(xpos=.4, ypos=.4) with dissolve
    show luzes at Position(xpos=.6, ypos=.8) with dissolve
    show luzes at Position(xpos=.2, ypos=.8) with dissolve
    hide luzes with dissolve

    scene quarto-helena-noite with fade
    show dante preocupado at Position(xpos=.85, ypos=.75)

    play sound "audio/Sound effects/Lugares/Natureza_ventania_leve.mp3" volume 1.0 loop

    narrador "Dante acorda suando frio, decidido a ir atrás de sua amiga."

    show dante preocupado at Position(xpos=.85, ypos=.75):
        xzoom -1
    with dissolve

    menu:
        "Ir para Igreja":
            dante "Eu preciso ir até a igreja."

            show dante preocupado at Position(xpos=.15, ypos=.75) with move
            hide dante preocupado with dissolve

    narrador "Diz Dante para si mesmo, saindo silenciosamente de casa."

    scene igreja-dentro-noite
    $ renpy.music.set_volume(0.1, channel='music')
    show dante preocupado at Position(xpos=.165, ypos=.75)
    show icaro sentado at Position(xpos=.85, ypos=.75)
    with dissolve

    narrador "Na igreja, ele encontra Ícaro, o jovem seminarista, lendo proximo ao quarto do padre."

    icaro "Dante, o que está fazendo aqui tão tarde?"

    show icaro at Position(xpos=.75, ypos=.75) with move
    show dante at Position(xpos=.25, ypos=.95)
    show icaro at Position(xpos=.75, ypos=.95)
    with move

    menu:
        "Contar sobre o sonho":
            show dante at Position(xpos=.25, ypos=.75)
            show icaro at Position(xpos=.75, ypos=.75)
            with move

            dante "Eu tive um sonho... vi Helena aqui, envolta em luzes, tem que ter um significado."

            icaro "Entendo, mas isso não justifica estar aqui sozinho."
            icaro "Você deixou Vitória sozinha?"
            icaro "Vamos investigar juntos amanhã, mas por hora, você precisa voltar para casa de Helena."

        "Perguntar sobre a leitura":
            
            $ historia.incrementar_peso(1)
            show dante preocupado at Position(xpos=.25, ypos=.75)
            show icaro at Position(xpos=.75, ypos=.75)
            with move

            dante "Acabou que eu perdi o sono e estou andando pela cidade enquanto o sono volta."
            dante "Por que você está lendo aqui tão tarde nesse bréu."

            icaro "Entendo, nós ouvimos coisas estranhas e viemos ver como esta o padre."
            icaro "Augusto está lá dentro conferindo se o padre precisa de algo."
            icaro "Caso queira voltar aqui amanhã, está convidado. Mas por hora, você precisa descansar."

    dante "Sim, amanhã conversaremos melhor."
    dante "Boa noite."

    hide dante with dissolve
    scene quarto-helena-noite with fade
    show dante at Position(xpos=.85, ypos=.75) with dissolve

    narrador "Dante se despede dos seminaristas e, em casa, tem uma péssima noite de sono, ainda preocupado com Helena."

    return