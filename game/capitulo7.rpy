

label capitulo7:
    
    $ peso_final = historia.get_peso_bom()
    
    if peso_final >= 9:
        call finalBom
    elif peso_final >= 5:
        call finalMedio
    else:
        call finalRuim

    return