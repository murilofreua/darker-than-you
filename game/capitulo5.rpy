label capitulo5:
    
    scene igreja-fora-dia

    narrador "Dante começa a investigação no dia seguinte ao desaparecimento de Helena."

    narrador "O ambiente é carregado de tensão e mistério, refletindo a gravidade da situação."

    narrador "A igreja está envolta em névoa matinal, com a luz do sol filtrando-se através das janelas de vitrais coloridos."

    narrador "O ambiente é silencioso, exceto pelo som distante dos sinos."

    narrador " Dante entra com um olhar determinado, observando a tranquilidade aparente que contrasta com a urgência de sua missão."

    narrador "Dante se dirige ao escritório do Padre Iohann, a luz do dia gradualmente se intensifica conforme ele avança."

    scene escritorio-padre

    narrador "O escritório é um espaço acolhedor, mas com uma atmosfera pesada."

    narrador "Livros antigos estão empilhados em prateleiras de madeira escura, e um crucifixo pendurado na parede parece observar tudo."
    
    show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve

    show padre normal at Position(xpos = 0.9, ypos = 0.75) with dissolve

    narrador "O Padre Iohann está sentado atrás de uma mesa, sua expressão é de preocupação, misturada com uma leve tensão."

    menu:
        "Perguntar diretamente sobre Helena (Confiança Alta)":

            $ historia.incr_peso_bom()

            dante "Padre Iohann, você viu Helena esta manhã?"

            narrador "O Padre Iohann, visivelmente aliviado, se oferece para ajudar."

            padre "Sim, a vi mais cedo. Ela disse que ia ajudar na montagem da procissão."

            padre "Ícaro e Augusto podem ter visto algo. Procure os seminaristas na sala ao lado."

        "Perguntar diretamente sobre Helena (Confiança Baixa)":
            dante "Padre Iohann, você viu Helena esta manhã?"

            narrador "O Padre se mostra evasivo e desinteressado, desviando o olhar e dando respostas vagas."

            padre "Hum... não tenho certeza. Talvez ela esteja por aí ajudando."

            narrador "Dante percebe uma sensação de desconforto, levando-o a procurar pistas por conta própria."

    hide dante normal with dissolve

    hide padre normal with dissolve

    narrador "Dante deixa o escritório, passando pelos corredores da igreja que parecem ainda mais sombrios, refletindo sua crescente desconfiança."

    scene sala-dos-seminaristas

    show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve

    narrador "A sala é modesta, com bancos de madeira e mesas dispostas em linha."

    show icaro normal at Position(xpos = 0.7, ypos = 0.75) with dissolve
    show augusto normal at Position(xpos = 0.9, ypos = 0.75) with dissolve

    narrador "Ícaro e Augusto estão ocupados com seus estudos, a luz suave das lâmpadas cria um ambiente introspectivo."

    menu:
        "Perguntar sobre a noite do desaparecimento":

            $ historia.incr_peso_bom()

            dante "Vocês viram algo na noite em que Helena desapareceu?"

            icaro "Eu ouvi murmúrios e vi uma figura encapuzada. Foi muito estranho."

            augusto "Eu vi uma sombra estranha que se movia rapidamente. Parecia... fora do comum."

        "Questionar sobre o Padre Iohann":

            dante "Vocês notaram algo estranho no comportamento do Padre Iohann?"

            icaro "Ele tem estado mais reservado ultimamente. Algo parece incomodá-lo."

            augusto "Sim, notei que ele anda mais introspectivo e preocupado. Ele costumava ser mais acessível, mas agora parece evitar conversas longas."

            icaro "Recentemente, vi ele saindo da igreja tarde da noite, o que é bem incomum. Ele parecia estar carregando algo, mas não consegui ver o que era."

            augusto "E tem aquelas reuniões misteriosas que ele tem tido no escritório. Ele sempre tranca a porta e ninguém sabe com quem ele está falando."

            icaro "A atmosfera ao redor dele mudou. É como se ele estivesse carregando um grande fardo."

            augusto "Talvez esteja relacionado ao desaparecimento de Helena. Pode ser que ele saiba mais do que está nos contando."

            icaro "Nós também ouvimos alguns sussurros e passos estranhos vindo do escritório dele nas últimas noites."

            augusto "Algo definitivamente não está certo. Precisamos ficar atentos e talvez investigar um pouco mais por conta própria."

    narrador "Dante se despede dos seminaristas e se dirige para a casa de Seu Pedro, passando por ruas que parecem mais escuras e silenciosas."

    hide icaro normal with dissolve
    hide augusto normal with dissolve
    hide dante normal with dissolve

    scene casa-pedro

    narrador "A casa é simples e acolhedora, com móveis antigos e uma atmosfera de nostalgia."

    show pedro normal at Position(xpos = 0.8, ypos = 0.75) with dissolve

    narrador "Seu Pedro está sentado à mesa, com um olhar preocupado, rodeado por velhas fotografias e lembranças."

    menu:
        "Perguntar sobre o relicário":
            dante "Seu Pedro, você sabe algo sobre o relicário que Helena estava interessada?"

            pedro "Ela estava obcecada com uma lenda sobre o relicário. Acreditava que ele tinha um grande poder."
            
            narrador "O ambiente se torna carregado de suspense, com Dante recebendo uma nova pista para investigar."

        "Perguntar sobre sombras estranhas":
            dante "Você viu algo estranho ultimamente, como sombras ou figuras encapuzadas?"

            pedro "Sim, vi uma sombra nas proximidades recentemente. Algo parecia fora do comum."

            narrador "O ambiente parece cada vez mais opressor."

    hide pedro normal with dissolve

    narrador "Dante se despede e se dirige à biblioteca da igreja, refletindo sobre as novas pistas e o crescente senso de urgência."

    scene biblioteca-noite

    narrador "A biblioteca é um local de silêncio absoluto, com estantes repletas de livros antigos."

    narrador "A luz da tarde filtra-se através das janelas, criando um jogo de luz e sombra que aumenta o mistério."

    show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve

    menu:
        "Investigar livros antigos (Confiança Alta)":

            $ historia.incr_peso_bom()

            narrador "Dante encontra um livro sobre o relicário e rituais antigos, descobrindo uma referência a uma área secreta na igreja."

            dante "Isso pode ser importante. Preciso investigar essa área secreta."

        "Investigar livros antigos (Confiança Baixa)":
            narrador "Dante encontra um livro sobre lendas antigas, sugerindo uma conexão com práticas ocultas."

            dante "Isso está ficando cada vez mais estranho. Preciso ter cuidado."

    narrador "Dante se prepara para explorar a área secreta mencionada no livro, o ambiente se tornando mais sombrio e carregado de tensão."

    hide dante normal with dissolve

    return