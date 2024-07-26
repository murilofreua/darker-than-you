

label capitulo7:
    
    $ ValorPesoBom = historia.get_peso_bom().get('peso', 0) 
    
    if ValorPesoBom >= 9:
        call finalBom
    elif ValorPesoBom >= 5:
        call finalMedio
    else:
        call finalRuim

    return