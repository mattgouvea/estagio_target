def inverte(string):
    resposta = []
    for i in range(len(string) - 1, -1, -1):
        resposta.append(string[i])
    
    print(''.join(resposta))
    return

inverte('1234')