# Simulação de Substituição de Páginas (FIFO, LRU, MRU)
# Feito por Augusto Sousa, Fabio Spiller, Lucas Gabriel, Vinicius Wamser
# Teste com 8 quadros de memória e três sequências de páginas

QTD_QUADROS = 8  # quantos quadros temos

# ----------------------------- Algoritmos -----------------------------

def fifo(seq_paginas, quadros):
    mem = [None]*quadros  # memória inicial vazia
    ponteiro = 0           # aponta qual quadro vai ser substituído
    faltas = 0             # contador de falhas
    
    for p in seq_paginas:
        if p not in mem:   # se a página não está na memória
            faltas += 1    # aconteceu uma falta
            mem[ponteiro] = p  # coloca a página no quadro atual
            ponteiro = (ponteiro + 1) % quadros  # próximo quadro
    return mem, faltas

def lru(seq_paginas, quadros):
    mem = []             # memória inicial vazia
    ult_uso = {}         # guarda o último uso de cada página
    faltas = 0           # contadode de falhas
    
    for i, p in enumerate(seq_paginas):
        if p not in mem:  # se não está na memória
            faltas += 1
            if len(mem) < quadros:
                mem.append(p)  # ainda tem espaço, só colocar
            else:
                # substitui a página menos usada recentemente
                menos_usada = min(ult_uso, key=ult_uso.get)
                mem[mem.index(menos_usada)] = p
                del ult_uso[menos_usada]  # tira do controle de uso
        ult_uso[p] = i  # marca o último uso da página
    return mem, faltas

def mru(seq_paginas, quadros):
    mem = []            # memória inicial vazia
    ult_uso = {}        # guarda o último uso de cada página
    faltas = 0          #contador de faltas
    
    for i, p in enumerate(seq_paginas):
        if p not in mem:
            faltas += 1
            if len(mem) < quadros: #adiciona na memoria
                mem.append(p)
            else:
                # substitui a página mais usada recentemente
                mais_usada = max(ult_uso, key=ult_uso.get) # acha a mais recente
                mem[mem.index(mais_usada)] = p # substitui
                del ult_uso[mais_usada]  # remove a antiga
        ult_uso[p] = i
    return mem, faltas

# ----------------------------- Funções Auxiliares -----------------------------

def quadro_de_pagina(mem, p):
    # devolve o quadro onde está a página ou "não está"
    try:
        return mem.index(p) + 1
    except:
        return "não está"

# ----------------------------- Sequências de Teste -----------------------------

casos = {
    'A': {'seq': [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7], 'busca': 7},
    'B': {'seq': [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11], 'busca': 11},
    'C': {'seq': [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11], 'busca': 11}
}

algos = {'FIFO': fifo, 'LRU': lru, 'MRU': mru}

# ----------------------------- Execução -----------------------------

print(f"\n--- SIMULAÇÃO: {QTD_QUADROS} QUADROS ---\n")

for caso, info in casos.items():
    seq = info['seq']
    alvo = info['busca']
    print(f"----- CASO {caso} -----")
    print(f"Sequência: {seq}")
    print(f"Página final buscada: {alvo}\n")
    
    for nome, func in algos.items():
        mem, faltas = func(seq, QTD_QUADROS)       # roda o algoritmo
        quadro = quadro_de_pagina(mem, alvo)       # acha a página final
        print(f"{nome}:")
        print(f"  Falhas: {faltas}")                # mostra falhas
        print(f"  Memória final: {mem}")           # mostra memória
        print(f"  Página {alvo} está no quadro {quadro}\n")

    print("="*40)