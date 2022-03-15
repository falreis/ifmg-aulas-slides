import numpy as np

def solver(objet, f_obj, restr_A, restr_op, restr_b, verbose=False):
    """
    Função para solução de problemas de programação linear
    Deve ser implementada para solução de PPL usando métodos Simplex e Simplex Duas Fases.
    Não devem ser adicionados novos parâmetros à função.
    
    Parâmetros:
    : param objet:    string, contendo indicação de 'MA' (para maximização) ou 'MI' (para minimização)
    : param f_obj:    np.array float, contendo a função objetivo
    : param restr_A:  np.array float, contendo a matriz A das restrições
    : param restr_op: np.array string, contendo o vetor de operadores das restrições
    : param restr_b:  np.array float, contendo o vetor b das restrições
    : param verbose:  booleano opcional para impressão de valores intermediários (não obrigatório implementar)
    : return:         np.array contendo os valores das variáveis (não retornar valor da função objetivo nem variáveis de folga)
    """
    
    #verifica tipo dos parâmetros (não remover)
    if not isinstance(objet, str):
        raise TypeError('Parâmetro "objet" diferente do especificado.')
    
    if(objet != 'MA' and objet != 'MI'):
        raise TypeError('Tipo de objetivo diferente do especificado.')
    
    if not isinstance(f_obj, np.ndarray):
        raise TypeError('Parâmetro "f_obj" diferente do especificado.')
        
    if not isinstance(restr_A, np.ndarray):
        raise TypeError('Parâmetro "restr_A" diferente do especificado.')
    
    if not isinstance(restr_op, np.ndarray):
        raise TypeError('Parâmetro "restr_op" diferente do especificado.')
        
    if not isinstance(restr_b, np.ndarray):
        raise TypeError('Parâmetro "restr_b" diferente do especificado.')
    
    #################################################################
    ##
    # implemente seu código aqui
    # caso queira, subdivida o código em funções
    ##
    #################################################################
    
    if(verbose):                     #esta linha pode ser removida
        print('Solver Simplex IFMG') #esta linha pode ser removida

    #return np.array([[2.66, 3.33]]) #exemplo retorno (esta linha pode ser removida)
    
    #alterar para implementação dos valores de retorno
    return None