
label capitulo4:

    scene igreja-fora-dia with fade

    narrador "Os dias que antecedem o festival são intensos e cheios de atividades."

    narrador "Dante, Helena e Vitória se voluntariam para ajudar nos preparativos, e o vilarejo fervilha de excitação."

    narrador "A praça principal se transforma em um colorido cenário festivo, com bandeirolas, barracas de comida e atividades sendo organizadas."

    narrador "Na manhã do primeiro dia de preparativos, Dante se encontra com Padre Iohann na igreja."

    show dante normal at Position(xpos = 0.15, ypos = 0.75) with dissolve
    show padre normal at Position(xpos = 0.9, ypos = 0.75) with dissolve
    
    padre "Bom dia, Dante. Estamos muito agradecidos por sua ajuda com o festival."

    dante "Estou feliz em ajudar, Padre Iohann. O que precisa ser feito?"

    padre "Temos muitas coisas para organizar."

    padre "As barracas de comida, as decorações da praça, e precisamos preparar a procissão."

    padre "Qualquer coisa que você possa fazer será de grande valor."

    hide padre normal with dissolve
    hide dante normal with dissolve

    # scene festival-dia with dissolve

    narrador "Dante, Helena e Vitória se envolvem nas tarefas, conhecendo mais moradores do vilarejo durante o processo."

    narrador "Isabel, Sofia e Seu Pedro estão todos presentes, contribuindo de diferentes maneiras para os preparativos."

    show dante normal at Position(xpos = 0.15, ypos = 0.75) with dissolve
    show isabel normal at Position(xpos = 0.9, ypos = 0.75) with dissolve

    dante "Este festival é realmente importante para todos aqui, não é?"

    isabel "Sim, é a alma da nossa cidade. Ele une todos nós e mantém viva a nossa história."

    hide isabel normal with dissolve

    show sofia normal at Position(xpos = 0.9, ypos = 0.75) with dissolve

    sofia "Dante, você sabia que o festival começou como uma celebração para agradecer a boa colheita?"

    sofia "Ao longo dos anos, ele evoluiu, mas nunca perdeu seu significado."

    menu:
        "Não sabia disso. É fascinante como a história do vilarejo está entrelaçada com o festival.":

            dante "Não sabia disso. É fascinante como a história do vilarejo está entrelaçada com o festival."

        "Eu já sabia disso. Mas muito obrigado por me relembrar":
            dante "Eu já sabia disso. Mas muito obrigado por me relembrar"

    hide sofia normal with dissolve
    hide dante normal with dissolve

    # scene festival-noite with fade

    narrador "Finalmente, a noite do festival chega."

    narrador "A praça está iluminada com lanternas coloridas, e a música tradicional enche o ar."

    narrador "As barracas de comida oferecem delícias típicas da região, e as pessoas dançam e celebram com alegria."

    narrador "Dante, Helena e Vitória circulam pelo festival, absorvendo a atmosfera vibrante."

    narrador "Eles experimentam comidas típicas, participam de jogos e danças, e se envolvem na celebração."

    narrador "Dante se sente cada vez mais conectado com a cidade e seus habitantes."

    narrador "Enquanto caminham pela praça, encontram-se com o Padre Iohann."

    show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve
    show helena normal at Position(xpos = 0.3, ypos = 0.75) with dissolve
    show padre normal at Position(xpos = 0.7, ypos = 0.75) with dissolve

    padre "Boa noite, filhos. Espero que estejam aproveitando o festival."

    helena "Está maravilhoso, Padre Iohann. Obrigada por todo o trabalho duro."

    padre "O mérito é de todos nós. Amanhã, temos a procissão e outras atividades importantes. Espero vê-los lá."

    narrador "Dante olha para Helena e Vitória, ambos concordando em ajudar novamente."

    dante "Estaremos lá, Padre."

    hide padre normal with dissolve
    hide helena normal with dissolve
    hide dante normal with dissolve

    scene igreja-fora-noite

    show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve

    narrador "Durante a primeira noite do festival, Dante vê novamente as luzes estranhas perto da igreja."

    narrador "Ele tenta investigar, mas elas desaparecem antes que ele possa se aproximar."

    narrador "A sensação de que algo está fora do comum continua a perturbá-lo, mas ele decide manter suas preocupações para si por enquanto."

    hide dante normal with dissolve

    # scene festival-noite with fade

    narrador "Enquanto os três amigos conversam sobre a festa, Rocha, o policial, aproxima-se."


    show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve
    show vitoria normal at Position(xpos = 0.3, ypos = 0.75) with dissolve
    show helena normal at Position(xpos = 0.5, ypos = 0.75) with dissolve
    show rocha normal at Position(xpos = 0.9, ypos = 0.75) with dissolve

    rocha "Boa noite, pessoal. Aproveitando o festival?"

    vitoria "Sim, Rocha. Está tudo incrível."

    rocha "Recebi mais relatos de luzes estranhas perto da igreja. Se virem algo, por favor, nos avisem."

    narrador "Dante sente um arrepio, mas decide não deixar que isso estrague a noite."

    dante "Claro, Rocha. Manteremos os olhos abertos."

    hide rocha normal with dissolve
    hide helena normal with dissolve
    hide vitoria normal with dissolve
    hide dante normal with dissolve

    scene quarto-dante
    
    show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve

    narrador "No segundo dia do festival, Helena desaparece misteriosamente. A última vez que alguém a viu foi perto da igreja."
    
    narrador "A manhã começa com Dante acordando e percebendo que Helena não está em casa."

    hide dante normal with dissolve

    scene quarto-helena

    show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve
    show vitoria normal at Position(xpos = 0.3, ypos = 0.75) with dissolve

    dante "Helena?"

    narrador "Ele bate na porta do quarto dela. Não há resposta."

    vitoria "Ela deve estar na igreja."

    hide vitoria normal with dissolve
    hide dante normal with dissolve

    scene centro

    show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve
    show vitoria normal at Position(xpos = 0.3, ypos = 0.75) with dissolve

    narrador "Ele e Vitória começam a procurá-la por toda a cidade, perguntando aos moradores se a viram."

    narrador "Eles vão até a igreja, onde encontram Padre Iohann."

    hide vitoria normal with dissolve
    hide dante normal with dissolve

    scene igreja-fora-dia
    
    show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve
    show vitoria normal at Position(xpos = 0.3, ypos = 0.75) with dissolve
    show padre normal at Position(xpos = 0.9, ypos = 0.75) with dissolve

    dante "Padre Iohann, você viu Helena esta manhã?"

    narrador "O padre parece pensativo."

    padre "Sim, a vi mais cedo. Ela disse que ia ajudar na montagem da procissão."

    hide padre normal with dissolve

    narrador "Dante e Vitória procuram pela igreja, mas não encontram sinal de Helena."

    narrador "Conforme o dia avança, a preocupação aumenta."

    hide vitoria normal with dissolve
    hide dante normal with dissolve

    narrador "Eles voltam para a praça, onde encontram Rocha."

    # scene praca

    show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve
    show vitoria normal at Position(xpos = 0.3, ypos = 0.75) with dissolve
    show rocha normal at Position(xpos = 0.9, ypos = 0.75) with dissolve

    vitoria "Rocha, precisamos da sua ajuda. Helena desapareceu."

    narrador "Rocha fica sério imediatamente."

    rocha "Vamos organizar uma busca. Ela estava perto da igreja, certo? Vamos começar por lá."

    hide rocha normal with dissolve
    hide vitoria normal with dissolve
    hide dante normal with dissolve

    scene centro

    show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve
    show vitoria normal at Position(xpos = 0.3, ypos = 0.75) with dissolve

    narrador "Enquanto a busca se intensifica, Dante e Vitória se sentem cada vez mais desesperados."

    narrador "Eles vasculham cada canto da cidade, perguntando a todos que encontram."

    vitoria "Helena estava tão animada com o festival."

    vitoria "Ela não desapareceria assim."

    dante "Eu sei. Algo está errado."

    show padre normal at Position(xpos = 0.1, ypos = 0.75) with dissolve

    narrador "Padre Iohann tenta manter a calma, mas Dante percebe que ele também está preocupado."

    padre "Precisamos manter a fé e continuar procurando"

    hide padre normal with dissolve
    hide vitoria normal with dissolve
    hide dante normal with dissolve

    narrador "A noite cai e Helena ainda não foi encontrada."

    narrador "A atmosfera do festival muda, tornando-se mais tensa e preocupada."

    # scene praca

    show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve
    show vitoria normal at Position(xpos = 0.3, ypos = 0.75) with dissolve

    narrador "Dante, Vitória e os outros se reúnem na praça, discutindo os próximos passos."

    dante "Ela não pode ter ido longe. Alguém deve ter visto algo."

    show rocha normal at Position(xpos = 0.9, ypos = 0.75) with dissolve

    rocha "Vamos continuar a busca pela manhã. Precisamos de mais luz."

    hide rocha normal with dissolve
    hide vitoria normal with dissolve
    hide dante normal with dissolve

    # scene quarto-dante-noite

    show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve

    narrador "Naquela noite, Dante tem um sonho estranho."

    narrador "Ele vê Helena perto da igreja, cercada pelas mesmas luzes misteriosas que ele viu antes."

    narrador "Acorda suando frio, decidido a descobrir a verdade."

    dante "Eu preciso ir até a igreja."

    narrador "Diz Dante para si mesmo, saindo silenciosamente de casa."

    hide dante normal with dissolve

    # scene igreja-dentro-noite

    narrador "Na igreja, ele encontra Ícaro e Augusto, os jovens seminaristas, que também estão preocupados com o desaparecimento de Helena."

    show dante normal at Position(xpos = 0.1, ypos = 0.75) with dissolve
    show icaro normal at Position(xpos = 0.7, ypos = 0.75) with dissolve
    show augusto normal at Position(xpos = 0.9, ypos = 0.75) with dissolve

    icaro "Dante, o que está fazendo aqui tão tarde?"

    dante "Eu tive um sonho... vi Helena aqui."

    augusto "Nós também ouvimos coisas estranhas."

    augusto "Vamos investigar juntos, mas por hora, você precisa descansar."

    dante "Sim, amanhã conversaremos melhor. Boa noite."

    hide dante normal with dissolve
    hide icaro normal with dissolve
    hide augusto normal with dissolve

    narrador "Dante se despede dos seminaristas e, em casa, tem uma péssima noite de sono, ainda preocupado com Helena."

    return
