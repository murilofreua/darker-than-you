define narrador = Character("")

image cozinha = "images/cenarios/cozinha.png"
image igreja-dentro = "images/cenarios/igreja-dentro.png"


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

    dante "Dormi sim, obrigado. O cheiro de café está maravilhoso."

    play sound "audio/bebendo café.mp3"

    narrador "Enquanto tomavam café, Helena e Vitória discutiam o plano do dia."

    helena "Pensei em levar você para conhecer a Igreja da Misericórdia e conversar com o Padre Iohann. Ele é uma pessoa fascinante"

    stop sound

    narrador "Dante assentiu, lembrando-se das palavras de Rocha sobre as luzes estranhas. Ele estava curioso para conhecer o Padre Iohann e descobrir mais sobre a igreja que tanto o intrigara."

    narrador "Após o café, o trio seguiu em direção à igreja. O caminho era tranquilo, com poucas pessoas nas ruas, e a brisa fresca da manhã tornava a caminhada agradável."
    
    stop sound

    scene igreja-dentro

    narrador "Quando chegaram à igreja, Dante ficou impressionado novamente com sua arquitetura."

    narrador "A fachada barroca estava decorada com detalhes intrincados, e os vitrais coloridos refletiam a luz do sol, criando um espetáculo de cores."

    narrador "Ao entrarem, foram recebidos pelo som suave do órgão e pelo aroma de incenso. No altar, um homem alto de cabelos negros e olhos cansados estava terminando suas orações. Ao notar a presença dos visitantes, ele se levantou e se aproximou."

    show padre iohann normal at Position(xpos = 0.5, ypos = 0.75) with dissolve

    padre iohann "Bom dia, Helena, Vitória. E você deve ser Dante, o amigo de Helena. Sou o Padre Iohann. Seja bem-vindo à nossa igreja."

    dante "Muito prazer em conhecê-lo, Padre Iohann. É um lugar lindo."

    padre iohann "Obrigado, meu filho. Esta igreja tem uma história rica, que muitos desconhecem. Espero que possam sentir a paz que ela proporciona."

    narrador "Enquanto conversavam, dois jovens seminaristas se aproximaram, curiosos. Helena os apresentou a Dante."

    show icaro normal at Position(xpos = 0.3, ypos = 0.75) with dissolve
    show augusto normal at Position(xpos = 0.7, ypos = 0.75) with dissolve

    helena "Este é Ícaro e aquele é Augusto. Eles estão estudando aqui com o Padre Iohann."

    icaro "Muito prazer. É sempre bom conhecer pessoas novas."

    augusto "Prazer em conhecê-lo."

    narrador "Dante sentiu uma sensação de camaradagem entre os seminaristas e o padre, mas não podia deixar de pensar nas luzes estranhas mencionadas por Rocha."

    return
