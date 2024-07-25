label capitulo2:

    $ renpy.music.play("audio/Capitulos/Capitulo 2 - uma vista calorosa.mp3", loop=True)
    $ renpy.music.set_volume(.10, channel='music')

    scene centro

    narrador "Dante sentia a sensação de voltar para o passado"
    narrador "A paisagem verdejante e as casas simples no estilo barroco europeu lembravam sua infância, passada numa pequena cidade no interior de Goiás"
    narrador "Ao descer do ônibus e olhar em volta, ficou impressionado pela beleza da cidade."
    narrador "O sol começava a se pôr, pintando o céu de tons dourados e fazendo com que as casas da vila parecessem ainda mais charmosas"

    show vitoria normal at Position(xpos=.65, ypos=.75) with dissolve

    show helena-vestido-azul-feliz at Position(xpos=.3, ypos=.75) with dissolve


    narrador "Helena estava radiante em um vestido azul, e lhe aguardava com um grande sorriso, acompanhada por uma amiga, que fora momentaneamente ofuscada pelo brilho de Helena."

    show vitoria normal at Position(xpos=1., y=.75) with move
    hide vitoria normal with dissolve

    show helena-vestido-azul-feliz at Position(xpos=.85, ypos=.75) with move

    helena "Tão bom te ver!"

    show helena-vestido-azul-feliz at Position(xpos=.85, ypos=.95) with move

    show dante normal at Position(xpos = .165, ypos=.95) with dissolve

    menu: 
        "Abraçar":
            show helena-vestido-azul-feliz at Position(xpos=.65, ypos=.75)
            show dante normal at Position(xpos=.45, ypos=.75)
            with move

            dante "Olá, Helena! Você mudou muito desde a última vez que nos vimos!"

            narrador "Dante pensa em voz alta exaltando a beleza da amiga"

            dante "Está estonteantemente linda!"

            show helena-vestido-azul-feliz at Position(xpos=.85, ypos=.75)
            show dante normal at Position(xpos = .165, ypos=.75)
            with move

            narrador "Helena se distancia por ter ficado embasbacada com o elogio durante o abraço enquanto Vitória se apresenta"
    
    hide helena-vestido-azul-feliz with dissolve

    show vitoria normal at Position(xpos = .7, ypos = .25):
        xzoom -1
    with dissolve

    vitoria "Olá, Dante! Sou a Vitória, muito prazer"

    menu:
        "Cumprimentar cordialmente":
            show vitoria normal at Position(xpos=.6, ypos=.25)
            show dante normal at Position(xpos=.3, ypos=.75)
            with move

            dante "Prazer Vitória, como é bom te conhecer!"

            show vitoria normal at Position(xpos=.7, ypos=.25)
            show dante normal at Position(xpos = .165, ypos=.75)
            with move
    
    show helena-vestido-azul-feliz at Position(xpos=.50,ypos=.75)

    helena "Vamos começar nosso passeio amigos"

    show vitoria normal at Position(xpos=.5, ypos=.25)
    show dante normal at Position(xpos=.3, ypos=.75)
    with move

    narrador "disse Helena antes de pegar ambos pelos braços e sair correndo em direção ao centro da cidade."

    hide helena-vestido-azul-feliz with dissolve

    hide dante normal
    hide vitoria normal
    with dissolve


    narrador "O trio passou o dia caminhando pelo centro da cidade" 
    narrador "Conheceram alguns residentes e atravessaram um riacho..."
    narrador "Até chegarem na porta da Igreja da Misericórdia, uma bela igreja antiga."

    play sound "audio/Sound effects/Objetos/Sinos_tocando_vento_batendo_passaros_fundo.mp3" volume .2 fadein 2.0

    scene igreja-fora-dia

    narrador "Apesar de Dante de não ser muito religioso..."
    narrador "O garoto sentiu uma sensação estranha enquanto olhava para a igreja, como se alguma energia misteriosa o atraísse."

    show dante normal at Position(xpos = .165, ypos=.75) with dissolve

    dante "Que bela igreja!"

    show helena-vestido-azul-feliz at Position(xpos=.85, ypos=.75) with dissolve

    helena "É incrível, né?"
    helena "A Igreja é símbolo deste lugar. Seus fundadores vieram da Europa e trouxeram a tradição católica aqui"


    hide dante normal
    hide helena-vestido-azul-feliz
    with dissolve
    stop sound fadeout 1.5

    scene padaria-fora

    $ renpy.music.play("audio/Sound effects/pessoas/Homem_cantarolar_senior_trabalhando_corte.mp3", loop=True)
    $ renpy.music.set_volume(.5, channel='music')

    narrador "Após uma tarde de conversa, os três se dirigiram para a padaria favorita de Vitória, próxima à praça principal da cidade."
    narrador "Lá, foram recebidos por Seu Pedro, o padeiro."
    
    show pedro normal at Position(xpos=.5, ypos=.75) with dissolve

    pedro "Olha quem veio! Helena, você trouxe um visitante especial, não é? "

    show pedro normal at Position(xpos=.75, ypos=.75) with move

    show helena-vestido-azul-feliz at Position(xpos=.075,ypos=.2175):
        xzoom -1
    with dissolve

    helena "Ah, Seu Pedro! Este é o meu amigo Dante. Ele está aqui para passar alguns dias conosco."

    pedro "Ah sim! Bem-vindo ao vilarejo! Eu sou Pedro"

    hide helena-vestido-azul-feliz with dissolve

    show pedro normal at Position(xpos=.8, ypos=.95) with move
    show dante normal at Position(xpos = .165, ypos=.95) with dissolve 

    menu: 
        "Apertar a mão de Pedro":

            show dante normal at Position(xpos=.25, ypos=.75)
            show pedro normal at Position(xpos=.65, ypos=.75)
            with move

            dante "Obrigado, Seu Pedro. É um prazer conhecer você."

    hide dante normal with dissolve
    show pedro normal at Position(xpos=.5, ypos=.75)
    with move

    pedro "O que querem comer? Aposto que estão morrendo de fome..."

    play sound "audio/Sound effects/pessoas/Grupo_misto_rindo.mp3"

    narrador "Mal ele terminara a frase, Helena e Vitória riram em disparate, acompanhadas pelo padeiro"

    menu:
        "Sorrir confuso":
            narrador "Dante olhou para Helena e Vitória, ainda rindo, e sorriu confuso"

        "Pedir explicação":
            show pedro normal at Position(xpos=.8, ypos=.75) with move
            show dante normal at Position(xpos = .165, ypos=.75) with dissolve

            narrador "Sem entender muito, Dante indaga a Helena e Vitoria qual foi a graça da fala"

            dante "Eu realmente estou com fome após a viagem, por que as risadas?"

            hide pedro normal with dissolve

            show helena-vestido-azul-feliz at Position(xpos=.85, ypos=.75) with move

            helena "Não seja tão careta Dante, o seu Pedro trabalha no cemitério da cidade por isso a graça em morrendo de fome"

            stop sound

            dante "Nossa, já tinha ouvido falar de padeiro que fazia a função de açogueiro e barbeiro, mas coveiro é a primeira vez." 

            helena "Por isso mesmo, seu Pedro não é uma figura!"

            hide helena-vestido-azul-feliz

    hide pedro normal 
    hide dante normal
    with dissolve

    narrador "Seu Pedro, com seu semblante acolhedor, guiou o trio até uma mesa perto da cozinha, de onde podia-se sentir o cheiro das delicias ali preparadas."

    scene padaria-dentro
    stop sound
    show pedro normal at Position(xpos=.5, ypos=.75) with dissolve

    pedro "Hoje temos pão de queijo fresquinho, broa de milho, e bolos variados"
    
    narrador "Anunciou Seu Pedro, com um sorriso orgulhoso."
    
    pedro "E claro, o café passado na hora, que não pode faltar."

    show pedro normal at Position(xpos=.85, ypos=.75) with move
    show helena-vestido-azul-feliz at Position(xpos=.15, ypos=.75) with dissolve

    helena "Parece uma ótima escolha! Vou querer um pouco de tudo, para experimentar."

    hide pedro normal
    hide helena-vestido-azul-feliz with dissolve
    $ renpy.music.set_volume(.2, channel='music')
    
    show vitoria normal at Position(xpos=.7, ypos=.25):
        xzoom -1
    with dissolve 

    vitoria "Dante, você vai adorar o festival!"
    vitoria "É a melhor época do ano aqui: tem música, danças tradicionais, comidas típicas e até bingo!"

    show dante normal at Position(xpos = .165, ypos=.75) with dissolve

    dante "Sou muito bom no bingo hein!"
    dante "Já estou ansioso, Parece incrível!"

    show pedro normal at Position(xpos=.45, ypos=.75) with dissolve
    
    $ renpy.music.set_volume(.6, channel='music')

    narrador "Logo, Seu Pedro retornou com uma bandeja cheia de delícias, e os três começaram a comer, rindo e conversando sobre a vida no vilarejo e relembrando histórias de infância."

    narrador " A tarde caía e Dante sentiu-se mais relaxado e feliz do que em muito tempo."
    narrador "Depois de agradecer calorosamente a Seu Pedro e pagarem a conta, o trio se dirigiu à praça principal. "

    hide dante normal
    hide vitoria normal
    with dissolve

    $ renpy.music.play("audio/Sound effects/Lugares/Safe_house_seguro_tranquilo.mp3", loop=True)
    $ renpy.music.set_volume(.3, channel='music')
 
    scene praca-principal with fade

    play sound "audio/Sound effects/Lugares/Natureza_ventania_leve.mp3"

    narrador "A brisa da tarde assoprava fria e o céu se estendia como uma folha de ouro sob suas cabeças, e iluminava resplandecia toda a cidade"
    narrador "Caminhando pela praça, a atmosfera acolhedora do vilarejo os envolvia."
    narrador "Crianças corriam e brincavam, e o grupo de amigos conversava animadamente"
    narrador "Ao se aproximarem de um banco perto da fonte, avistaram uma mulher sentada, muito concentrada na leitura de um pequeno livro de capa cor de vinho, sem título." 
    narrador "A sombra de Helena tocou as páginas, e ela notou a presença do grupo."

    stop sound

    show sofia normal at Position(xpos=.85, ypos=.75) with dissolve

    sofia "Helena, Vitória! Quem é o rapaz?"

    show helena-vestido-azul-feliz at Position(xpos=.15, ypos=.75) with dissolve

    helena "Boa tarde, Sofia"
    helena "Este é Dante, o amigo meu de infância"
    helena "Ele está aqui para passar alguns dias conosco"

    hide helena-vestido-azul-feliz normal with dissolve
    show sofia normal at Position(xpos=.5, ypos=.75) with move

    sofia "Seja bem-vindo, Dante"
    sofia "Espero que goste da nossa cidade"

    show sofia normal at Position(xpos=.85, ypos=.75) with move
    show dante normal at Position(xpos = .165, ypos=.75) with dissolve

    dante "Muito prazer em conhecê-la! Até agora, todos têm sido muito acolhedores."

    sofia "Que bom ouvir isso. A Encosta da Saudade é um lugar especial. Se precisar de algo, não hesite em me procurar."

    narrador "Enquanto conversavam, Isabel, a esposa do fazendeiro, se aproximou, carregando uma cesta de frutas."

    hide dante normal 
    hide sofia normal
    with dissolve

    show isabel normal at Position(xpos=.5, ypos=.75) with dissolve

    isabel "Boa noite, meninas. Quem é este rapaz charmoso?"

    show isabel normal at Position(xpos=.85, ypos=.75) with move

    show vitoria normal at Position(xpos=.15, ypos=.75)

    vitoria "Este é Dante, um amigo de infância da Helena. Ele está aqui para passar alguns dias conosco."

    isabel " Bem-vindo, Dante. Espero que aproveite sua estadia. Aceite uma maçã fresca da fazenda."

    hide vitoria normal with dissolve

    show dante normal at Position(xpos = .165, ypos=.75) with dissolve

    menu:
        "Aceitar maçã e comer":
            
            dante "Obrigado, Isabel. É um prazer conhecê-la!"
            
            isabel " O prazer é todo meu pequeno."

        "Aceitar maça e guardar no bolso":

            dante "Muito obrigado, Isabel, acabei de comer um lanche agora a pouco no Pedro."
            dante "É um imenso prazer conhecê-la!"

            isabel " Que pena que está cheio, pelo menos leve essa maça então para o passeio."

            $ historia.maca_guardada()
            narrador "Dante pega a maça e a guarda!"

            isabel " Tenham um bom passeio crianças."

        "Recusar Maçã":
            
            dante "Muito obrigado, Isabel, mas dispenso, estou cheio de nosso lanche agora a pouco. É um imenso prazer conhecê-la!"
            
            isabel " Que pena que está cheio, fica para a proxima então a maça."
            isabel " Tenham um bom passeio crianças."

    hide dante normal with dissolve

    narrador "Isabel continua seu caminho"

    show isabel normal at Position(xpos=0, ypos=.75) with move 
    hide isabel normal with dissolve

    show sofia normal at Position(xpos=.5, ypos=.75) with dissolve

    narrador "Sofia se despede e volta a ler seu livro"

    hide sofia normal with dissolve

    narrador "Os jovens dão continuidade ao passeio."

    show vitoria normal at Position(xpos=.15, ypos=.75)
    show helena-vestido-azul-feliz at Position(xpos=.25, ypos=.75)
    show dante normal at Position(xpos=.45, ypos=.75)
    with dissolve
    show vitoria normal at Position(xpos=1., ypos=.75) 
    show helena-vestido-azul-feliz at Position(xpos=1., ypos=.75) 
    show dante normal at Position(xpos=1., ypos=.75)
    with move 
    hide vitoria normal with dissolve
    hide helena-vestido-azul-feliz with dissolve
    hide dante normal with dissolve

    narrador "Enquanto continuavam a conversar, Rocha, o policial, aproximou-se do grupo, acenando com um sorriso."

    show rocha normal at Position(xpos=.5, ypos=.75) with dissolve
    
    rocha "Boa tarde, pessoal. Parece que temos um novo rosto na cidade"   

    show rocha normal at Position(xpos=.825, ypos=.75) with move
    show vitoria normal at Position(xpos=.15, ypos=.75) with dissolve 

    vitoria "Boa tarde, Rocha. Este é Dante, amigo de infância da Helena"  


    show vitoria normal at Position(xpos=.35,ypos=.75) with move
    show dante normal at Position(xpos = .165, ypos=.75) with dissolve

    menu:
        "Apertar mão de rocha firmemente":
            hide vitoria normal with dissolve
            show dante normal at Position(xpos=.35,ypos=.75) with move
            show rocha normal at Position(xpos=.65,ypos=.75) with move

            rocha "Prazer em conhecê-lo, Dante"
            rocha "Espero que aproveite sua estadia."
            
            dante "Obrigado, Rocha. Até agora, tudo tem sido ótimo"

            rocha "Isso é bom de ouvir"

        "Acenar mão a distância":
            dante "Oi seu policial"
            
            rocha "Meio arisco, não é mesmo?!."
            
            rocha "É sempre bom ser alerta, mesmo que descortes."

    hide dante normal with dissolve

    show rocha normal at Position(xpos=.5,ypos=.75) with move

    $ renpy.music.set_volume(.15, channel='music')
    play sound "audio/Sound effects/Lugares/Praca_clima_tensao.mp3" volume .1 loop

    rocha "Mas, preciso alertar vocês sobre algo estranho que aconteceu hoje."
   
    show rocha normal at Position(xpos=.825, ypos=.75) with move
    show vitoria normal at Position(xpos=.15, ypos=.75) with dissolve 

    vitoria "O que houve??"
    
    hide dante normal
    hide vitoria normal 
    with dissolve

    show rocha normal at Position(xpos=.5, ypos=.75) with move

    rocha "Recebemos uma denúncia de que algumas pessoas viram luzes estranhas perto da Igreja nesta madrugada."
    rocha "Não sabemos o que pode ter causado isso, mas é algo que estamos investigando"

    show rocha normal at Position(xpos=.85, ypos=.75) with move
    
    show vitoria normal at Position(xpos=.15, ypos=.75) with dissolve

    vitoria "Luzes estranhas?" 
    vitoria " Como assim?"

    hide vitoria normal

    show rocha normal at Position(xpos=.5, ypos=.75) with move

    rocha "Testemunhas dizem que pareciam pequenas esferas de luz flutuando ao redor da igreja, desaparecendo antes de poderem se aproximar"
    rocha "Eu sei que pode parecer estranho, mas estamos tratando isso como apenas rumores."
    rocha "Se virem algo, por favor, nos avisem imediatamente."

    hide rocha normal with dissolve
    show dante normal at Position(xpos=.5, ypos=.75) with dissolve

    narrador "Dante sentiu um arrepio percorrer sua espinha. Aquela Igreja já lhe causara uma sensação estranha durante o dia."

    hide dante normal with dissolve

    show helena-vestido-azul-feliz at Position(xpos=.5, ypos=.75) with dissolve
    show helena-vestido-azul-feliz at Position(xpos=.15, ypos=.75) with move
    show rocha normal at Position(xpos=.5, ypos=.75) with dissolve
    show rocha normal at Position(xpos=.85, ypos=.75) with move

    helena "Vamos ficar atentos, Rocha. Obrigada por nos avisar"

    rocha "Se precisarem de qualquer coisa, sabem onde me encontrar."


    hide rocha normal with dissolve
    show helena-vestido-azul-feliz at Position(xpos=.35, ypos=.75) with move

    show vitoria normal at Position(xpos=.50, ypos=.75)
    show dante normal at Position(xpos=.65, ypos=.75)
    with dissolve

    narrador "Depois da conversa com o policial, o grupo se despediu e continuou caminhando pela praça, com uma leve tensão no ar."

    show dante normal at Position(xpos = .165, ypos=.75)
    show helena-vestido-azul-feliz at Position(xpos=.75, ypos=.75)
    show vitoria normal at Position(xpos=.85, ypos=.75):
        xzoom -1
    with move

    dante "Isso é muito estranho"

    hide helena-vestido-azul-feliz with dissolve

    vitoria "Concordo"
    vitoria "Mas vamos tentar não nos preocupar demais"
    vitoria "Amanhã é um novo dia, e vamos descobrir mais sobre essa história."

    stop sound fadeout 1.5

    show helena-vestido-azul-feliz at Position(xpos=.65, ypos=.75) 

    helena "Sim, vamos descansar agora."
    helena "Amanhã pode ser um dia longo"

    hide helena-vestido-azul-feliz
    hide dante normal
    hide vitoria normal 
    with dissolve

    scene quarto-helena

    narrador "O grupo chega à casa de Helena e as meninas apresentam ao Dante o quarto que o acolherá"

    show helena-vestido-azul-feliz at Position(xpos=.5, ypos=.75) with dissolve

    helena "Espero que goste do quarto. É simples, mas confortável"
    
    show helena-vestido-azul-feliz at Position(xpos=.35, ypos=.75) with move
    show dante normal at Position(xpos=.65, ypos=.75) with dissolve

    dante "Está ótimo, Helena. Obrigado por tudo"

    show dante normal at Position(xpos=.85, ypos=.75):
        xzoom -1    
    with move 
    show vitoria normal at Position(xpos=.15, ypos=.75) with dissolve

    vitoria "Boa noite, Dante. Até amanhã"

    dante "Boa noite, Vitória."

    show vitoria normal at Position(xpos=0, ypos=.75):
        xzoom -1
    with move
    hide vitoria normal with dissolve
    show helena-vestido-azul-feliz at Position(xpos=.25, ypos=.75) with move
    
    dante "Boa noite, Helena"

    show helena-vestido-azul-feliz at Position(xpos=.15, ypos=.75) with move
    
    helena "Boa noite Dante, estaremos no quarto ao lado caso precise"

    show helena-vestido-azul-feliz at Position(xpos=0, ypos=.75) with move
    hide helena-vestido-azul-feliz with dissolve

    narrador "Com passeios lúdicos e duvidas no ar, chega ao fim o primeiro dia da viagem de dante"

    hide dante normal with dissolve

    return