label capitulo7:
    
    $ peso_final = historia.get_peso_bom()

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

    $ finaisAtingidos = int(finalOtimoAtingido) + int(finalBomAtingido) + int(finalMedioAtingido) + int(finalRuimAtingido)

    show text "Você atingiu [finaisAtingidos] de 4 finais possíveis" at Position(xpos=0.5, ypos=0.19)

    if finalOtimoAtingido:
        show selo-final-otimo at Position(xpos=0.2, ypos=0.6) with dissolve
    else:
        show retangulo-vazio-branco at Position(xpos=0.2, ypos=0.6) with dissolve

    if finalBomAtingido:
        show selo-final-bom at Position(xpos=0.4, ypos=0.6) with dissolve
    else:
        show retangulo-vazio-branco1 at Position(xpos=0.4, ypos=0.6) with dissolve

    if finalMedioAtingido:
        show selo-final-medio at Position(xpos=0.6, ypos=0.6) with dissolve
    else:
        show retangulo-vazio-branco2 at Position(xpos=0.6, ypos=0.6) with dissolve

    if finalRuimAtingido:
        show selo-final-ruim at Position(xpos=0.8, ypos=0.6) with dissolve
    else:
        show retangulo-vazio-branco3 at Position(xpos=0.8, ypos=0.6) with dissolve

    pause

    return