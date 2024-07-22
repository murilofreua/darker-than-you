label capitulo3:

    scene cozinha 

    play sound "audio/sino_vento.mp3"

    narrador "O sol ainda estava nascendo quando Dante foi despertado por um som distante de sinos."

    stop sound

    play sound "audio/Waking_Up.mp3"

    show dante normal at Position(xpos = 0.15, ypos = 0.75) with dissolve

    narrador "Ele se levantou, espreguiçando-se e ouvindo os sons suaves do vilarejo."
    
    stop sound

    narrador "Helena e Vitória já estavam na cozinha, preparando o café da manhã."

    play sound "audio/Barulho_de_óleo_fritando.mp3"

    show helena normal at Position(xpos = 0.65, ypos = 0.75) with dissolve
    show vitoria normal at Position(xpos = 0.9, ypos = 0.75) with dissolve
    
    helena "Bom dia, Dante! Dormiu bem?"

    menu:
        "Dormi sim, obrigado.":
            dante "Dormi sim, obrigado. O cheiro de café está maravilhoso."

        "Tive uma noite de sono péssima":
            dante "Dormi péssimo. Ao menos o cheiro de café está maravilhoso."

    play sound "audio/bebendo café.mp3"

    narrador "Enquanto tomavam café, Helena e Vitória discutiam o plano do dia."

    helena "Pensei em levar você para conhecer a Igreja da Misericórdia e conversar com o Padre Iohann. Ele é uma pessoa fascinante"

    stop sound

    narrador "Dante assentiu, lembrando-se das palavras de Rocha sobre as luzes estranhas. Ele estava curioso para conhecer o Padre Iohann e descobrir mais sobre a igreja que tanto o intrigara."

    narrador "Após o café, o trio seguiu em direção à igreja. O caminho era tranquilo, com poucas pessoas nas ruas, e a brisa fresca da manhã tornava a caminhada agradável."

    scene igreja-dentro

    narrador "Quando chegaram à igreja, Dante ficou impressionado novamente com sua arquitetura."

    narrador "A fachada barroca estava decorada com detalhes intrincados, e os vitrais coloridos refletiam a luz do sol, criando um espetáculo de cores."

    narrador "Ao entrarem, foram recebidos pelo som suave do órgão e pelo aroma de incenso. No altar, um homem alto de cabelos negros e olhos cansados estava terminando suas orações. Ao notar a presença dos visitantes, ele se levantou e se aproximou."

    show padre normal at Position(xpos = 0.9, ypos = 0.75) with dissolve

    padre "Bom dia, Helena, Vitória. E você deve ser Dante, o amigo de Helena. Sou o Padre Iohann. Seja bem-vindo à nossa igreja."

    show vitoria normal at Position(xpos = 0.1, ypos = 0.75) with dissolve
    show helena normal at Position(xpos = 0.25, ypos = 0.75) with dissolve
    show dante normal at Position(xpos = 0.40, ypos = 0.75) with dissolve

    dante "Muito prazer em conhecê-lo, Padre Iohann. É um lugar lindo."

    padre "Obrigado, meu filho. Esta igreja tem uma história rica, que muitos desconhecem. Espero que possam sentir a paz que ela proporciona."

    hide padre normal with dissolve
    hide dante normal with dissolve
    hide helena normal with dissolve
    hide vitoria normal with dissolve

    narrador "Enquanto conversavam, dois jovens seminaristas se aproximaram, curiosos. Helena os apresentou a Dante."

    show helena normal at Position(xpos = 0.7, ypos = 0.75) with dissolve
    show dante normal at Position(xpos = 0.9, ypos = 0.75) with dissolve

    show icaro normal at Position(xpos = 0.1, ypos = 0.75) with dissolve
    show augusto normal at Position(xpos = 0.3, ypos = 0.75) with dissolve

    helena "Este é Ícaro e aquele é Augusto. Eles estão estudando aqui com o Padre Iohann."

    icaro "Muito prazer. É sempre bom conhecer pessoas novas."

    augusto "Prazer em conhecê-lo."

    narrador "Dante sentiu uma sensação de camaradagem entre os seminaristas e o padre, mas não podia deixar de pensar nas luzes estranhas mencionadas por Rocha."

    hide icaro normal with dissolve
    hide augusto normal with dissolve
    hide dante normal with dissolve
    hide helena normal with dissolve

    menu:
        "Perguntar sobre as luzes estranhas":

            show padre normal at Position(xpos = 0.9, ypos = 0.75) with dissolve
            show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve
            show helena normal at Position(xpos = 0.3, ypos = 0.75) with dissolve

            dante "Padre Iohann, ouvimos algumas histórias sobre luzes estranhas perto da igreja. O senhor sabe de algo?"

            narrador "O padre franziu a testa levemente antes de responder, seus olhos se tornando ainda mais profundos e misteriosos."

            padre "Sim, soube dessas histórias. Alguns fiéis relataram ter visto essas luzes, mas não temos nenhuma explicação concreta. Estamos investigando, mas até agora, nada de anormal foi encontrado."

            narrador "Dante notou um leve tremor na mão do padre enquanto ele falava. Helena, tentando aliviar o clima, sugeriu que explorassem a igreja e seu entorno."

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

    padre "Este livro contém registros antigos da nossa igreja. É uma verdadeira relíquia. Alguns dizem que ele guarda segredos sobre o passado do vilarejo."

    menu:
        "Folhear livro":
            narrador "Dante, curioso, folheou algumas páginas, notando nomes e eventos registrados ao longo dos anos."

            narrador "Algo no livro parecia despertar uma memória distante, mas ele não conseguiu identificar o quê."
        "Não folhear livro":
            pass

    scene corredor

    # SOM DE VENTO

    narrador "Enquanto se dirigiam para sair, um barulho suave, quase imperceptível, chamou a atenção de Dante. Parecia vir de uma sala adjacente. Ele olhou para o padre, que imediatamente desviou o olhar."

    menu:
        "Perguntar sobre barulho":
            show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve

            dante "O que foi isso?"

            show padre normal at Position(xpos = 0.9, ypos = 0.75) with dissolve

            padre "Oh, nada de mais. Apenas o vento batendo nas janelas. Esta igreja é antiga, sabe?"
  
            narrador "Dante não estava totalmente convencido, mas decidiu não insistir."

        "Ignorar barulho":
            pass

    narrador "O grupo continuou a explorar a igreja até que Padre Iohann sugeriu uma visita à torre do sino."

    show helena normal at Position(xpos = 0.3, ypos = 0.75) with dissolve
    show vitoria normal at Position(xpos = 0.5, ypos = 0.75) with dissolve

    padre "A vista lá de cima é magnífica. Vocês deveriam ver."

    narrador "A escada para a torre era estreita e íngreme."

    scene torre-do-sino
    # Som de vendo com um pouco de barulho de povoado

    narrador "Quando chegaram ao topo, a vista realmente era de tirar o fôlego. O vilarejo parecia um cenário de conto de fadas, cercado por colinas verdejantes e banhado pela luz suave da manhã."

    narrador "Enquanto admiravam a vista, Dante sentiu um arrepio ao lembrar-se das luzes estranhas."

    narrador "Algo naquele lugar parecia fora do comum, e ele estava determinado a descobrir o que era."

    scene igreja-dentro

    narrador "Quando desceram, Padre Iohann se despediu do grupo, dizendo que precisava atender a alguns afazeres."

    show padre normal at Position(xpos = 0.9, ypos = 0.75) with dissolve
    show vitoria normal at Position(xpos = 0.1, ypos = 0.75) with dissolve
    show helena normal at Position(xpos = 0.25, ypos = 0.75) with dissolve
    show dante normal at Position(xpos = 0.40, ypos = 0.75) with dissolve

    padre "Tenho que ajudar nos preparativos do festival da cidade. É um evento muito importante para nós."

    menu:
        "Perguntar sobre o festival da cidade":
                dante "O festival parece ser incrível. O que exatamente você faz para ajudar, Padre Iohann?"

                padre "Na ornamentação e na organização da Missa de Domingo de Ramos. Também coordeno algumas atividades culturais que acontecem durante o festival."

                vitoria "Isso deve ser bastante trabalho. Mas o festival é sempre um sucesso, graças a todos os esforços da comunidade."

                dante "Estou ansioso para ver tudo isso de perto. Parece ser um evento muito especial."

                helena "E é mesmo. O festival traz todos juntos, é uma celebração de nossa fé e cultura."

                menu:
                    "Sugerir ajuda":
                            dante "Se precisar de ajuda, pode contar comigo."

                            padre "Agradeço muito, meu filho. Qualquer ajuda é bem-vinda. Espero que aproveite o festival e toda a experiência."
                    
                    "Não sugerir ajuda":
                        pass

        "Não perguntar sobre o festival da cidade":
            pass

    hide padre normal with dissolve
    hide dante normal with dissolve
    hide helena normal with dissolve
    hide vitoria normal with dissolve

    scene centro

    narrador "Helena, Vitória e Dante decidiram aproveitar o resto do dia explorando o vilarejo."

    narrador "Mas Dante não conseguia tirar a sensação de estranheza da cabeça."

    narrador "Algo naquela igreja o incomodava."

    narrador "Enquanto caminhavam de volta para a praça principal, Helena virou-se para Dante e disse:"

    show helena normal at Position(xpos = 0.3, ypos = 0.75) with dissolve
    show dante normal at Position(xpos = 0.8, ypos = 0.75) with dissolve

    helena "O que achou do Padre Iohann? Ele é uma figura interessante, não é?"

    menu:
        "Sim, muito interessante. Há algo nele que me intriga.":
            dante "Sim, muito interessante. Há algo nele que me intriga."
        "Sim, muito interessante. Gostei de conhece-lo":
            dante "Sim, muito interessante. Gostei de conhece-lo"

    show vitoria normal at Position(xpos = 0.1, ypos = 0.75) with dissolve

    vitoria "Ele é um homem bom, mas também parece carregar um grande fardo. Acho que há mais nele do que aparenta."

    scene quarto-dante

    narrador "O dia passou rapidamente, e à noite, enquanto estava deitado em sua cama, Dante refletia sobre tudo o que havia visto e ouvido."

    play sound "audio/sino_vento.mp3"

    narrador "Antes de adormecer, ouviu novamente o som dos sinos da igreja, desta vez mais próximo, quase como um sussurro."

    stop sound

    narrador "Com um último pensamento sobre as luzes estranhas e o olhar enigmático do Padre Iohann, ele finalmente fechou os olhos, esperando que o dia seguinte trouxesse mais respostas, e talvez, mais perguntas."

    menu:
        "Dormir":
            dante "ZzZzZzZz"

    return