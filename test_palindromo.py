def test_palin():
    palabra = 'ana'
    palindromo = reversed(palabra)
    resultado = (list(palabra)) == (list(palindromo))

    assert True == resultado , 'si es un palindromo'
    assert False != resultado, 'no es un palindromo'