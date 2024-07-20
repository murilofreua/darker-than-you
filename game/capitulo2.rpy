
define posicao_direita = Position(xalign=0.85, yalign=0.50)

define posicao_esquerda = Position(xalign=0.15, yalign=0.5)

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

    narrador "O trio caminhou até o centro da cidade, conheceram alguns residentes, atravessaram um riacho até chegarem na porta da Igreja da Misericórdia, uma bela igreja antiga."

    scene igreja-fora

    narrador "Apesar de não ser muito religioso..."

    play 

    narrador "Dante sentiu uma sensação estranha enquanto olhava para ela, como se alguma energia misteriosa o atraísse."



    

    return

