label capitulo3:

    play sound "audio/Sound effects/Objetos/Sinos_tocando_vento_batendo_passaros_fundo.mp3" volume 0.1 fadein 1.5

    scene cozinha 

    narrador "O sol ainda estava nascendo quando Dante foi despertado por um som distante de sinos."

    indefinido "..."

    play sound "audio/Sound effects/pessoas/Homem_acordando_alongamento_escandaloso_descansado_cena_descontração.mp3" volume 0.025

    show dante normal at Position(xpos = 0.15, ypos = 0.75) with dissolve

    narrador "Ele se levantou, espreguiçando-se e ouvindo os sons suaves do vilarejo."
    
    stop sound

    play sound "audio/Sound effects/Objetos/Panela_fritando_oléo_quente.mp3" volume 0.05

    narrador "Helena e Vitória já estavam na cozinha, preparando o café da manhã."

    show vitoria normal at posicao_direita_invertido_cap3:
        xzoom -1
    with dissolve

    show helena normal at Position(xpos = 0.5, ypos = 0.25):
        xzoom -1
    with dissolve
    
    helena "Bom dia, Dante! Dormiu bem?"

    menu:
        "Dormi sim, obrigado.":
            dante "Dormi sim, obrigado. O cheiro de café está maravilhoso."

        "Tive uma noite de sono péssima":
            dante "Dormi péssimo. Ao menos o cheiro de café está maravilhoso."

    play sound "audio/Sound effects/pessoas/Pessoa_bebendo_café_xicará_garganta.mp3"

    narrador "Enquanto tomavam café, Helena e Vitória discutiam o plano do dia."

    helena "Pensei em levar você para conhecer a Igreja da Misericórdia e conversar com o Padre Iohann. Ele é uma pessoa fascinante"

    narrador "Dante assentiu, lembrando-se das palavras de Rocha sobre as luzes estranhas. Ele estava curioso para conhecer o Padre Iohann e descobrir mais sobre a igreja que tanto o intrigara."
    narrador "Após o café, o trio seguiu em direção à igreja. O caminho era tranquilo, com poucas pessoas nas ruas, e a brisa fresca da manhã tornava a caminhada agradável."

    stop sound

    scene igreja-dentro with fade

    $ renpy.music.play("audio/Sound effects/Objetos/Celebração_católica_orgão_melodia_completa.mp3", loop=True)
    $ renpy.music.set_volume(0.04, channel='music')

    narrador "Quando chegaram à igreja, Dante ficou impressionado novamente com sua arquitetura."
    narrador "Ao entrarem, foram recebidos pelo som suave do órgão e pelo aroma de incenso."
    narrador "No altar, um homem alto de cabelos negros e olhos cansados estava terminando suas orações."
    narrador "Ao notar a presença dos visitantes, ele se levantou e se aproximou."

    show padre normal at Position(xpos = 0.5, ypos = 0.75) with dissolve

    padre "Bom dia, Helena, Vitória. E você deve ser Dante, o amigo de Helena. Sou o Padre Iohann. Seja bem-vindo à nossa igreja."

    show padre normal at Position(xpos = 0.85, ypos = 0.75) with move
    show vitoria normal at Position(xpos = 0.1, ypos = 0.75)
    show helena normal at Position(xpos = 0.25, ypos = 0.75)
    show dante normal at Position(xpos = 0.40, ypos = 0.75)
    with dissolve

    dante "Muito prazer em conhecê-lo, Padre Iohann. É um lugar lindo."

    padre "Obrigado, meu filho. Esta igreja tem uma história rica, que muitos desconhecem. Espero que possam sentir a paz que ela proporciona."

    hide padre normal with dissolve
    hide dante normal with dissolve
    hide helena normal with dissolve
    hide vitoria normal with dissolve

    narrador "Enquanto conversavam, dois jovens seminaristas se aproximaram, curiosos. Helena os apresentou a Dante."

    show dante normal at Position(xpos = 0.1, ypos = 0.75)
    show helena normal at Position(xpos = 0.3, ypos = 0.75)
    with dissolve

    show icaro normal at Position(xpos = 0.7, ypos = 0.75)
    show augusto normal at Position(xpos = 0.9, ypos = 0.75)
    with dissolve

    helena "Este é Ícaro e aquele é Augusto. Eles estão estudando aqui com o Padre Iohann."

    icaro "Muito prazer. É sempre bom conhecer pessoas novas."

    augusto "Prazer em conhecê-lo."

    narrador "Dante sentiu uma sensação de camaradagem entre os seminaristas e o padre, mas não podia deixar de pensar nas luzes estranhas mencionadas por Rocha."

    hide icaro normal with dissolve
    hide augusto normal with dissolve
    hide dante normal with dissolve
    hide helena normal with dissolve

    # todo aumentar parte

    menu:
        "Perguntar sobre as luzes estranhas":

            show padre normal at Position(xpos = 0.9, ypos = 0.75) with dissolve
            show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve
            show helena normal at Position(xpos = 0.3, ypos = 0.75) with dissolve

            dante "Padre Iohann, ouvimos algumas histórias sobre luzes estranhas perto da igreja. O senhor sabe de algo?"

            narrador "O padre franziu a testa levemente antes de responder, seus olhos se tornando ainda mais profundos e misteriosos."

            padre "Sim, soube dessas histórias. Alguns fiéis relataram ter visto essas luzes, mas não temos nenhuma explicação concreta. Estamos investigando, mas até agora, nada de anormal foi encontrado."

            narrador "Dante notou um leve tremor na mão do padre enquanto ele falava, como se estivesse sendo pressionado a falar de um assunto desagradável"
            # . Helena, tentando aliviar o clima, sugeriu que explorassem a igreja e seu entorno."
            

            hide padre normal with dissolve
            hide dante normal with dissolve
            hide helena normal with dissolve

        "Não perguntar sobre as luzes estranhas":
            pass

    narrador "O grupo caminhou pelos corredores, admirando as obras de arte e as relíquias históricas."

    scene sacristia

    narrador "Ao chegarem à sacristia, notaram um antigo livro de registros, que parecia estar ali há séculos."

    show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve
    show helena normal at Position(xpos = 0.3, ypos = 0.75) with dissolve
    show padre normal at Position(xpos = 0.9, ypos = 0.75) with dissolve

    padre "Este livro contém registros antigos da nossa igreja."
    padre "É uma verdadeira relíquia!"
    padre "Alguns dizem que ele guarda segredos sobre o passado do vilarejo."

    show dante normal at Position(xpos = 0.1, ypos = 0.95)
    show helena normal at Position(xpos = 0.3, ypos = 0.95)
    show padre normal at Position(xpos = 0.9, ypos = 0.95)
    with move

    menu:
        "Folhear livro":
            hide helena normal
            hide padre normal
            with dissolve

            show dante normal at Position(xpos = 0.5, ypos = 0.75) with move
            play sound "audio/Sound Effects/Objetos/livro_sendo_aberto.mp3"

            narrador "Dante, curioso, Abriu o livro."

            narrador "Encantado com seu conteúdo, Dante continuou a ler entretido"

            play sound "audio/Sound Effects/Objetos/livro_sendo_folheado.mp3"

            narrador "Ao aprofundar sua leitura acabou notando nomes de moradores e visitantes"

            narrador "Eventos registrados ao longo dos anos também eram bem descritos, mas nenhum que fosse relevante."

            narrador "Algo no livro parecia despertar uma memória distante, mas ele não conseguiu identificar o quê."

            stop sound

        "Não folhear livro":
            pass

    scene igreja-corredor

    play sound "audio/Sound effects/Objetos/Objeto_caindo_som_forte.mp3" volume .3 loop fadeout 1

    narrador "Enquanto se dirigiam para sair, um barulho de algo caindo ao chão chamou a atenção de Dante."


    narrador "Parecia vir de uma sala adjacente."

    stop sound

    narrador "Ele olhou para o padre, que imediatamente desviou o olhar."

    menu:
        "Perguntar sobre barulho":
            show dante normal at Position(xpos = 0.165, ypos = 0.75) with dissolve

            dante "O que foi isso?"

            show padre normal at Position(xpos = 0.85, ypos = 0.75) with dissolve

            padre "Oh, nada de mais. Apenas o vento batendo nas janelas. Esta igreja é antiga, sabe?"
  
            narrador "Dante não estava totalmente convencido, mas decidiu não insistir."

        "Ignorar barulho":
            pass
    
    narrador "O grupo continuou a explorar a igreja até que Padre Iohann sugeriu uma visita à torre do sino."

    show padre normal at Position(xpos = 0.85, ypos = 0.75) with dissolve

    padre "A vista lá de cima é magnífica."
    padre "Vocês deveriam ver."

    show dante normal at Position(xpos = 0.165, ypos = 0.75) with dissolve
    show vitoria normal at Position(xpos = 0.35, ypos = 0.75) with dissolve
    show helena normal at Position(xpos = 0.55, ypos = 0.75) with dissolve

    helena "Vamos lá, a vista é realmente linda"

    play sound "audio/Sound effects/Lugares/Escadaria_subida_e_descida.mp3" volume .5 loop
    show helena normal at Position(xpos = 0.65, ypos = 0.75) with move
    hide helena normal with dissolve
    show vitoria normal at Position(xpos = 0.65, ypos = 0.75) with move
    hide vitoria normal with dissolve
    show dante normal at Position(xpos = 0.65, ypos = 0.75) with move
    hide dante normal with dissolve

    $ renpy.music.set_volume(0.005, channel='music')

    scene torre-do-sino
    stop sound

    narrador "A escada para a torre era estreita e íngreme."
    narrador "Quando chegaram ao topo, a vista realmente era de tirar o fôlego."
    narrador "O vilarejo parecia um cenário de conto de fadas, cercado por colinas verdejantes e banhado pela luz suave da manhã."
    narrador "Enquanto admiravam a vista, Dante sentiu um arrepio ao lembrar-se das luzes estranhas."
    narrador "Algo naquele lugar parecia fora do comum, e ele estava determinado a descobrir o que era."

    dante "A vista realmente é de tirar o fólego."
    dante "Mas não consigo parar de pensar naquele barulho estranho, vou lá investigar."

    vitoria "Você não pode ir sozinho Dante."
    vitoria "Vamos descer todos juntos."

    play sound "audio/Sound effects/Lugares/Escadaria_subida_e_descida.mp3" volume 0.5

    narrador "Assim desce o grupo unido indo em peso ao causador do barulho."

    scene igreja-dentro

    stop sound
    $ renpy.music.set_volume(0.075, channel='music')
    narrador "Quando desceram, Padre Iohann prostravasse em frente a porta."


    show padre normal at Position(xpos = 0.9, ypos = 0.75) with dissolve
    show vitoria normal at Position(xpos = 0.1, ypos = 0.75) with dissolve
    show helena normal at Position(xpos = 0.25, ypos = 0.75) with dissolve
    show dante normal at Position(xpos = 0.40, ypos = 0.75) with dissolve

    padre "Filhos, preciso fazer meus afazeres."
    padre "teremos que encerrar essa visita, está ficando tarde e logo teremos a missa das sete."
    padre "Tenho que ajudar também nos preparativos do festival da cidade."
    padre "É um evento muito importante para nós."

    menu:
        "Perguntar sobre o festival da cidade":
                dante "O festival parece ser incrível. O que exatamente você faz para ajudar, Padre Iohann?"

                padre "Na ornamentação e na organização da Missa de Domingo de Ramos. Também coordeno algumas atividades culturais que acontecem durante o festival."

                helena "Isso deve ser bastante trabalho."
                helena "Mas o festival é sempre um sucesso, graças a todos os esforços da comunidade."

                dante "Estou ansioso para ver tudo isso de perto. Parece ser um evento muito especial."

                helena "E é mesmo. O festival traz todos juntos, é uma celebração de nossa fé e cultura."

                dante "Se precisar de ajuda, pode contar comigo."

                padre "Agradeço muito, meu filho. Qualquer ajuda é bem-vinda. Espero que aproveite o festival e toda a experiência."

        "Não perguntar sobre o festival da cidade":
            padre "Aguardo pela sua presença, Dante."

    hide padre normal with dissolve
    hide dante normal with dissolve
    hide helena normal with dissolve
    hide vitoria normal with dissolve

    $ renpy.music.play("audio/Capitulos/Capitulo 3 - inicio dos sinais de cansaço.mp3", loop=True)
    $ renpy.music.set_volume(0.2, channel='music')

    scene centro

    narrador "Helena, Vitória e Dante decidiram aproveitar o resto do dia explorando o vilarejo."

    narrador "Mas Dante não conseguia tirar a sensação de estranheza da cabeça."

    narrador "Algo naquela igreja o incomodava."

    narrador "Enquanto caminhavam de volta para a praça principal, Helena virou-se para Dante e disse:" #aqui

    show helena normal at Position(xpos = 0.3, ypos = 0.75) with dissolve
    show dante normal at Position(xpos = 0.8, ypos = 0.75) with dissolve

    helena "O que achou do Padre Iohann? Ele é uma figura interessante, não é?"

    show dante normal at Position(xpos = 0.8375, ypos = 0.75):
        xzoom -1
    with dissolve

    menu:
        "Gostou de conhece-lo":
            dante "Sim, muito interessante."
            dante "Gostei de conhece-lo"
        
        "Achou evasivo":
            dante "Sim, muito interessante."
            dante "Há algo nele que me intriga."

    show vitoria normal at Position(xpos = 0.1, ypos = 0.75) with dissolve

    vitoria "Ele é um homem bom!"
    vitoria "Mas também parece carregar um grande fardo"
    vitoria "Acho que há mais nele do que aparenta."

    helena "Está ficando tarde, vamos descansar para amanhã"

    narrador "Todos seguem rumo ao seu local de descanso e tiram o sono merecido depois do dia cansativo"

    hide dante normal with dissolve
    hide helena normal with dissolve
    hide vitoria normal with dissolve

    scene quarto-helena-noite

    show dante normal at Position(xpos=.15, ypos=.75) with dissolve
    show dante normal at Position(xpos=.85, ypos=.75) with move

    narrador "O dia passou rapidamente, e à noite, enquanto estava deitado em sua cama, Dante sonha sobre tudo o que havia visto e ouvido se imaginando em seu quarto."

    $ renpy.music.play("audio/Sound effects/Objetos/Sinos_tocando_vento_batendo_passaros_fundo.mp3", loop=True)
    $ renpy.music.set_volume(0.02, channel='music')


    narrador "Antes de adormecer, ouviu novamente o som dos sinos da igreja, desta vez mais distante, quase como um sussurro."

    narrador "Com um último pensamento sobre as luzes estranhas e o olhar enigmático do Padre Iohann, ele finalmente fechou os olhos, esperando que o dia seguinte trouxesse mais respostas, e talvez, mais perguntas."

    menu:
        "Dormir":
            dante "ZzZzZzZz"

    return