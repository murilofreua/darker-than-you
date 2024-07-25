

label capitulo7:
    
    $ peso_bom = historia.get_peso_bom().get('peso', 0) 
    
    if peso_bom >= 10:
        call finalBom
    elif peso_bom >= 5:
        call finalMedio
    else:
        call finalRuim

    return