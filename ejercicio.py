def m_max( n1 : int, n2 : int) :
    """Dado dos numeros de entrada, retorna el mayor de ambos
    
    Argumentos:
        n1(int): Primer numero a comparar
        n2(int): Segundo numero a comparar
        
    Return:
        int: Mayor de ambos
    """
    if n1>n2:
        return n1 
    elif n2>n1 :
        return n2
    elif n1 ==n2 :
        raise Exception("Los valores no pueden ser iguales")
    else:
        Exception("Algo salio mal")



print(m_max(5,5))


