label capitulo5:
    scene quarto-helena with fade
    show dante at Position(xpos=.85, ypos=.75)

    $ renpy.music.play("audio/Sound effects/Lugares/Natureza_ventania_leve.mp3", loop=True)
    $ renpy.music.set_volume(1.0, channel='music')
    play sound "audio/Sound effects/Objetos/Sinos_tocando_vento_batendo_passaros_fundo.mp3" volume .2 fadein 2.0 loop

    narrador "Novamente Dante é acordado pelo soar do sino da igreja."
    narrador "O ambiente é silencioso, exceto pelo som distante dos sinos."
    
    show dante at Position(xpos=.85, ypos=.75):
        xzoom -1
    with dissolve

    narrador "Dante começa a investigação cedo no dia seguinte, retornando a igreja para tentar entender o sonho que teve."

    show dante at Position(xpos=.25, ypos=.75) with move
    hide dante with dissolve
    stop sound fadeout 2.0

    scene igreja-fora-dia with fade
    show dante at Position(xpos=.165, ypos=.75)

    narrador "O ambiente é carregado de tensão e mistério, refletindo a gravidade da situação."
    narrador "Dante se dirige ao escritório do Padre Iohann, a pessoa que supostamente viu Helena por ultimo."

    scene escritorio-padre with fade
    $ renpy.music.play("audio/Sound effects/pessoas/Celebração_católica_latim_coral_latim_piano_fundo.mp3", loop=True)
    $ renpy.music.set_volume(.1, channel='music')

    show padre orando at Position(xpos=.85, ypos=.75)
    narrador "O escritório é um espaço acolhedor, mas com uma atmosfera pesada."
    narrador "Livros antigos estão empilhados em prateleiras de madeira escura, e um crucifixo pendurado na parede parece observar tudo."
    
    show dante at Position(xpos=.165, ypos=.75) with dissolve

    narrador "O Padre Iohann estava sentado em sua mesa, orando."
    
    show padre preocupado at Position(xpos=.85, ypos=.75) with dissolve

    padre "Com a chegada de Dante o padre para seus ritos e apresenta um semblante de preocupação, misturado com uma leve tensão."

    show dante at Position(xpos=.165, ypos=.95)
    show padre preocupado at Position(xpos=.85, ypos=.95)
    with move
    menu:
        "Por que Helena veio sozinha?":
            show dante at Position(xpos=.165, ypos=.75)
            show padre preocupado at Position(xpos=.85, ypos=.75)
            with move
            
            dante "Padre Iohann, Quando o senhor viu Helena, ela disse o que faria após a procissão?"

            padre "Sim, meu filho, ela disse que queria achar um objeto em forma de cruz, e por isso veio aqui mais cedo"
            padre "Quando eu perguntei a ela por que o interesse nesse especifico quando temos tantos por toda a igreja, ela apenas disse que esse era especial antes de sair de minha vista"

            show dante preocupado at Position(xpos=.165, ypos=.75) with dissolve

            narrador "Dante fica pensativo quanto ao objeto e sai do escritório comprometido a encontrar mais informações sobre tal cruz pela igreja!"

        "Aonde ela foi após ajudar":
            $ historia.incrementar_peso(1)
            show dante at Position(xpos=.165, ypos=.75)
            show padre preocupado at Position(xpos=.85, ypos=.75)
            with move
            dante "Padre Iohann, você viu aonde Helena foi após auxiliar na procissão?"
            
            padre "Sim, a vi naquele dia mais cedo . Ela disse que ia ajudar na montagem da procissão e queria saber sobre um objeto."
            padre "Ícaro e Augusto podem ter visto algo. Procure os seminaristas na sala ao lado."

            narrador "O Padre se mostrava exausto, desviando o olhar e dando respostas vagas."

            show dante preocupado at Position(xpos=.165, ypos=.75) with dissolve

            narrador "Dante percebe uma sensação de desconforto, levando-o a procurar pistas com os coroinha."
    
            padre "Ah, ela também citou estar atrás de um objeto que poderia estar aqui, ela sempre o procura na biblioteca."
            padre "Se tiver um livro lá sem poeira, foi Helena que tirou lendo."

            narrador "Repete o padre, adicionado informações de onde Helena poderia ter passado."

    padre "Esse objeto era um relicário dourado, meu filho"

    narrador "Completa o padre"

    hide dante preocupado with dissolve

    narrador "Dante deixa o escritório, passando pelos corredores da igreja que parecera ainda mais vazios, refletindo a perda da amiga."

    scene sala-dos-seminaristas
    show icaro sentado at Position(xpos=.6, ypos=.75)
    show augusto lendo at Position(xpos=.85, ypos=.75)

    narrador "Após passar por diversas salas da igreja chega a sala de estudos dos seminaristas"
    narrador "A sala é modesta, com bancos de madeira e mesas dispostas em linha."
    narrador "Decidido a encontrar pistas uteis questiona se os seminaristas sabem de algo"
    narrador "Ícaro e Augusto estão ocupados com seus estudos, a luz suave das lâmpadas cria um ambiente introspectivo."

    show dante at Position(xpos=.165, ypos=.75) with dissolve

    narrador "Augusto parece imerso em sua leitura e apenas Icaro nota Dante"

    hide augusto lendo with dissolve
    show icaro preocupado at Position(xpos=.85, ypos=.75)
    with move

    icaro "Bom dia Dante, como você está nessa manhã? Alguma boa notícia"

    dante "Bom dia amigo de fé, ainda não, foi justamente sobre isso que vim conversar"

    show dante at Position(xpos=.165, ypos=.95) 
    show icaro sentado at Position(xpos=.8, ypos=.95)
    with move

    menu:
        "Perguntar sobre a noite do desaparecimento":
            $ historia.incrementar_peso(1)
            show dante at Position(xpos=.165, ypos=.75) 
            show icaro sentado at Position(xpos=.85, ypos=.75)
            with move

            dante "Vocês viram Helena procurar por algo na manhã que desapareceu?"

            icaro "Eu ouvi murmúrios na biblioteca e vi uma figura encapuzada pela vidraça. Foi muito estranho."
            icaro "Mas sobre ela procurar por algo, lembro de ser sobre um relicário que pertencerá a familia fundadora do vilarejo."
            icaro "Não sei se pode ajudar muito, mas temos documentos dessa epoca que ela estava lendo antes de você chegar."

        "Questionar sobre o Padre Iohann":
            show dante at Position(xpos=.165, ypos=.75) 
            show icaro sentado at Position(xpos=.85, ypos=.75)
            with move

            dante "Vocês notaram algo estranho no comportamento do Padre Iohann?"

            icaro "Ele tem estado mais reservado ultimamente. Algo parece incomodá-lo."
            icaro "Recentemente, vi ele saindo da igreja tarde da noite, o que é bem incomum. Ele parecia estar carregando algo, mas não consegui ver o que era."
            icaro "A atmosfera ao redor dele mudou. É como se ele estivesse carregando um grande fardo."
            icaro "Nós também ouvimos alguns sussurros e passos estranhos vindo da bibliotéca da paroquia nas últimas noites, aconselho prestar uma visita lá."

    show icaro sentado at Position(xpos=.6, ypos=.75) with move
    show augusto lendo at Position(xpos=.85, ypos=.75)with dissolve

    hide dante with dissolve

    narrador "Dante se despede e se dirige à biblioteca da igreja, refletindo sobre as novas pistas e deixando os seminaristas livres para seus estudos novamente."

    scene biblioteca-trevosa
    show dante at Position(xpos=.5, ypos=.75) with dissolve

    narrador "A biblioteca é um local de silêncio absoluto, com estantes repletas de livros antigos."
    narrador "A luz da tarde filtra-se através das janelas, criando um jogo de luz e sombra que aumenta o mistério."
    narrador "Livros sobre documentações antigas estão espalhados sobre a mesa, alguns cobertos por uma fina camada de poeira e outros recentemente utilizados."

    show dante at Position(xpos=.5, ypos=.95) with move

    menu:
        "Investigar os livros novos":
            $ historia.incrementar_peso(1)
            show dante at Position(xpos=.4, ypos=.75) with move
            show livro antigo at Position(xpos=.6, ypos=.75) with dissolve
            
            narrador "Dante encontra um livro sobre o relicário e rituais antigos, descobrindo possiveis rituais ligados ao objeto."
            narrador "No livro também mostra que o relicário é uma herança da familia mais antiga da cidade."

            dante "Isso pode ser importante. Preciso investigar quem são os antigos donos dessa cruz."

        "Investigar os livros antigos":
            show dante at Position(xpos=.6, ypos=.75):
                xzoom -1
            with move
            show livro antigo at Position(xpos=.25, ypos=.5):
                xzoom -1
            with dissolve

            narrador "Dante encontra um livro sobre lendas antigas, sugerindo uma conexão com práticas ocultas."

            dante "Isso está ficando cada vez mais estranho. Preciso ter cuidado."

    hide livro antigo with dissolve
    show dante at Position(xpos=.5, ypos=.75):
        xzoom 1
    with move

    narrador "Após uma dezena de livros lidos, Dante decide verificar o registro da cidade."

    show dante at Position(xpos=.35, ypos=.75) with move
    show livro aberto at Position(xpos=.65, ypos=.75) with dissolve

    narrador "O registro aponta a familia de pedro, o confeiteiro, como antiga dona da cruz dourada"
    narrador "Vindos do méxico, essa familia se mostra fortemente ligada a criação do vilarejo e de áreas não mais utilizadas atualmente, identificadas como canais, no entorno da cidade"

    scene biblioteca-noite with fade
    show dante at Position(xpos=.35, ypos=.75)
    show livro aberto at Position(xpos=.65, ypos=.75)   

    narrador "A biblioteca apresenta mais sombria do que antes, com as manchas da noite se alongando e criando um ambiente inquietante."

    show dante at Position(xpos=.25, ypos=.75)
    show livro aberto at Position(xpos=.5, ypos=.75)
    with move
    show vitoria preocupado at Position(xpos=.62, ypos=.25):
        xzoom -1
    with dissolve

    narrador "Vitoria chega abatida por não ter visto Dante o dia todo"

    vitoria "Dante, não me deixe tão preocupada, te procurei o dia todo, do raiar ao entardecer, entrei em panico pensando que você tinha sumido como a Helena"

    dante "Não Vitória, estou bem, desculpe"
    dante "Precisamos encontrar algo que nos dê uma pista definitiva."

    vitoria "Vou verificar os registros históricos, talvez haja algo que nos ajude."

    hide livro aberto with dissolve

    dante "Já fiz isso, precisamos ir ver o seu Pedro, o livro de registros diz que a familia dele tinha posse de uma cruz dourada a qual Helena estava atrás"

    vitoria "O relicário?"
    vitoria "Lembro de Helena ler sobre ele no inicio das férias"
    vitoria "Vocé está me dizendo que ela sumiu procurando por isso?"

    dante "Essa é minha melhor aposta"

    hide dante
    hide vitoria preocupado
    with dissolve

    narrador "Dante e Vitória se dirigem para a casa de Seu Pedro."

    $ renpy.music.play("audio/Sound effects/Lugares/Natureza_clima_pesado_suspense.mp3", loop=True)
    $ renpy.music.set_volume(.15, channel='music')
    scene casa-pedro
    show pedro at Position(xpos = 0.85, ypos = 0.75)

    narrador "A casa é simples e acolhedora, com móveis antigos e uma atmosfera nostalgica."
    narrador "Seu Pedro está sentado, com um olhar preocupado, rodeado por velhas fotografias e lembranças."

    pedro "Olá meninos, alguma notícia da nossa menina Helena?"

    vitoria "Ainda não Seu Pedro, viemos exatamente por isso."

    menu:
        "Perguntar sobre o relicário":
            vitoria "Seu Pedro, você sabe algo sobre o relicário que Helena estava interessada?"

            pedro "Aquele dourado? Ela acreditava que ele tinha um grande poder, mas não o vejo desde que era um menino, nem sei se ainda o tenho."
            pedro "Também já havia dito isso a essa moleca sapeca, agora toda a cidade está preocupada com uma fujona correndo atrás de rumores"
            pedro "Da ultima vez que conversamos, ela me perguntou se eu sabia das construções feitas por minha familia."
            pedro "Meu Deus, talvez ela tenha ido lá."
            pedro "Deus, que esse não seja o caso, seria perigoso estar lá fora a tanto tempo em uma área cavernosa tão abandonada."
            pedro "Vamos pedir para o Rocha ir lá amanhã crianças. descansem e iremos achar essa custosa logo cedo."

            narrador "O ambiente se torna carregado de suspense, com Dante recebendo uma nova pista para investigar."

    return