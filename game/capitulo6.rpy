label capitulo6:

    scene casa-helena
    show vitoria at Position(xpos=.75, ypos=.25):
        xzoom -1
    show dante at Position(xpos=.95, ypos=.20):
        xzoom -1
    with dissolve

    show vitoria at Position(xpos=.45, ypos=.25)
    show dante at Position(xpos=.55, ypos=.20)
    with move 

    show vitoria at Position(xpos=.05, ypos=.25) with move

    narrador "Chegando na porta da casa de Helena, Dante para, descidido a nao deixar Helena perdida mais uma noite"

    show vitoria preocupado at Position(xpos=.05, ypos=.25):
        xzoom 1
    with dissolve

    vitoria "Você não vai sozinho garoto, se for fazer alguma idiotice, faremos juntos por nossa amiga."

    dante "Então parece que seremos idiotas juntos"

    vitoria "Otimo, apenas eu sei o caminho mesmo"

    #scene area-secreta-noite with fade
    scene area-secreta with fade
    show luzes at Position(xpos=.75, ypos=.6)

    narrador "A área secreta é um espaço oculto e enigmático, com paredes de pedra e símbolos antigos gravados."
    narrador "O ambiente é sombrio, com a única iluminação vindo da lua."
    
    show dante at Position(xpos = 0.3, ypos = 0.2):
        xzoom 1
    show vitoria at Position(xpos = 0.15, ypos = 0.75)
    with dissolve

    dante "Esses símbolos... são muito antigos. Precisamos ter cuidado."
    
    vitoria "Sim, algo me diz que este lugar guarda muitos segredos."
    narrador "Eles encontram vestígios de um ritual envolvendo uma chama flutuante e uma porta logo ao fundo, com manchas no chão em sua direção."

    menu:
        "Verificar chama primeiro":

            narrador "A atmosfera é de mistério e revelação, com a sensação de que algo grandioso está prestes a ser desvendado."
            
            dante "Isso confirma que Helena esteve aqui."
            
            vitoria "Não, apenas que algo aconteceu aqui"

            dante "Verdade, me desculpe, precisamos encontrar mais pistas."
            
            vitoria "Olhe aqui, Dante. Essa porta parece ter sido aberta recentemente. Pode significar algo."

            narrador "O local é um edifício antigo e deteriorado, com janelas quebradas e paredes cobertas de mofo."


        "Verificar sala primeiro":
            $ historia.incrementar_peso(1)

            narrador "A tensão aumenta, e o ambiente parece carregar uma sensação de urgência e perigo iminente."
            
            dante "Essa chama é suspeira mas sinto que ela não nos ajudará a encontra nossa amiga."

            vitoria "Concordo. Vamos procurar qualquer coisa que possa nos levar para a Helena."
            
            vitoria "Veja estas marcas no chão. algo foi arrastado aqui."

            dante "Vou abrir essa porta, para trás!"
    
    scene local-abandonado with fade
    show helena dormindo at Position(xpos=.15, ypos=.75)
    narrador "A atmosfera é opressiva, com a sensação de que algo sombrio aconteceu ali."
    narrador "Helena é encontrada no chão"

    show dante at Position(xpos=.65, ypos=.2):
        xzoom -1
    show vitoria at Position(xpos=.8, ypos=.25):
        xzoom -1
    with dissolve

    dante "Helena!!..."

    show dante at Position(xpos=.25, ypos=.2)
    show vitoria at Position(xpos=.4, ypos=.25)
    with move

    indefinido ""

    return
