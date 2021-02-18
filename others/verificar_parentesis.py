def parejas(str_pareja):

    list_simbols = ["()",r"{}", "[]"]

    if str_pareja in list_simbols:
        return True
    else: 
        return False
global b1
b1 = 0

def clean(simbols):
    if len(simbols) > 1:
        if parejas(simbols[-2:]) == True:
            simbols = simbols.replace(simbols[-2:], "")
        else: 
            if not len(simbols) <= 2:
                global b1
                b = simbols[-1]
                b1 = b
                a = clean(simbols[:len(simbols)- 1])

                if a == True:
                    return clean(b)
                else:
                    simbols = a
                    simbols = simbols + b

        if not simbols:
            return True 
        elif len(simbols) > 1: 
            return clean(simbols)
        elif b1: 
            return simbols
        else:
            return False
    else: 
        return False

print("El resultado es ", clean(r"{}[{}"))
print("El resultado es ", clean(r"(){}]"))
print("El resultado es ", clean(r"({}{})"))
print("El resultado es ", clean(r"(){}"))
print("El resultado es ", clean(r"{}{}"))
print("El resultado es ", clean(r"()[]{}"))