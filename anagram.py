def anagram(pal1,pal2):
    palabra1 = sorted(pal1)
    palabra2 = sorted(pal2)

    if palabra1 == palabra2:
        return True
    else:
        return False