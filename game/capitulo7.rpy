

label capitulo7:
    
    $ peso_bom = historia.get_peso_bom().get('peso', 0) 
    
    if pesoFinal >= 10:
        call finalBom
    elif pesoFinal >= 5:
        call finalMedio
    else:
        call finalRuim

    return