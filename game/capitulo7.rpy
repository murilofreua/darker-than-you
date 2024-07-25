label capitulo7:

    $ historia.get_peso_bom()

    if historia.get_peso_bom() >= 2:
        call finalBom
    elif historia.get_peso_bom() >= 1:
        call finalMedio
    else:
        call finalRuim

    return