
define posicao_direita = Position(xalign=0.85, yalign=0.50)

define posicao_esquerda = Position(xalign=0.15, yalign=0.5)

define posicao_centro = Position(xalign=0.50,yalign=0.5)

label capitulo2:

    scene centro

    narrador "Dante sentia a sensação de voltar para o passado"

    narrador "A paisagem verdejante e as casas simples no estilo barroco europeu lembravam sua infância, passada numa pequena cidade no interior de Goiás"

    show helena normal with dissolve:
        yalign 0.50
        xalign 0.30

    show vitoria normal with dissolve:
        yalign 0.50
        xalign 0.65


    indefinido "..."

    hide vitoria normal with dissolve

    show helena normal at posicao_direita with move

    helena "Tão bom te ver!"

    show dante normal at posicao_esquerda 

    menu: 
        "Abraçar":
            dante "Olá, Helena! Você mudou muito desde a última vez que nos vimos!"
    
    hide helena normal with dissolve

    show vitoria normal at posicao_direita with dissolve

    vitoria "Prazer, Dante! Sou a Vitória, muito prazer"

    menu:
        "Cumprimentar cordialmente":
            dante "Prazer Vitória, sou Dante"
    
    hide dante normal with dissolve
    
    hide vitoria normal with dissolve

    narrador "O trio passou o dia caminhando pelo centro da cidade, conheceram alguns residentes e atravessaram um riacho..."

    narrador "até chegarem na porta da Igreja da Misericórdia, uma bela igreja antiga."

    scene igreja-fora-dia

    narrador "Apesar de Dante de não ser muito religioso..."

    play sound "audio/trovão.mp3"

    narrador "O garoto sentiu uma sensação estranha enquanto olhava para a igreja, como se alguma energia misteriosa o atraísse."

    show dante at posicao_esquerda with dissolve

    dante "Que bela igreja!"

    show helena at posicao_direita with dissolve

    helena "É incrível, né?"

    helena "A Igreja é símbolo deste lugar. Seus fundadores vieram da Europa e trouxeram a tradição católica aqui"

    stop sound 

    hide dante normal with dissolve

    hide helena normal with dissolve

    narrador "Após uma tarde de conversa, os três se dirigiram para a padaria favorita de Vitória, próxima à praça principal da cidade. Lá, foram recebidos por Seu Pedro, o padeiro."

    scene padaria-dentro

    show pedro normal at posicao_direita with dissolve

    pedro "Olha quem veio! Helena, você trouxe um visitante especial, não é? "

    show helena normal at posicao_centro with dissolve

    helena "Ah, Seu Pedro! Este é o meu amigo Dante. Ele está aqui para passar alguns dias conosco."

    pedro "Ah sim! Bem-vindo ao vilarejo! Eu sou Pedro"

    show dante normal at posicao_esquerda with dissolve

    menu: 
        "Apertar a mão de Pedro":
            dante "Obrigado, Seu Pedro. É um prazer conhecer você."

    pedro "O que querem comer? Aposto que estão morrendo de fo.."

    narrador "Mal ele terminara a frase, Helena e Vitória riram em disparate, acompanhadas pelo padeiro"

    menu:
        "Sorrir confuso":
            narrador "Dante olhou para Helena e Vitória, ainda rindo, e sorriu confuso"

    hide pedro normal 
    hide dante normal
    hide helena normal
    with dissolve

    narrador "Seu Pedro, com seu semblante acolhedor, guiou o trio até uma mesa perto da janela, de onde se podia ver a praça principal começando a se iluminar com as luzes da noite."
    
    show pedro normal at posicao_centro with dissolve

    pedro "Hoje temos pão de queijo fresquinho, broa de milho, e bolos variados — anunciou Seu Pedro, com um sorriso orgulhoso."

    pedro "E claro, o café passado na hora, que não pode faltar."

    show helena normal at posicao_direita 

    helena "Parece uma ótima escolha! Vou querer um pouco de tudo, para experimentar."

    hide pedro normal with dissolve

    show vitoria normal at posicao_centro with dissolve 

    vitoria "Dante, você vai adorar o festival!"

    vitoria "É a melhor época do ano aqui: tem música, danças tradicionais, comidas típicas e até bingo!"

    show dante normal at posicao_esquerda with dissolve

    dante "Sou muito bom no bingo hein! Já estou ansioso!"

    dante "Parece incrível!"

    show pedro normal at top behind vitoria
    
    narrador "Logo, Seu Pedro retornou com uma bandeja cheia de delícias, e os três começaram a comer, rindo e conversando sobre a vida no vilarejo e relembrando histórias de infância. A tarde caía e Dante sentiu-se mais relaxado e feliz do que em muito tempo."

    narrador "Depois de agradecer calorosamente a Seu Pedro e pagarem a conta, o trio se dirigiu à praça principal. "

    hide dante normal with dissolve

    hide helena normal with dissolve

    hide vitoria normal with dissolve

    hide pedro normal with dissolve

    scene centro-final-tarde

    narrador "A brisa da tarde assoprava fria e o céu se estendia como uma folha de ouro sob suas cabeças, e iluminava resplandecia toda a cidade"


    narrador "Caminhando pela praça, a atmosfera acolhedora do vilarejo os envolvia. Crianças corriam e brincavam, e grupos de amigos conversavam animadamente"

    narrador "Ao se aproximarem de um banco perto da fonte, avistaram uma mulher sentada, muito concentrada na leitura de um pequeno livro de capa cor de vinho, sem título. A sombra de Vitória tocou as páginas, e ela notou a presença do grupo." 

    show sofia normal at posicao_direita with dissolve

    sofia "Helena, Vitória! Quem é o rapaz?"

    show helena normal at posicao_centro with dissolve

    helena "Boa noite, Sofia"

    helena "Este é Dante, um amigo meu de infância. Ele está aqui para passar alguns dias conosco"

    sofia "Seja bem-vindo, Dante"

    sofia "Espero que goste da nossa cidade"

    show dante normal at posicao_esquerda with dissolve

    dante "Muito prazer em conhecê-la! Até agora, todos têm sido muito acolhedores."

    sofia "Que bom ouvir isso. A Encosta da Saudade é um lugar especial. Se precisar de algo, não hesite em me procurar."

    narrador "Enquanto conversavam, Isabel, a esposa do fazendeiro, se aproximou, carregando uma cesta de frutas."

    hide dante normal 
    hide vitoria normal 
    hide helena normal 
    hide sofia normal
    with dissolve

    show isabel normal at posicao_centro with dissolve

    isabel "Boa noite, meninas. Quem é este novo amigo?"

    show vitoria normal at posicao_direita

    vitoria "Este é Dante, um amigo de infância da Helena. Ele está aqui para passar alguns dias conosco."

    isabel " Bem-vindo, Dante. Espero que aproveite sua estadia. Aceite uma maçã fresca da fazenda."

    show dante normal at posicao_esquerda with dissolve

    menu:
        "Aceitar maçã":
            show dante normal at posicao_esquerda
            dante "Obrigado, Isabel. É um prazer conhecê-la!"

    hide isabel normal 
    hide vitoria normal
    hide dante normal
    with dissolve

    narrador "Enquanto continuavam a conversar, Rocha, o policial, aproximou-se do grupo, acenando com um sorriso."

    show rocha normal at posicao_centro with dissolve
    
    rocha "Boa noite, pessoal. Parece que temos um novo rosto na cidade"   

    show rocha normal at posicao_direita with move

    show vitoria normal at posicao_centro

    vitoria "Boa noite, Rocha. Este é Dante, amigo de infância da Helena"  

    rocha "Prazer em conhecê-lo, Dante"

    show dante normal at posicao_esquerda with dissolve

    menu:
        "Apertar mão de rocha firmemente":
            rocha "Espero que aproveite sua estadia."
            dante "Obrigado, Rocha. Até agora, tudo tem sido ótimo"
            rocha "Isso é bom de ouvir"
            rocha "Mas, preciso alertar vocês sobre algo estranho que aconteceu hoje."
            vitoria "O que houve??"
    
    hide dante normal
    hide vitoria normal 
    with dissolve

    show rocha normal at posicao_centro with move

    rocha "Recebemos uma denúncia de que algumas pessoas viram luzes estranhas perto da Igreja nesta madrugada. Não sabemos o que pode ter causado isso, mas é algo que estamos investigando"

    show vitoria normal at posicao_direita

    vitoria "Luzes estranhas?  Como assim?"

    hide vitoria normal

    rocha "Testemunhas dizem que pareciam pequenas esferas de luz flutuando ao redor da igreja, desaparecendo antes de poderem se aproximar"

    rocha "Eu sei que pode parecer estranho, mas estamos tratando isso com seriedade. Se virem algo, por favor, nos avisem imediatamente."

    narrador "Dante sentiu um arrepio percorrer sua espinha. Aquela Igreja já lhe causara uma sensação estranha durante o dia."

    show helena normal at posicao_esquerda with dissolve

    helena "Vamos ficar atentos, Rocha. Obrigada por nos avisar"

    rocha "Se precisarem de qualquer coisa, sabem onde me encontrar."

    hide rocha normal
    hide helena normal
    hide dante normal
    hide vitoria normal
    with dissolve

    narrador "Depois da conversa com o policial, o grupo se despediu e continuou caminhando pela praça, com uma leve tensão no ar."

    show dante normal at posicao_esquerda with dissolve

    dante "Isso é muito estranho"

    show vitoria normal at posicao_direita

    vitoria "Concordo. Mas vamos tentar não nos preocupar demais. Amanhã é um novo dia, e vamos descobrir mais sobre essa história."

    show helena normal at posicao_centro 

    helena "Sim, vamos descansar agora. Amanhã pode ser um dia longo"

    hide helena normal
    hide dante normal
    hide vitoria normal 
    with dissolve

    scene quarto-helena

    show helena normal at posicao_direita with dissolve

    helena "Espero que goste do quarto. É simples, mas confortável"

    show dante normal at posicao_esquerda 

    dante "Está ótimo, Helena. Obrigado por tudo"

    show vitoria normal at posicao_centro

    vitoria "Nós também estamos felizes que você veio. Boa noite, Dante. Até amanhã"

    dante "Boa noite, Vitória. Boa noite, Helena"

    hide vitoria normal

    hide dante normal 
    
    hide helena normal

    with dissolve

    return
