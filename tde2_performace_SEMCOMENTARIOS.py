QTD_QUADROS = 8  


def fifo(seq_paginas, quadros):
    mem = [None]*quadros  
    ponteiro = 0           
    faltas = 0            
    
    for p in seq_paginas:
        if p not in mem:   
            faltas += 1    
            mem[ponteiro] = p  
            ponteiro = (ponteiro + 1) % quadros  
    return mem, faltas

def lru(seq_paginas, quadros):
    mem = []            
    ult_uso = {}         
    faltas = 0           
    
    for i, p in enumerate(seq_paginas):
        if p not in mem:  
            faltas += 1
            if len(mem) < quadros:
                mem.append(p)  
            else:
                menos_usada = min(ult_uso, key=ult_uso.get)
                mem[mem.index(menos_usada)] = p
                del ult_uso[menos_usada]  
        ult_uso[p] = i  
    return mem, faltas

def mru(seq_paginas, quadros):
    mem = []            
    ult_uso = {}       
    faltas = 0         
    
    for i, p in enumerate(seq_paginas):
        if p not in mem:
            faltas += 1
            if len(mem) < quadros:
                mem.append(p)
            else:
                mais_usada = max(ult_uso, key=ult_uso.get) 
                mem[mem.index(mais_usada)] = p 
                del ult_uso[mais_usada]  
        ult_uso[p] = i
    return mem, faltas


def quadro_de_pagina(mem, p):
    try:
        return mem.index(p) + 1
    except:
        return "não está"


casos = {
    'A': {'seq': [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7], 'busca': 7},
    'B': {'seq': [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11], 'busca': 11},
    'C': {'seq': [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11], 'busca': 11}
}

algos = {'FIFO': fifo, 'LRU': lru, 'MRU': mru}


print(f"\n--- SIMULAÇÃO: {QTD_QUADROS} QUADROS ---\n")

for caso, info in casos.items():
    seq = info['seq']
    alvo = info['busca']
    print(f"----- CASO {caso} -----")
    print(f"Sequência: {seq}")
    print(f"Página final buscada: {alvo}\n")
    
    for nome, func in algos.items():
        mem, faltas = func(seq, QTD_QUADROS)      
        quadro = quadro_de_pagina(mem, alvo)       
        print(f"{nome}:")
        print(f"  Falhas: {faltas}")                
        print(f"  Memória final: {mem}")          
        print(f"  Página {alvo} está no quadro {quadro}\n")

    print("="*40)