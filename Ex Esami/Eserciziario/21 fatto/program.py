def es21(matrice):
    '''
    es21(matrice) presa la matrice di caratteri rappresentata tramite una lista di liste di caratteri, 
    la restituisce dopo averne ordinato le colonne in ordine lessicografico. 
    La matrice passata in input al termine della funzione non deve risultare modificata.  
    Ad esempio se la matrice di input e'
     [['q','s','g','g'],
      ['b','a','m','f'],
      ['a','b','n','z']] 
    la funzione restituira' la matrice:
     [['a','a','g','f'],
      ['b','b','m','g'],
      ['q','s','n','z']]     
    '''

    nr = len(matrice)
    nc = len(matrice[0])
    new_mat = []
    for r in range (nr):
        app_list = []
        for c in range (nc):
           app_list.append(' ') 
        new_mat.append(app_list)   
    
    for c in range(nc):
        app_list = []
        for r in range(nr):
            app_list += matrice [r][c]
        app_list.sort()    
        for n in range(nr):
            new_mat[n][c] = app_list[n]
    return new_mat
    