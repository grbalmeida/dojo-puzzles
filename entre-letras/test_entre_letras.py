from entre_letras import entre_letras

def test_deve_retornar_mensagem_erro_se_letras_nao_estiverem_ordenadas():
    mensagem_validacao = 'Não está na ordem alfabética'
    assert entre_letras('w', 'e') == mensagem_validacao
    assert entre_letras('b', 'a') == mensagem_validacao
    assert entre_letras('d', 'b') == mensagem_validacao
    assert entre_letras('z', 'f') == mensagem_validacao
    
    assert entre_letras('W', 'E') == mensagem_validacao
    assert entre_letras('B', 'A') == mensagem_validacao
    assert entre_letras('D', 'B') == mensagem_validacao
    assert entre_letras('Z', 'F') == mensagem_validacao
    
def test_deve_retornar_a_quantidade_de_letras_entre_duas_letras():
    assert entre_letras('a', 'b') == 0
    assert entre_letras('a', 'c') == 1
    assert entre_letras('a', 'z') == 24
    assert entre_letras('A', 'B') == 0
    assert entre_letras('A', 'C') == 1
    assert entre_letras('A', 'Z') == 24
    assert entre_letras('A', 'F') == 4
    assert entre_letras('F', 'M') == 6