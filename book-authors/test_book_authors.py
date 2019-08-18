# -*- coding: utf-8 -*-

from book_authors import book_authors
import types

def test_should_be_a_function():
    assert isinstance(book_authors, types.FunctionType)

def test_should_return_a_string():
    assert type(book_authors('')) == str

def test_should_return_a_single_uppercase_string():
    assert book_authors('Guimaraes') == 'GUIMARAES'
    assert book_authors('ana') == 'ANA'
    assert book_authors('mArIa') == 'MARIA'

def test_first_author():
    assert book_authors('Joao Silva') == 'SILVA, Joao'
    assert book_authors('joao silva') == 'SILVA, Joao'
    assert book_authors('JOAO SILVA') == 'SILVA, Joao'

def test_second_author():
    assert book_authors('Paulo Coelho') == 'COELHO, Paulo'
    assert book_authors('paulo coelho') == 'COELHO, Paulo'
    assert book_authors('PAULO COELHO') == 'COELHO, Paulo'

def test_third_author():
    assert book_authors('Celso de Araujo') == 'ARAUJO, Celso de'
    assert book_authors('celso de araujo') == 'ARAUJO, Celso de'
    assert book_authors('CELSO DE ARAUJO') == 'ARAUJO, Celso de'

def test_fifth_author():
    assert book_authors('Maria Pereira da Silva') == 'SILVA, Maria Pereira da'
    assert book_authors('maria pereira da silva') == 'SILVA, Maria Pereira da'
    assert book_authors('MARIA PEREIRA DA SILVA') == 'SILVA, Maria Pereira da'

def test_sixth_author():
    assert book_authors('Matilde Santos Dias') == 'DIAS, Matilde Santos'
    assert book_authors('matilde santos dias') == 'DIAS, Matilde Santos'
    assert book_authors('MATILDE SANTOS DIAS') == 'DIAS, Matilde Santos'

def test_seventh_author():
    assert book_authors('Augusto dos Santos de Oliveira') == 'OLIVEIRA, Augusto dos Santos de'
    assert book_authors('Augusto dos santos de oliveira') == 'OLIVEIRA, Augusto dos Santos de'
    assert book_authors('Augusto DOS SANTOS DE OLIVEIRA') == 'OLIVEIRA, Augusto dos Santos de'

def test_eighth_author():
    assert book_authors('Joana das Graças Moraes de Almeida') == 'ALMEIDA, Joana das Graças Moraes de'
    assert book_authors('joana das graças moraes de almeida') == 'ALMEIDA, Joana das Graças Moraes de'

def test_ninth_author():
    assert book_authors('Maria do Carmo') == 'CARMO, Maria do'
    assert book_authors('maria do carmo') == 'CARMO, Maria do'
    assert book_authors('MARIA DO CARMO') == 'CARMO, Maria do'

def test_inherited_fathers_name():
    assert book_authors('João Filho') == 'FILHO, João'
    assert book_authors('joão filho') == 'FILHO, João'

def test_inherited_grandfathers_name():
    assert book_authors('João Neto') == 'NETO, João'
    assert book_authors('joão neto') == 'NETO, João'
    assert book_authors('João Silva Neto') == 'SILVA NETO, João'
    assert book_authors('joão silva neto') == 'SILVA NETO, João'
    assert book_authors('João da Silva Neto') == 'SILVA NETO, João da'
    assert book_authors('joão da silva neto') == 'SILVA NETO, João da'

def test_inherited_mothers_name():
    assert book_authors('Maria Filha') == 'FILHA, Maria'
    assert book_authors('maria filha') == 'FILHA, Maria'
    assert book_authors('MARIA FILHA') == 'FILHA, Maria'
    assert book_authors('Maria Novaes Filha') == 'NOVAES FILHA, Maria'
    assert book_authors('maria novaes filha') == 'NOVAES FILHA, Maria'

def test_inherited_grandmothers_name():
    assert book_authors('Cecilia Neta') == 'NETA, Cecilia'
    assert book_authors('cecilia neta') == 'NETA, Cecilia'
    assert book_authors('CECILIA NETA') == 'NETA, Cecilia'
    assert book_authors('Cecilia Oliveira Neta') == 'OLIVEIRA NETA, Cecilia'
    assert book_authors('cecilia oliveira neta') == 'OLIVEIRA NETA, Cecilia'

def test_inherited_uncles_name():
    assert book_authors('Augusto Sobrinho') == 'SOBRINHO, Augusto'
    assert book_authors('augusto sobrinho') == 'SOBRINHO, Augusto'
    assert book_authors('AUGUSTO SOBRINHO') == 'SOBRINHO, Augusto'
    assert book_authors('Augusto Moraes Sobrinho') == 'MORAES SOBRINHO, Augusto'
    assert book_authors('augusto moraes sobrinho') == 'MORAES SOBRINHO, Augusto'

def test_inherited_aunts_name():
    assert book_authors('Alessandra Sobrinha') == 'SOBRINHA, Alessandra'
    assert book_authors('alessandra sobrinha') == 'SOBRINHA, Alessandra'
    assert book_authors('ALESSANDRA SOBRINHA') == 'SOBRINHA, Alessandra'
    assert book_authors('Alessandra Lessa Sobrinha') == 'LESSA SOBRINHA, Alessandra'
