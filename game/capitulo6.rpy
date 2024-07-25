label capitulo6:

    # scene area-secreta

    narrador "A área secreta é um espaço oculto e enigmático, com paredes de pedra e símbolos antigos gravados."

    narrador " O ambiente é sombrio e úmido, com a única iluminação vindo de lanternas que Dante e Vitória carregam."

    show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve
    show vitoria normal at Position(xpos = 0.9, ypos = 0.75) with dissolve

    menu:
        "Encontrar vestígios do ritual (Confiança Alta)":
            narrador "Eles encontram vestígios do ritual e evidências de que Helena foi levada para este local."

            narrador "A atmosfera é de mistério e revelação, com a sensação de que algo grandioso está prestes a ser desvendado."

            dante "Isso confirma que Helena esteve aqui."

            dante "Precisamos encontrar mais pistas."

        "Encontrar sinais de um ritual interrompido (Confiança Baixa)":

            narrador "Eles encontram sinais de um ritual interrompido e evidências de que Helena foi levada de forma abrupta."
            
            narrador " A tensão aumenta, e o ambiente parece carregar uma sensação de urgência e perigo iminente."

            dante "Parece que Helena foi levada rapidamente."

            dante "Precisamos agir rápido!"

    hide dante normal with dissolve
    hide vitoria normal with dissolve

    narrador "Dante e Vitória deixam a área secreta e vão em direção ao local onde o relicário pode estar escondido."

    narrador "O caminho é desolado e cheio de sombras."

    # scene investigacao-biblioteca

    narrador "A biblioteca parece mais sombria do que antes, com as sombras das estantes se alongando e criando um ambiente inquietante."

    narrador "Livros sobre práticas ocultas estão espalhados sobre a mesa."

    show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve
    show vitoria normal at Position(xpos = 0.9, ypos = 0.75) with dissolve

    menu:
        "Consultar registros históricos (Confiança Alta)":

            narrador "Eles encontram um registro detalhado sobre o relicário e o ritual."

            narrador "A descoberta é significativa e os leva a uma nova pista sobre o local de realização do ritual."

            dante "Isso é exatamente o que precisávamos."

            dante "Temos uma nova pista sobre onde o ritual pode ter ocorrido."

        "Conversar com moradores antigos (Confiança Baixa)":

            narrador "Eles obtêm relatos fragmentados sobre o relicário e sua importância histórica, levando a uma busca mais intensa por informações."

            dante "As informações são vagas, mas ainda podem ser úteis."

            dante "Precisamos continuar investigando!"

    hide dante normal with dissolve
    hide vitoria normal with dissolve

    narrador "A busca os leva a investigar um local abandonado na cidade, onde eles esperam encontrar mais pistas."

    # scene local-abandonado

    narrador "O local é um edifício antigo e deteriorado, com janelas quebradas e paredes cobertas de mofo."

    narrador "A atmosfera é opressiva, com a sensação de que algo sombrio aconteceu ali."

    show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve
    show vitoria normal at Position(xpos = 0.9, ypos = 0.75) with dissolve

    menu:
        "Encontrar o relicário (Confiança Alta)":
            narrador "Eles encontram o relicário e uma série de documentos revelando o motivo do ritual."

            narrador "A tensão dá lugar a uma sensação de alívio e realização."

            dante "Finalmente, encontramos o relicário."

            dante "Agora podemos entender o que está acontecendo."

        "Descobrir vestígios do ritual (Confiança Baixa)":
            narrador "Eles encontram apenas fragmentos do ritual e pistas sobre o possível paradeiro de Helena."

            narrador "A sensação de frustração e desespero cresce."

            dante "Ainda não é o que esperávamos!"

            dante "Precisamos de mais pistas para encontrar Helena!"

    hide dante normal with dissolve
    hide vitoria normal with dissolve

    narrador "A investigação os leva ao confronto final, onde todas as peças se encaixam."

    return
