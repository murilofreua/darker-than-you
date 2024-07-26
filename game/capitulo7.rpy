

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



    scene tela-finais

    $ finalOtimoAtingido = persistent.finalOtimo
    $ finalBomAtingido = persistent.finalBom
    $ finalMedioAtingido = persistent.finalMedio
    $ finalRuimAtingido = persistent.finalRuim

    if finalOtimoAtingido:
        show final-otimo at Position(xpos = .2, ypos = 3) with dissolve
    if finalBomAtingido:
        show final-bom at Position(xpos = .4, ypos = .3) with dissolve
    if finalMedioAtingido:
        show final-medio at Position(xpos = .6, ypos = .3) with dissolve
    if finalRuimAtingido:
        show final-ruim at Position(xpos = .8, ypos = .3) with dissolve

    indefinido ""

    return