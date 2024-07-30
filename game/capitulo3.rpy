label capitulo3:
    scene quarto-helena with fade
    
    show dante at Position(xpos=.85, ypos=.75)

    play sound "audio/Sound effects/Objetos/Sinos_tocando_vento_batendo_passaros_fundo.mp3" volume 0.25

    narrador "O sol ainda estava nascendo quando Dante foi despertado por um som distante de sinos."

    play sound "audio/Sound effects/pessoas/Homem_acordando_alongamento_escandaloso_descansado_cena_descontração.mp3" volume.3

    show dante at Position(xpos=.85, ypos=.75):
        xzoom -1    
    with dissolve
    narrador "Ele se levantou, espreguiçando-se e ouvindo os sons suaves do vilarejo."
    show dante at Position(xpos=.25, ypos=.75) with move

    stop sound
    play sound "audio/Capitulos/Capitulo 3 - inicio dos sinais de cansaço.mp3"
    $ renpy.music.set_volume(0.2, channel='music')

    scene cozinha 

    show vitoria at Position(xpos=.72, ypos=.25):
        xzoom -1
    show helena at Position(xpos=.5, ypos=.25):
        xzoom -1
    with dissolve
    show dante at Position(xpos=.165, ypos=.75) with dissolve

    play sound "audio/Sound effects/Objetos/Panela_fritando_oléo_quente.mp3" volume.2

    narrador "Helena e Vitória já estavam na cozinha, preparando o café da manhã."
    
    helena "Bom dia, Dante! Dormiu bem?"

    show vitoria at Position(xpos=.72, ypos=.45)
    show helena at Position(xpos=.5, ypos=.45)
    show dante at Position(xpos=.165, ypos=.95)
    with move

    menu:
        "Dormi bem.":
            $ historia.incrementar_peso(1)

            show vitoria at Position(xpos=.72, ypos=.25)
            show helena at Position(xpos=.5, ypos=.25)
            show dante at Position(xpos=.165, ypos=.75)
            with move

            dante "Dormi sim, obrigado. O cheiro de café está maravilhoso."

        "Noite péssima de sono":
            show vitoria at Position(xpos=.72, ypos=.25)
            show helena at Position(xpos=.5, ypos=.25)
            show dante at Position(xpos=.165, ypos=.75)
            with move

            dante "Tive uma noite péssima. Ao menos o cheiro de café está maravilhoso."

    play sound "audio/Sound effects/pessoas/Pessoa_bebendo_café_xicará_garganta.mp3"

    narrador "Enquanto tomavam café, Helena e Vitória discutiam o plano do dia."

    helena "Pensei em levar você para conhecer a Igreja da Misericórdia e conversar com o Padre Iohann."
    helena "Ele é uma pessoa fascinante e me ajuda muito nas minhas pesquisas sobre o passado do vilarejo"

    narrador "Dante assentiu, momentaneamente lembrando-se das palavras de Rocha sobre as luzes estranhas."
    narrador "Ele estava curioso para conhecer o Padre Iohann e descobrir mais sobre a igreja que tanto o intrigara."

    stop sound

    narrador "Após o café, o trio seguiu em direção à igreja."

    scene igreja-dentro
    # show padre orando at Position(xpos=.85, ypos=.75)
    show padre orando pequeno at Position(xpos=.57, ypos=.64)

    $ renpy.music.play("audio/Sound effects/Objetos/Celebração_católica_orgão_melodia_completa.mp3", loop=True)
    $ renpy.music.set_volume(0.04, channel='music')

    narrador "Quando chegaram à igreja, Dante ficou impressionado novamente com sua arquitetura."
    narrador "No altar, um homem alto de cabelos negros e olhos cansados estava terminando suas orações."
    narrador "Ao entrarem, foram recebidos pelo som suave do órgão e pelo aroma de incenso."

    show vitoria at Position(xpos=.15, ypos=.75)
    show helena at Position(xpos=.3, ypos=.75)
    show dante at Position(xpos=.5, ypos=.75)
    with dissolve

    narrador "Ao fim de sua reza, o padre notou o grupo."

    show padre at Position(xpos=.85, ypos=.75) with move

    padre "Bom dia, Helena!"
    padre "Bom dia, Vitória!"
    padre "E você deve ser Dante, o amigo que Helena comentou que viria prestar uma visita."
    padre "Sou o Padre Iohann. Seja bem-vindo à nossa igreja."

    hide helena normal
    hide vitoria normal
    with dissolve
    show dante at Position(xpos=.165, ypos=.75) with move

    dante "Muito prazer em conhecê-lo, Padre Iohann. É um lugar lindo."

    padre "Obrigado, meu filho. Esta igreja tem raizes antigas, que muitos desconhecem."
    padre "Espero que possam sentir a paz que ela proporciona."

    hide padre with dissolve
    hide dante normal with dissolve

    show icaro at Position(xpos=.65, ypos=.75)
    show augusto lendo at Position(xpos=.85, ypos=.75)
    with dissolve

    narrador "Enquanto conversavam, dois jovens seminaristas se aproximaram, curiosos. Helena os apresentou a Dante."

    show dante at Position(xpos=.165, ypos=.75)
    show helena at Position(xpos=.35, ypos=.75)
    with dissolve

    helena "Este é Ícaro e aquele é Augusto. Eles estão estudando aqui com o Padre Iohann."

    icaro "Muito prazer. É sempre bom conhecer pessoas novas, principalmente da nossa idade."

    augusto "Prazer em conhecê-lo."

    narrador "Dante sentiu uma sensação de camaradagem entre os seminaristas e o padre."

    hide icaro normal
    hide augusto normal
    hide helena normal
    with dissolve

    show dante at Position(xpos=.5, ypos=.75) with move

    narrador "Ao notar mais na decoração da igreja, com seus vitrais coloridos refletindo e colorindo a luz do sol nas paredes, Dante viu um espetáculo de cores."

    show dante at Position(xpos=.5, ypos=.75):
        xzoom -1
    with move

    narrador "Como uma epifánia, Dante lembrou das luzes estranhas mencionadas por Rocha."

    show dante at Position(xpos=.165, ypos=.95):
        xzoom 1
    with move
    show padre at Position(xpos=.85, ypos=.95) with dissolve


    menu:
        "Perguntar sobre as luzes estranhas":

            $ historia.incrementar_peso(1)

            show padre at Position(xpos=.85, ypos=.75)
            show dante at Position(xpos=.165, ypos=.75)
            with move

            dante "Padre Iohann, ouvimos algumas histórias sobre luzes estranhas perto da igreja. O senhor sabe de algo?"

            show padre preocupado at Position(xpos=.85, ypos=.75) with dissolve
            
            narrador "O padre franziu a testa levemente antes de responder, seus olhos se tornando ainda mais profundos e misteriosos."
            
            show padre orando at Position(xpos=.85, ypos=.75) with dissolve
            
            padre "Sim, soube dessas histórias."
            
            show padre at Position(xpos=.85, ypos=.75) with dissolve

            padre "Alguns fiéis relataram ter visto essas luzes proxima a igreja qunado estão vindo à missa, mas não temos nenhuma explicação concreta."
            padre "Estamos investigando. Até agora nada de anormal foi encontrado."

            hide padre normal
            hide helena normal
            with dissolve
            show dante at Position(xpos=.5, ypos=.75) with move
            show dante preocupado at Position(xpos=.5, ypos=.75) with dissolve 

            narrador "Dante notou um leve tremor na mão do padre enquanto ele falava."

        "Não perguntar sobre as luzes estranhas":
            pass

    show dante at Position(xpos=.165, ypos=.75) with move
    show padre at Position(xpos=.85, ypos=.75)
    show helena at Position(xpos=.35, ypos=.75)
    with dissolve
    narrador "O grupo caminhou pelos corredores, admirando as obras de arte e as relíquias históricas."

    $ renpy.music.set_volume(0.02, channel='music')

    scene sacristia with dissolve

    narrador "Ao chegarem à sacristia, notaram um antigo livro de registros, que parecia estar ali há séculos."

    show padre at Position(xpos=.7, ypos=.75)
    show livro aberto at Position(xpos=.45, ypos=.75)
    with dissolve

    padre "Este livro contém registros antigos da nossa igreja."
    padre "É uma verdadeira relíquia!"
    padre "Alguns dizem que ele guarda segredos sobre o passado do vilarejo."

    hide padre normal
    show livro aberto at Position(xpos=.65, ypos=.75) with move
    show dante at Position(xpos=.35, ypos=.75) with dissolve
    show dante at Position(xpos=.35, ypos=.75) with move

    show dante at Position(xpos=.35, ypos=.95)
    show livro aberto at Position(xpos=.65, ypos=.95)
    with move


    menu:
        "Folhear livro":
            $ historia.incrementar_peso(1)
            $ historia.livro_lido()

            show livro aberto at Position(xpos=.65, ypos=.75)
            show dante at Position(xpos=.35, ypos=.75)
            with move
            play sound "audio/Sound Effects/Objetos/livro_sendo_aberto.mp3" loop volume.75
            show livro aberto at Position(xpos=.64, ypos=.76) with move

            narrador "Dante, curioso, Abriu o livro."

            narrador "Encantado com seu conteúdo, Dante continuou a ler entretido."

            show livro aberto at Position(xpos=.66, ypos=.74) with move

            narrador "Ao aprofundar sua leitura acabou notando nomes de moradores e visitantes."

            narrador "Eventos registrados ao longo dos anos também eram bem descritos, mas nenhum que fosse relevante no imediato."

            show livro aberto at Position(xpos=.65, ypos=.75) with move

            narrador "Algo no livro parecia despertar uma memória distante, mas ele não conseguiu identificar o quê."

            stop sound

        "Não folhear livro":
            pass

    $ renpy.music.set_volume(0.03, channel='music')
    play sound "audio/Sound effects/Objetos/Objeto_caindo_som_forte.mp3" volume.2
    scene igreja-corredor with fade

    show vitoria at Position(xpos=.15, ypos=.75)
    show helena at Position(xpos=.3, ypos=.75)
    show dante at Position(xpos=.5, ypos=.75)
    with dissolve
    show padre at Position(xpos=.85, ypos=.75) with dissolve

    narrador "Enquanto retornavam para o salão principal, um barulho de algo caindo ao chão chamou a atenção de Dante."

    narrador "Parecia vir de uma sala adjacente."

    stop sound

    show padre preocupado at Position(xpos=.85, ypos=.75) with dissolve

    narrador "Dante olhou para o padre, que imediatamente desviou o olhar."

    # show padre at Position(xpos=.85, ypos=.75) with dissolve
    
    hide vitoria normal
    hide helena normal
    with dissolve
    show dante at Position(xpos=.165, ypos=.75) with move

    show dante at Position(xpos=.165, ypos=.95)
    show padre at Position(xpos=.85, ypos=.95)
    with move

    menu:
        "Perguntar sobre barulho":
            $ historia.incrementar_peso(1)

            show dante at Position(xpos=.165, ypos=.75)
            show padre at Position(xpos=.85, ypos=.75)
            with move

            dante "O que foi isso?"

            show padre at Position(xpos=.85, ypos=.75) with dissolve

            padre "Oh, nada de mais."
            padre "Apenas o vento batendo nas janelas. Esta igreja é antiga e eventualmente range."
  
            narrador "Dante não estava totalmente convencido, mas decidiu não insistir."

        "Ignorar barulho":
            pass
    
    show dante at Position(xpos=.165, ypos=.75)
    show padre at Position(xpos=.85, ypos=.75)
    with move

    narrador "O grupo continuou a explorar a igreja até que Padre Iohann sugeriu que visitassem um local especial."

    padre "A vista lá de cima é magnífica."
    padre "Vocês deveriam apreciar."

    show dante at Position(xpos=.165, ypos=.75) with move
    show vitoria at Position(xpos=.35, ypos=.75)
    show helena at Position(xpos=.55, ypos=.75)
    with dissolve
    show padre at Position(xpos=.85, ypos=.75) with move
    show helena at Position(xpos=.55, ypos=.75):
        xzoom -1
    with move

    helena "Vamos lá, a vista é realmente linda."

    show helena at Position(xpos=.55, ypos=.75):
        xzoom 1
    with move

    play sound "audio/Sound effects/Lugares/Escadaria_subida_e_descida.mp3" volume .5 loop
    show helena at Position(xpos=.65, ypos=.75) with move
    hide helena with dissolve
    show vitoria at Position(xpos=.65, ypos=.75) with move
    hide vitoria with dissolve
    show dante at Position(xpos=.65, ypos=.75) with move
    hide dante with dissolve

    $ renpy.music.set_volume(0.01, channel='music')

    scene vista-da-torre:
        xsize 1920
        ysize 1080
    with fade

    show dante at Position(xpos=.67, ypos=.25):
        xzoom -1
    show helena feliz at Position(xpos=.15, ypos=.77)
    show vitoria feliz at Position(xpos=.35, ypos=.75)
    with dissolve

    stop sound

    dante "A vista realmente é de tirar o fólego."
    dante "Mas não consigo parar de pensar que algo estranho está acontecendo aqui, vou lá investigar."

    show helena preocupado at Position(xpos=.15, ypos=.75)
    show vitoria preocupado at Position(xpos=.35, ypos=.75)
    with dissolve

    vitoria "Você não pode ir sozinho Dante."
    vitoria "Vamos descer todos juntos."

    play sound "audio/Sound effects/Lugares/Escadaria_subida_e_descida.mp3" volume 0.5

    $ renpy.music.set_volume(0.04, channel='music')

    scene igreja-corredor with fade
    show padre at Position(xpos=.05, ypos=.1):
        xzoom -1
    show dante at Position(xpos=.35, ypos=.2):
        xzoom -1
    show vitoria at Position(xpos=.55, ypos=.25):
        xzoom -1
    show helena at Position(xpos=.75, ypos=.25):
        xzoom -1
    with dissolve

    stop sound

    padre "Filhos, preciso fazer meus afazeres."
    padre "Teremos que encerrar essa visita, está ficando tarde e logo teremos a missa das sete."

    scene igreja-dentro with fade
    show dante at Position(xpos=.165, ypos=.75)
    show vitoria at Position(xpos=.35, ypos=.75)
    show helena at Position(xpos=.55, ypos=.75)
    show padre at Position(xpos=.85, ypos=.75)
    with dissolve

    padre "Tenho que ajudar também nos preparativos do festival da cidade."
    padre "É um evento muito importante para nós."

    show dante at Position(xpos=.165, ypos=.95)
    show vitoria at Position(xpos=.35, ypos=.95)
    show helena at Position(xpos=.55, ypos=.95)
    show padre at Position(xpos=.85, ypos=.95)
    with move

    menu:
        "Perguntar sobre o festival da cidade":  
            $ historia.incrementar_peso(1)
            
            show dante at Position(xpos=.165, ypos=.75)
            show vitoria at Position(xpos=.35, ypos=.75)
            show helena at Position(xpos=.55, ypos=.75)
            show padre at Position(xpos=.85, ypos=.75)
            with move

            dante "O festival parece ser incrível. O que exatamente você faz para ajudar, Padre Iohann?"

            padre "Na ornamentação e na organização da Missa de Domingo de Ramos. Também coordeno algumas atividades culturais que acontecem durante o festival."

            helena "Isso dá bastante trabalho, principalmente por envolver os ritos antigos."
            helena "Mas o festival é sempre um sucesso, graças a todos os esforços da comunidade."

            dante "Estou ansioso para ver tudo isso de perto. Parece ser um evento muito especial."

            helena "E é mesmo. O festival traz todos juntos, é uma celebração de nossa fé e cultura."

            dante "Se precisar de ajuda, pode contar comigo."

            padre "Agradeço muito, meu filho. Qualquer ajuda é bem-vinda. Espero que aproveite o festival e toda a experiência."

        "Sem interesse sobre":
            show dante at Position(xpos=.165, ypos=.75)
            show vitoria at Position(xpos=.35, ypos=.75)
            show helena at Position(xpos=.55, ypos=.75)
            show padre at Position(xpos=.85, ypos=.75)
            with move
        
            padre "Aguardo pela sua presença, Dante."

    hide dante normal
    hide helena normal
    hide vitoria normal
    with dissolve

    $ renpy.music.play("audio/Sound effects/Lugares/Safe_house_seguro_tranquilo.mp3", loop=True)
    $ renpy.music.set_volume(0.05, channel='music')
    scene centro with dissolve

    show helena at Position(xpos=.35, ypos=.75)
    show vitoria at Position(xpos=.55, ypos=.75)
    show dante at Position(xpos=.75, ypos=.75)
    with dissolve

    narrador "Helena, Vitória e Dante decidiram aproveitar o resto do dia explorando o vilarejo."
    narrador "Mas Dante não conseguia tirar a sensação de estranheza da cabeça."
    narrador "Algo naquela igreja o incomodava."

    helena "O que achou do Padre Iohann? Ele é uma figura interessante, não é?"

    show dante at Position(xpos=.8375, ypos=.95):
        xzoom -1
    show helena at Position(xpos=.15, ypos=.95)
    show vitoria at Position(xpos=.35, ypos=.95)
    with move

    menu:
        "Uma boa pessoa":
            show dante at Position(xpos=.8375, ypos=.75)
            show helena at Position(xpos=.15, ypos=.75)
            show vitoria at Position(xpos=.35, ypos=.75)
            with move

            dante "Sim, muito interessante."
            dante "Gostei de conhece-lo."
        
        "Uma pessoa reservada":
            $ historia.incrementar_peso(1)

            show dante at Position(xpos=.8375, ypos=.75)
            show helena at Position(xpos=.15, ypos=.75)
            show vitoria at Position(xpos=.35, ypos=.75)
            with move


            dante "Sim, muito interessante."
            dante "Há algo nele que me intriga."

    vitoria "Ele é um homem bom!"
    vitoria "Mas também parece carregar um grande fardo."
    vitoria "Acho que há mais nele do que aparenta."

    helena "Está ficando tarde, vamos descansar para amanhã."

    narrador "Todos seguem rumo ao seu local de descanso e tiram o sono merecido depois do dia cansativo."

    hide dante normal
    hide helena normal
    hide vitoria normal
    with dissolve

    scene quarto-helena-noite with fade

    show dante at Position(xpos=.165, ypos=.75) with dissolve
    show dante at Position(xpos=.85, ypos=.75) with move

    narrador "O dia passou rapidamente, e à noite, enquanto estava deitado em sua cama, Dante sonha sobre tudo o que havia visto e ouvido se imaginando em seu quarto."

    $ renpy.music.play("audio/Sound effects/Objetos/Sinos_tocando_vento_batendo_passaros_fundo.mp3", loop=True)
    $ renpy.music.set_volume(0.01, channel='music')

    narrador "Antes de adormecer, ouviu novamente o som dos sinos da igreja, desta vez mais distante, quase como um sussurro."
    narrador "Com um último pensamento sobre as luzes estranhas e o olhar enigmático do Padre Iohann, ele finalmente fechou os olhos."
    narrador "esperando que o dia seguinte trouxesse mais respostas."

    show dante dormindo at Position(xpos=.85, ypos=.75) with dissolve

    menu:
        "Dormir":

            dante "ZzZzZzZz"

    return