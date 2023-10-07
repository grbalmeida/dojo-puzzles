def entre_letras(primeira_letra: str, segunda_letra: str):
    primeira_letra_minuscula = ord(primeira_letra.lower())
    segunda_letra_minuscula = ord(segunda_letra.lower())
    
    if primeira_letra_minuscula > segunda_letra_minuscula:
        return 'Não está na ordem alfabética'
    
    return segunda_letra_minuscula - primeira_letra_minuscula - 1