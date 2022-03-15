import numpy as np
import numpy.random as rd

##########################################
## funções de distância e definição de coordenadas

def f_generate_coords(num_nodes, interv=10, randint=False):
    if(not randint):
        return [[rd.uniform(-interv, interv), rd.uniform(-interv, interv)] for i in range(num_nodes)]
    else:
        return [[rd.randint(-interv, interv), rd.randint(-interv, interv)] for i in range(num_nodes)]

def f_calc_dist_euclidiana(x1, x2, y1, y2):
    return (((x1 - x2)**2) + ((y1 - y2)**2))**0.5

def f_calc_dist_eucl(coords):
    len_coords = len(coords)
    distances = np.full((len_coords, len_coords), np.inf)
    
    for i in range(len_coords):
        for j in range(i+1, len_coords):
            x1, x2, y1, y2 = coords[i][0], coords[j][0], coords[i][1], coords[j][1]
            d = f_calc_dist_euclidiana(x1, x2, y1, y2)
            distances[i][j] = d
            distances[j][i] = d
        
    return distances

##########################################
## busca gulosa

def f_obter_menor_valor(vetor, nodes):
    minimo, index = np.inf, 0
        
    for i in nodes:
        if(vetor[i] < minimo):
            minimo = vetor[i]
            index = i
            
    return minimo, index

def f_solucao_gulosa(distances, indice, return_vet_custos=False):
    path, custo, nodes = [], [], []
    curr = indice
    
    #gera sequencia de nós
    nodes.append(indice)
    nodes.extend([i for i in range(0, indice)])
    nodes.extend([i for i in range(indice+1, len(distances))])
        
    #caminha pela matriz, de forma gulosa
    for i in range(0, len(distances)-1):
        minimo, j = f_obter_menor_valor(distances[curr][:], nodes)
        
        custo.append(minimo)
        path.append(curr)
        nodes.remove(curr)
        curr = j
    
    #volta ao nó original
    minimo, j = f_obter_menor_valor(distances[curr][:], [indice])
    custo.append(minimo)
    path.append(curr)
                
    if(return_vet_custos):
        return path, custo
    
    return path, sum(custo)


##########################################
## busca aleatória com probabilidade

def f_obter_random_sol(vetor, nodes, prob):
    index = rd.choice(nodes, 1, p=prob)[0]
    minimo = vetor[index]

    return minimo, index

def f_gera_probabilidades(probab, nodes, curr):
    p = []
    for n in nodes:
        p.append(probab[curr][n])
    
    #redefine as probabilidades para que somem 1.
    p /= sum(p) 
    
    return p

def f_solucao_aleatoria_prob(distances, indice, probab, return_vet_custos=False):
    path, custo, nodes = [], [], []
    curr = indice
    
    #gera sequencia de nós
    #nodes.append(indice)
    nodes.extend([i for i in range(0, indice)])
    nodes.extend([i for i in range(indice+1, len(distances))])
        
    #caminha pela matriz, de forma gulosa
    for i in range(0, len(distances)-1):
        p = f_gera_probabilidades(probab, nodes, curr)
        minimo, j = f_obter_random_sol(distances[curr][:], nodes, p)
        
        custo.append(minimo)
        path.append(curr)
        nodes.remove(j)
        curr = j
    
    #volta ao nó original
    minimo, j = f_obter_random_sol(distances[curr][:], [indice], [1])
    custo.append(minimo)
    path.append(curr)
                
    if(return_vet_custos):
        return path, custo
    
    return path, sum(custo)