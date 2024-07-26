label capitulo6:

    scene area-secreta

    narrador "A área secreta é um espaço oculto e enigmático, com paredes de pedra e símbolos antigos gravados."
    
    narrador "O ambiente é sombrio e úmido, com a única iluminação vindo de lanternas que Dante e Vitória carregam."
    
    show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve
    show vitoria normal at Position(xpos = 0.9, ypos = 0.75) with dissolve

    dante "Esses símbolos... são muito antigos. Precisamos ter cuidado."
    
    vitoria "Sim, algo me diz que este lugar guarda muitos segredos."

    menu:
        "Encontrar vestígios do ritual (Confiança Alta)":

            narrador "Eles encontram vestígios do ritual e evidências de que Helena foi levada para este local."
            
            narrador "A atmosfera é de mistério e revelação, com a sensação de que algo grandioso está prestes a ser desvendado."
            
            dante "Isso confirma que Helena esteve aqui."
            
            dante "Precisamos encontrar mais pistas."
            
            vitoria "Olhe aqui, Dante. Parece um fragmento de um antigo manuscrito. Pode ser importante."

        "Encontrar sinais de um ritual interrompido (Confiança Baixa)":

            narrador "Eles encontram sinais de um ritual interrompido e evidências de que Helena foi levada de forma abrupta."
            
            narrador "A tensão aumenta, e o ambiente parece carregar uma sensação de urgência e perigo iminente."
            
            dante "Parece que Helena foi levada rapidamente."
            
            dante "Precisamos agir rápido!"
            
            vitoria "Veja estas marcas no chão. Alguém estava tentando completar algo aqui, mas foi interrompido."

    hide dante normal with dissolve
    hide vitoria normal with dissolve

    narrador "Dante e Vitória deixam a área secreta e vão em direção ao local onde o relicário pode estar escondido."

    narrador "O caminho é desolado e cheio de sombras, com árvores retorcidas e o vento assobiando de forma sinistra."

    # scene investigacao-biblioteca

    narrador "A biblioteca parece mais sombria do que antes, com as sombras das estantes se alongando e criando um ambiente inquietante."
    
    narrador "Livros sobre práticas ocultas estão espalhados sobre a mesa, cobertos por uma fina camada de poeira."

    show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve
    show vitoria normal at Position(xpos = 0.9, ypos = 0.75) with dissolve

    dante "Precisamos encontrar algo que nos dê uma pista definitiva."

    vitoria "Vou verificar os registros históricos, talvez haja algo que nos ajude."

    menu:
        "Consultar registros históricos (Confiança Alta)":

            $ historia.incrementar_peso(1)

            narrador "Eles encontram um registro detalhado sobre o relicário e o ritual."
            
            narrador "A descoberta é significativa e os leva a uma nova pista sobre o local de realização do ritual."
            
            dante "Isso é exatamente o que precisávamos."
            
            dante "Temos uma nova pista sobre onde o ritual pode ter ocorrido."
            
            vitoria "Aqui está, um mapa antigo que mostra a localização exata. Vamos!"

        "Conversar com moradores antigos (Confiança Baixa)":

            narrador "Eles obtêm relatos fragmentados sobre o relicário e sua importância histórica, levando a uma busca mais intensa por informações."
            
            dante "As informações são vagas, mas ainda podem ser úteis."
            
            dante "Precisamos continuar investigando!"
            
            vitoria "Um dos moradores mencionou um local antigo na cidade. Pode ser nosso próximo destino."

    hide dante normal with dissolve
    hide vitoria normal with dissolve

    narrador "A busca os leva a investigar um local abandonado na cidade, onde eles esperam encontrar mais pistas."

    # scene local-abandonado

    narrador "O local é um edifício antigo e deteriorado, com janelas quebradas e paredes cobertas de mofo."
    
    narrador "A atmosfera é opressiva, com a sensação de que algo sombrio aconteceu ali."

    show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve
    show vitoria normal at Position(xpos = 0.9, ypos = 0.75) with dissolve

    dante "Este lugar me dá arrepios. Precisamos ser rápidos."

    vitoria "Concordo. Vamos procurar qualquer coisa que possa nos levar para a Helena."

    menu:
        "Encontrar o relicário (Confiança Alta)":
            narrador "Eles encontram o relicário e uma série de documentos revelando o motivo do ritual."
            
            narrador "A tensão dá lugar a uma sensação de alívio e realização."
            
            dante "Finalmente, encontramos o relicário."
            
            dante "Agora podemos entender o que está acontecendo."
            
            vitoria "Esses documentos são cruciais. Precisamos estudá-los com cuidado."

            narrador "Enquanto estudam os documentos, eles encontram uma pista crucial sobre o paradeiro de Helena."
            
            dante "Olhe isso, Vitória. Este símbolo... é o mesmo que vimos na área secreta."
            
            vitoria "Isso significa que Helena pode estar em algum lugar próximo a essa área."
            
            dante "Precisamos voltar e procurar mais detalhadamente."

            narrador "Com a nova pista, eles se preparam para retornar à área secreta com a esperança renovada de encontrar Helena."

            narrador "Enquanto se movem pelo local, eles encontram uma passagem secreta escondida atrás de uma parede deteriorada."
            
            dante "Vitória, veja isso! Uma passagem secreta. Pode nos levar a algo importante."
            
            vitoria "Vamos, não temos tempo a perder."

            narrador "Eles seguem pela passagem, sentindo que estão cada vez mais perto de descobrir o paradeiro de Helena."

        "Descobrir vestígios do ritual (Confiança Baixa)":

            $ historia.incrementar_peso(1)

            narrador "Eles encontram apenas fragmentos do ritual e pistas sobre o possível paradeiro de Helena."
            
            narrador "A sensação de frustração e desespero cresce."
            
            dante "Ainda não é o que esperávamos!"
            
            dante "Precisamos de mais pistas para encontrar Helena!"
            
            vitoria "Não vamos desistir. Cada pista nos aproxima mais."

            narrador "Enquanto continuam procurando, eles encontram uma passagem secreta escondida atrás de uma parede deteriorada."
            
            dante "Vitória, veja isso! Uma passagem secreta. Pode nos levar a algo importante."
            
            vitoria "Vamos, não temos tempo a perder."

            narrador "Eles seguem pela passagem, sentindo que estão cada vez mais perto de descobrir o paradeiro de Helena."

    hide dante normal with dissolve
    hide vitoria normal with dissolve

    narrador "Dante e Vitória se aproximam da passagem secreta, seus corações batendo acelerados com a expectativa."
    
    narrador "A passagem é estreita e escura, com paredes úmidas e o som de gotejamento ecoando ao longe."
    
    narrador "Eles se preparam para seguir adiante, determinados a descobrir os mistérios que os aguardam no final desse caminho sombrio."

    return
