
label creditos:

    scene black

    show text """
    Jogo criado por:
    Gabriel Cardoso de Castro
    João Gabriel Tavares
    Luís Felipe Pires
    Murilo Freua
    Vitor Ribeiro
    """ at truecenter with dissolve

    pause 5

    show text "Jogo criado na disciplina de Experiência do Usuário de Software" at truecenter with dissolve

    pause 5

    show text """
    Agradecimentos Especiais:
    - Professora Luciana Berreta
    """ at truecenter with dissolve

    pause 5

    show text """
    Ferramentas Utilizadas:
    - Ren'Py
    - Geração de imagens com Inteligências artificiais
    """ at truecenter with dissolve

    pause 5

    show text "Obrigado por jogar!" at truecenter with dissolve

    pause

    hide text "Obrigado por jogar!" with dissolve

    menu:
        "Gostaria de resetar os finais que já desbloqueou?"
        "Sim":
            menu:
                "Tem certeza que gostaria de resetar todos finais desbloqueados?"
                "Não":
                    pass
                "Sim":
                    menu:
                        "Tem certeza absoluta que gostaria de RESETAR os finais desbloqueados?"
                        "Sim":
                            $ persistent.finalOtimo = False
                            $ persistent.finalBom = False
                            $ persistent.finalMedio = False
                            $ persistent.finalRuim = False
                        "Não":
                            pass
        "Não":
            pass

    return