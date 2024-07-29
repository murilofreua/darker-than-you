label capitulo2:

    $ renpy.music.play("audio/Capitulos/Capitulo 2 - uma vista calorosa.mp3", loop=True)
    $ renpy.music.set_volume(.10, channel='music')

    scene centro

    narrador "Dante sentia a sensação de voltar para o passado."
    narrador "A paisagem verdejante e as casas simples no estilo barroco europeu lembravam sua infância numa pequena cidade do interior de Goiás."
    narrador "Ao descer do ônibus e olhar em volta, ficou impressionado pela beleza da cidade mineira."
    narrador "O sol acabará de raiar, pintando o céu de tons claros e fazendo com que as casas da vila parecessem ainda mais charmosas."

    show helena feliz at Position(xpos=.3, ypos=.77) with dissolve
    show vitoria feliz at Position(xpos=.45, ypos=.25):
        xzoom -1
    with dissolve


    narrador "Helena estava radiante em um vestido azul, e lhe aguardava com um grande sorriso, acompanhada por uma amiga, que fora momentaneamente ofuscada pelo brilho de Helena."

    show vitoria feliz at Position(xpos=1., y=.75) with move
    hide vitoria with dissolve
    show helena feliz at Position(xpos=.86, ypos=.77) with move
    show helena feliz at Position(xpos=.86, ypos=.77):
        xzoom -1
    with dissolve

    helena "Dante!"
    helena "Tão bom te ver!"

    show helena feliz at Position(xpos=.86, ypos=.97) with move
    show dante feliz at Position(xpos = .165, ypos=.95) with dissolve

    menu: 
        "Abraçar":
            show helena feliz at Position(xpos=.6, ypos=.77)
            show dante feliz at Position(xpos=.4, ypos=.75)
            with move

            dante "Olá, Helena! Você mudou muito desde a última vez que nos vimos!"

            dante "Está estonteantemente linda!"

            show helena feliz at Position(xpos=.86, ypos=.77)
            show dante feliz at Position(xpos = .165, ypos=.75)
            with move

            narrador "Helena se distancia por ter ficado embasbacada com o elogio durante o abraço enquanto Vitória se apresenta."
    
    hide helena feliz with dissolve

    show vitoria feliz at Position(xpos = .7, ypos = .25):
        xzoom -1
    with dissolve

    vitoria "Olá, Dante! Sou a Vitória, muito prazer."

    show vitoria feliz at Position(xpos=.7, ypos=.45)
    show dante feliz at Position(xpos=.165, ypos=.95)
    with move

    menu:
        "Cumprimentar cordialmente":
            show vitoria feliz at Position(xpos=.6, ypos=.25)
            show dante feliz at Position(xpos=.3, ypos=.75)
            with move

            dante "Prazer Vitória, como é bom te conhecer!"

            show vitoria feliz at Position(xpos=.7, ypos=.25)
            show dante feliz at Position(xpos = .165, ypos=.75)
            with move
    
    show helena feliz at Position(xpos=.55,ypos=.77) with dissolve

    helena "Vamos começar nosso passeio amigos!"

    show vitoria feliz at Position(xpos=.6, ypos=.25)
    show dante feliz at Position(xpos=.35, ypos=.75)
    with move

    narrador "Disse Helena antes de pegar ambos pelos braços e sair correndo sem rumo para conhecer a cidade."

    hide helena feliz with dissolve
    hide dante normal
    hide vitoria normal
    with dissolve

    scene igreja-fora-dia

    play sound "audio/Sound effects/Objetos/Sinos_tocando_vento_batendo_passaros_fundo.mp3" volume .2 fadein 2.0

    narrador "O grupo passou na porta da Igreja da Misericórdia, uma bela igreja antiga."

    narrador "Apesar de Dante de não ser muito religioso..."
    narrador "O garoto sentiu uma sensação estranha enquanto olhava para a igreja, como se alguma energia misteriosa o atraísse."

    show dante preocupado at Position(xpos = .5, ypos=.75) with dissolve

    dante "Que bela igreja!"

    show dante feliz at Position(xpos = .165, ypos=.75) with move
    show helena feliz at Position(xpos = .71, ypos = .25):
        xzoom -1
    with dissolve

    helena "É incrível, né?"
    helena "A Igreja é o símbolo deste lugar."
    helena "Meus estudos indicam que seus fundadores vieram da Europa e do México e trouxeram a tradição católica aqui."
    helena "Mas esse não é nosso destino, vamos."

    hide helena feliz
    hide dante normal
    with dissolve

    stop sound fadeout 1.5
    scene praca-principal

    show vitoria feliz at Position(xpos=.15, ypos=.75)
    show helena feliz at Position(xpos=.25, ypos=.77)
    show dante feliz at Position(xpos=.45, ypos=.75)

    narrador "O trio passou em frente a praça da cidade."

    show vitoria feliz at Position(xpos=.75, ypos=.75) 
    show helena feliz at Position(xpos=.86, ypos=.77) 
    show dante feliz at Position(xpos=.95, ypos=.75)
    with move 
    hide vitoria normal
    hide helena feliz
    hide dante normal
    with dissolve

    narrador "Os jovens dão continuidade ao passeio."

    scene padaria-fora
    narrador "Após uma manhã de conversa, os três se dirigiram para a padaria favorita de Vitória, próxima à praça principal da cidade."

    $ renpy.music.play("audio/Sound effects/pessoas/Homem_cantarolar_senior_trabalhando_corte.mp3", loop=True)
    $ renpy.music.set_volume(.5, channel='music')

    narrador "Lá, foram recebidos por Seu Pedro, o padeiro."
    
    show pedro feliz at Position(xpos=.5, ypos=.75) with dissolve

    pedro "Olha quem veio! Helena, você trouxe um visitante especial, não é?"

    show pedro feliz at Position(xpos=.8, ypos=.75) with move

    show helena feliz at Position(xpos=.14,ypos=.75) with dissolve

    helena "Ah, Seu Pedro! Este é o meu amigo Dante. Ele está aqui para passar alguns dias conosco."

    pedro "Ah sim! Bem-vindo ao vilarejo! Eu sou Pedro."

    hide helena feliz with dissolve

    show pedro feliz at Position(xpos=.8, ypos=.95) with move
    show dante feliz at Position(xpos = .165, ypos=.95) with dissolve

    menu: 
        "Apertar a mão de Pedro":

            show dante feliz at Position(xpos=.25, ypos=.75)
            show pedro feliz at Position(xpos=.65, ypos=.75)
            with move

            dante "Obrigado, Seu Pedro. É um prazer conhecer você."

    hide dante with dissolve
    show pedro feliz at Position(xpos=.5, ypos=.75)
    with move

    pedro "O que querem comer? Aposto que estão morrendo de fome..."

    play sound "audio/Sound effects/pessoas/Grupo_misto_rindo.mp3"

    show pedro feliz at Position(xpos=.85, ypos=.75) with move
    show vitoria feliz at Position(xpos=.15, ypos=.75)
    show helena feliz at Position(xpos=.35, ypos=.77)
    with dissolve

    narrador "Mal ele terminara a frase, o padeiro rí em disparate, acompanhado por Helena e Vitória."

    show pedro feliz at Position(xpos=.85, ypos=.95)
    show vitoria feliz at Position(xpos=.15, ypos=.95)
    show helena feliz at Position(xpos=.35, ypos=.97)
    with move

    menu:
        "Sorrir confuso":
            hide vitoria feliz
            hide helena feliz
            with dissolve
            show pedro feliz at Position(xpos=.8, ypos=.75) with move
            show dante feliz at Position(xpos = .165, ypos=.75) with dissolve

            narrador "Dante olhou para Helena e Vitória, ainda rindo, e sorriu confuso."

            show pedro feliz at Position(xpos=.5, ypos=.75) with move

        "Estou com fome":
            $ historia.incrementar_peso(1)
            hide vitoria feliz
            hide helena feliz
            hide pedro feliz
            with dissolve
            show dante preocupado at Position(xpos = .5, ypos=.75) with dissolve

            dante "Eu realmente estou com fome após a viagem, por que as risadas?"

            show dante preocupado at Position(xpos = .165, ypos=.75) with move
            show helena feliz at Position(xpos = .71, ypos = .25):
                xzoom -1
            with dissolve

            helena "Não seja tão careta Dante, o seu Pedro trabalha no cemitério da cidade por isso a graça em morrendo de fome."

            stop sound

            show dante feliz at Position(xpos = .165, ypos=.75) with dissolve

            dante "Nossa, já tinha ouvido falar de padeiro que fazia a função de açogueiro e barbeiro, mas coveiro é a primeira vez." 

            helena "Por isso mesmo, seu Pedro não é uma figura!"

            show pedro feliz at Position(xpos=.5, ypos=.75) with dissolve

            hide helena feliz

    hide dante normal
    with dissolve

    scene padaria-dentro
    stop sound
    show pedro feliz at Position(xpos=.5, ypos=.75) with dissolve

    pedro "Hoje temos pão de queijo fresquinho, broa de milho, e bolos variados."
    pedro "E claro, o café passado na hora, que não pode faltar."

    show pedro feliz at Position(xpos=.85, ypos=.75) with move
    show helena feliz at Position(xpos=.15, ypos=.77) with dissolve

    helena "Parece uma ótima escolha! Vou querer o de sempre, para o Dante experimentar."

    hide pedro normal
    hide helena feliz with dissolve
    $ renpy.music.set_volume(.2, channel='music')
    
    show vitoria feliz at Position(xpos=.35, ypos=.25):
        xzoom -1
    with dissolve 

    vitoria "Dante, você vai adorar o festival!"
    vitoria "É a melhor época do ano aqui: tem música, danças tradicionais, comidas típicas e até bingo!"

    show vitoria feliz at Position(xpos=.7, ypos=.25) with move
    show dante feliz at Position(xpos=.165, ypos=.75) with dissolve

    dante "Sou muito bom no bingo hein!"
    dante "Já estou ansioso, Parece incrível!"

    show helena feliz at Position(xpos=.45, ypos=.27):
        xzoom -1
    with dissolve

    helena "A melhor parte, com certeza, são os doces locais e a música, que possui raizes antigas e ritualísticas destinadas aos espiritos da colheita"
    
    show vitoria preocupado at Position(xpos=.7, ypos=.25) with dissolve

    vitoria "Meu Deus Helena, não começa com suas curiosidades infindáveis!"

    show helena triste at Position(xpos=.45, ypos=.25):
        xzoom 1
    with dissolve

    helena "Amiga! não é para tanto, eu nem falo tanto assim sobre a história da vila."

    show helena triste at Position(xpos=.45, ypos=.25):
        xzoom -1
    with dissolve

    hide dante feliz with dissolve

    show pedro feliz at Position(xpos=.001, ypos=.2):
        xzoom -1
    with dissolve
    
    $ renpy.music.set_volume(.6, channel='music')
    narrador "Logo, Seu Pedro retornou com uma bandeja cheia de delícias"

    pedro "Helena, minha pequena, eu ouvi mais sobre a história da cidade em sua presença que em minha vida toda."

    play sound "audio/Sound effects/pessoas/Grupo_misto_rindo.mp3"
    show vitoria feliz at Position(xpos=.7, ypos=.25) with dissolve
    show helena feliz at Position(xpos=.45, ypos=.27) with dissolve


    narrador "Após a graça com o gosto da amiga os três começaram a comer, rindo e conversando sobre a vida no vilarejo e relembrando histórias de infância."

    hide vitoria feliz
    hide helena feliz
    hide pedro feliz
    with dissolve
    show dante feliz at Position(xpos=.5, ypos=.75) with dissolve

    stop sound

    narrador "O dia chegava a sua metade e Dante sentiu-se mais relaxado e feliz do que em muito tempo."
    narrador "Depois de agradecer calorosamente a Seu Pedro e pagarem a conta, o trio se dirigiu à praça principal."

    hide dante normal
    hide vitoria normal
    with dissolve

    $ renpy.music.play("audio/Sound effects/Lugares/Safe_house_seguro_tranquilo.mp3", loop=True)
    $ renpy.music.set_volume(.15, channel='music')
 
    scene praca-principal with fade

    play sound "audio/Sound effects/Lugares/Vilarejo_passaros_cachorro_sem_tecnologia.mp3" loop
    show helena feliz at Position(xpos=.15, ypos=.77) with dissolve
    show dante feliz at Position(xpos=.35, ypos=.75) with dissolve
    show vitoria feliz at Position(xpos=.55, ypos=.75) with dissolve

    narrador "A brisa da manhã, a qual assoprava fria, foi substituida pelos raios do meio dia que se estendia no céu como uma folha de ouro sob suas cabeças, e iluminava resplandecia toda a cidade."
    narrador "Caminhando pela praça, a atmosfera acolhedora do vilarejo os envolvia."
    narrador "Passaros cantavam, a natureza era vivída e o grupo de amigos conversava animadamente."

    show sofia at Position(xpos=.85, ypos=.75) with dissolve

    narrador "Ao se aproximarem de um banco perto da fonte, avistaram uma mulher sentada, muito concentrada na leitura de um pequeno livro de capa cor de vinho, sem título." 
    
    hide dante feliz
    hide helena feliz
    with dissolve
    show vitoria feliz at Position(xpos=.65, ypos=.75) with move

    narrador "Ao Vitoria se aproximar para cumprimentar a moça,sua sombra tocou as páginas, e ela notou a presença do grupo."

    show sofia feliz at Position(xpos=.85, ypos=.75) with dissolve

    sofia "Ah. Olá Vitória! Boa tarde?"

    show vitoria feliz at Position(xpos=.4, ypos=.75) with move

    vitoria "Boa tarde Sofia."

    sofia "Helena, olá! Quem é o rapaz?"

    hide vitoria feliz with dissolve
    show helena feliz at Position(xpos=.2, ypos=.77) with dissolve

    helena "Boa tarde, Sofia."
    helena "Este é Dante, o meu amigo de infância."
    helena "Ele está aqui para passar alguns dias conosco e me ajudar em minha pesquisa."

    hide helena feliz with dissolve

    show sofia at Position(xpos=.5, ypos=.75) with move

    sofia "Seja bem-vindo, Dante."
    sofia "Espero que goste da nossa cidade!"

    show sofia at Position(xpos=.85, ypos=.75) with move
    show dante feliz at Position(xpos = .165, ypos=.75) with dissolve

    dante "Muito prazer em conhecê-la! Até agora têm sido uma viajem maravilhosa."

    sofia "Que bom ouvir isso."
    sofia "A Encosta da Saudade é um lugar especial para todos, especialmente para essa menina curiosa."
    sofia "Se quiser saber sobre as curiosidades e fatos históricos daqui, não hesite em me procurar, assim como Helena faz diariamente."

    hide dante normal
    hide sofia normal
    with dissolve
    show isabel feliz at Position(xpos=.5, ypos=.75) with dissolve

    narrador "Enquanto conversavam, Isabel, a esposa do fazendeiro, se aproximou, carregando uma cesta de frutas."

    isabel "Boa noite, meninas."
    isabel "Quem é este rapaz charmoso?"

    show isabel at Position(xpos=.85, ypos=.75) with move

    show vitoria feliz at Position(xpos=.15, ypos=.75) with dissolve

    vitoria "Este é Dante, o amigo de infância da Helena."
    vitoria "Ele está aqui para passar alguns dias conosco."

    hide vitoria feliz with dissolve
    show isabel feliz at Position(xpos=.5, ypos=.75) with move

    isabel "Bem-vindo, Dante."
    isabel "Espero que aproveite sua estadia."
    isabel "Aceite uma maçã fresca da fazenda."

    show isabel at Position(xpos = .85, ypos=.95) with move
    show dante feliz at Position(xpos = .165, ypos=.95) with dissolve

    menu:
        "Aceitar maçã e comer":
            show dante feliz at Position(xpos = .165, ypos=.75)
            show isabel at Position(xpos = .85, ypos=.75)
            with move
            show maça at Position(xpos=.75, ypos=.75) with dissolve
            show maça at Position(xpos=.25, ypos=.75) with move
            hide maça
            show maça-mordida at Position(xpos=.25, ypos=.75)
            with dissolve

            dante "Obrigado, Isabel. É um prazer conhecê-la!"

            hide maça-mordida with dissolve
            
            isabel "O prazer é todo meu, pequeno."

        "Aceitar maça e guardar no bolso":
            $ historia.maca_guardada()
            show dante feliz at Position(xpos = .165, ypos=.75)
            show isabel at Position(xpos = .85, ypos=.75)
            with move

            dante "Muito obrigado, Isabel, acabei de comer um lanche agora a pouco no Pedro."
            dante "É um imenso prazer conhecê-la!"

            isabel "Que pena que está cheio, pelo menos leve essa maça então para o passeio."

            show maça at Position(xpos=.72, ypos=.8) with dissolve
            show maça at Position(xpos=.29, ypos=.8) with move
            hide maça with dissolve

            dante "Obrigado Isabel, comerei ela depois"

            isabel " Tenham um bom passeio crianças."

        "Recusar Maçã":
            show dante feliz at Position(xpos = .165, ypos=.75)
            show isabel at Position(xpos = .85, ypos=.75)
            with move
            
            dante "Muito obrigado, Isabel, mas dispenso, estou cheio de nosso lanche agora a pouco. É um imenso prazer conhecê-la!"
            
            isabel " Que pena que está cheio, fica para a proxima então."
            isabel " Tenham um bom passeio crianças."

    hide dante with dissolve
    show isabel feliz at Position(xpos=.5, ypos=.75) with move


    narrador "Isabel continua seu caminho."

    show isabel at Position(xpos=.15, ypos=.75) with move 
    hide isabel with dissolve

    show sofia at Position(xpos=.5, ypos=.75) with dissolve

    narrador "Sofia se despede e volta a ler seu livro."

    show sofia at Position(xpos=.85, ypos=.75) with move
    hide sofia with dissolve

    show vitoria feliz at Position(xpos=.15, ypos=.75)
    show helena feliz at Position(xpos=.25, ypos=.77)
    show dante feliz at Position(xpos=.45, ypos=.75)
    with dissolve
    show vitoria feliz at Position(xpos=.75, ypos=.75) 
    show helena feliz at Position(xpos=.86, ypos=.77) 
    show dante feliz at Position(xpos=.95, ypos=.75)
    with move 
    hide vitoria normal
    hide helena feliz
    hide dante normal
    with dissolve

    narrador "Os jovens dão continuidade ao passeio."
    narrador "Enquanto continuavam a conversar, Rocha, o policial, aproximou-se do grupo, acenando com um sorriso."

    show policial at Position(xpos=.5, ypos=.75) with dissolve
    
    rocha "Boa tarde, pessoal. Parece que temos um novo rosto na cidade."   

    show policial at Position(xpos=.825, ypos=.75) with move
    show vitoria feliz at Position(xpos=.15, ypos=.75) with dissolve 

    vitoria "Boa tarde, Rocha. Este é Dante, amigo de infância da Helena."  

    hide vitoria with dissolve

    show dante feliz at Position(xpos = .165, ypos=.95)
    show policial at Position(xpos = .85, ypos=.95)
    with move

    menu:
        "Apertar mão de rocha":

            $ historia.incrementar_peso(1)

            hide vitoria with dissolve
            show dante feliz at Position(xpos=.35,ypos=.75)
            show policial at Position(xpos=.65,ypos=.75)
            with move
            
            rocha "Prazer em conhecê-lo, Dante."
            rocha "Espero que aproveite sua estadia."

            show dante feliz at Position(xpos=.165,ypos=.75)
            show policial at Position(xpos=.85,ypos=.75)
            with move
            
            dante "Obrigado, Rocha. Até agora, tudo tem sido ótimo."

            rocha "Isso é bom de ouvir."

        "Acenar mão a distância":
            show dante feliz at Position(xpos=.165,ypos=.75)
            show policial at Position(xpos=.85,ypos=.75)
            with move

            dante "Oi seu policial."
            
            rocha "Meio arisco, não é mesmo?!."
            
            rocha "É sempre bom ser alerta, mesmo que descortes."

    hide dante with dissolve

    show policial at Position(xpos=.5,ypos=.75) with move

    $ renpy.music.set_volume(.15, channel='music')
    play sound "audio/Sound effects/Lugares/Natureza_clima_tensao.mp3" volume .1 loop

    rocha "Mas, preciso alertar vocês sobre algo estranho que aconteceu hoje."
   
    show policial at Position(xpos=.825, ypos=.75) with move
    show vitoria preocupado at Position(xpos=.15, ypos=.75) with dissolve 

    vitoria "O que houve??"
    
    hide dante normal
    hide vitoria 
    with dissolve

    show policial at Position(xpos=.5, ypos=.75) with move

    rocha "Recebemos uma denúncia de que algumas pessoas viram luzes estranhas perto da Igreja nesta madrugada."
    rocha "Não sabemos o que pode ter causado isso, mas é algo que estamos investigando."

    show policial at Position(xpos=.85, ypos=.75) with move
    
    show vitoria preocupado at Position(xpos=.15, ypos=.75) with dissolve

    vitoria "Luzes estranhas?" 
    vitoria " Como assim?"

    hide vitoria normal

    show policial at Position(xpos=.5, ypos=.75) with move

    rocha "Testemunhas dizem que pareciam pequenas esferas de luz flutuando ao redor da igreja, desaparecendo antes de poderem se aproximar."
    rocha "Eu sei que pode parecer estranho, mas estamos tratando isso apenas como rumores até o momento."
    rocha "Se virem algo, por favor, me avisem imediatamente."

    hide policial with dissolve
    show dante preocupado at Position(xpos=.5, ypos=.75) with dissolve

    narrador "Dante sentiu um arrepio percorrer sua espinha."
    narrador "Um misto de agitação e medo pelo suspense entregue por rocha."

    hide dante with dissolve

    show helena preocupado at Position(xpos=.5, ypos=.75) with dissolve
    show helena preocupado at Position(xpos=.15, ypos=.75) with move
    show policial at Position(xpos=.5, ypos=.75) with dissolve
    show policial at Position(xpos=.85, ypos=.75) with move

    helena "Vamos ficar atentos, Rocha. Obrigada por nos avisar"

    rocha "Se precisarem de qualquer coisa, sabem onde me encontrar."

    hide policial with dissolve
    show helena preocupado at Position(xpos=.25, ypos=.75) with move
    show vitoria preocupado at Position(xpos=.4, ypos=.75)
    show dante preocupado at Position(xpos=.55, ypos=.75)
    with dissolve

    narrador "Depois da conversa com o policial, o grupo se despediu e continuou caminhando pela praça, com uma leve tensão no ar."

    show dante preocupado at Position(xpos = .65, ypos=.75)
    show vitoria preocupado at Position(xpos=.5, ypos=.75)
    show helena preocupado at Position(xpos=.35, ypos=.75)
    with move

    show dante preocupado at Position(xpos = .165, ypos=.95)
    show helena preocupado at Position(xpos=.7, ypos=.95):
        xzoom -1
    show vitoria preocupado at Position(xpos=.85, ypos=.95):
        xzoom -1
    with move

    menu:
        "Demonstrar insatisfação":
            show dante preocupado at Position(xpos=.165, ypos=.75)
            show vitoria preocupado at Position(xpos=.85, ypos=.75)
            show helena preocupado at Position(xpos=.7, ypos=.75)
            with move

            dante "Isso é muito estranho"

    vitoria "Concordo"
    vitoria "Mas vamos tentar não nos preocupar demais."
    vitoria "Amanhã é um novo dia, e vamos descobrir mais sobre essa história."

    stop sound fadeout 1.5

    show helena preocupado at Position(xpos=.6, ypos=.75) with move

    helena "Sim, vamos descansar por agora."
    helena "Amanhã vai ser um dia longo."

    hide helena preocupado
    hide dante preocupado
    hide vitoria 
    with dissolve

    scene quarto-helena-noite

    narrador "O grupo chega à casa de Helena, a qual apresenta a Dante o quarto que o acolherá."

    show helena at Position(xpos=.5, ypos=.75) with dissolve

    helena "Espero que goste do quarto. É simples, mas confortável."
    
    show helena at Position(xpos=.35, ypos=.75) with move
    show dante feliz at Position(xpos=.65, ypos=.75) with dissolve

    dante "Está ótimo, Helena. Obrigado por tudo."

    show dante feliz at Position(xpos=.85, ypos=.75):
        xzoom -1    
    with move 
    show vitoria feliz at Position(xpos=.15, ypos=.75) with dissolve

    vitoria "Boa noite, Dante. Até amanhã."

    dante "Boa noite, Vitória."

    show vitoria feliz at Position(xpos=0, ypos=.75):
        xzoom -1
    with move
    hide vitoria with dissolve
    show helena at Position(xpos=.25, ypos=.75):
        xzoom -1
    with move
    
    dante "Boa noite, Helena."

    show helena at Position(xpos=.15, ypos=.75):
            xzoom 1
    
    helena "Boa noite Dante, estaremos no quarto ao lado caso precise."

    show helena at Position(xpos=.15, ypos=.75):
        xzoom -1
    with move
    show helena at Position(xpos=0, ypos=.75) with move
    hide helena with dissolve

    narrador "Com passeios lúdicos e duvidas no ar, chega ao fim o primeiro dia da viagem de dante."

    menu:
        "Dormir":
            dante "ZzZzZzZz"

    return