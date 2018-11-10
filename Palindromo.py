#crear un detector de palindromo


palabra = 'ana'
palindromo = reversed(palabra)


def palin():
    if (list(palabra)) == (list(palindromo)):
        return True
    else:
        return False
