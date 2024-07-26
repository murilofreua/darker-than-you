

label capitulo7:
    
    $ peso_final = historia.get_peso_bom()
    
    # if peso_final == 13:
    #     call finalOtimo
    # elif peso_final >= 9:
    #     call finalBom
    # elif peso_final >= 5:
    #     call finalMedio
    # else:
    #     call finalRuim



    #Trecho apenas para facilitar o desenvolvimento de visualização dos finais
    menu:
        "Escolher final"
        "Final ótimo":
            call finalOtimo
        "Final Bom":
            call finalBom
        "Final Medio":
            call finalMedio
        "Final Ruim":
            call finalRuim



    scene textura-madeira2

    $ finalOtimoAtingido = persistent.finalOtimo
    $ finalBomAtingido = persistent.finalBom
    $ finalMedioAtingido = persistent.finalMedio
    $ finalRuimAtingido = persistent.finalRuim

    if finalOtimoAtingido:
        show selo-final-otimo at Position(xpos=0.2, ypos=0.6) with dissolve
    else:
        show retangulo-vazio at Position(xpos=0.2, ypos=0.6) with dissolve

    if finalBomAtingido:
        show selo-final-bom at Position(xpos=0.4, ypos=0.6) with dissolve
    else:
        show retangulo-vazio1 at Position(xpos=0.4, ypos=0.6) with dissolve

    if finalMedioAtingido:
        show selo-final-medio at Position(xpos=0.6, ypos=0.6) with dissolve
    else:
        show retangulo-vazio2 at Position(xpos=0.6, ypos=0.6) with dissolve

    if finalRuimAtingido:
        show selo-final-ruim at Position(xpos=0.8, ypos=0.6) with dissolve
    else:
        show retangulo-vazio3 at Position(xpos=0.8, ypos=0.6) with dissolve


    pause

    return