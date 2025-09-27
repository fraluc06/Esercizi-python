

def es17(ls, k):
    '''
    Es 7: 6 punti 
    progettare la funzione es17(ls,k) che: 
    - riceve  in input una lista di parole ls ed un intero k
    - cancella da ls le parole che contengono almeno k  caratteri uguali (sia in maiuscolo che in minuscolo)
    - restituisce il numero di parole cancellate da ls. 
    Nota che al termine della funzione la lista passata come parametro deve risultare modificata
    (ricorda che le liste sono mutabili). 
     ESEMPI:
     Se ls=[ 'ananas', 'pera', 'banana', 'melone', 'kiwi','albicocca'] e k=3
     la funzione restituisce 3 e la lista ls diventa ['pera', 'melone', 'kiwi']  
     Se ls=[ 'Angelo', 'Andrea', 'Osvaldo', 'Anna', 'Monica', 'Adele'] e k=2
     la funzione restituisce 4 e la lista ls diventa ['Angelo', 'Monica']
    '''
    canc=0
    app_ls = ls.copy()
    for s in app_ls:
        s_low = s.lower()
        for c in range(0,len(s_low)):
             if (s_low.count(s_low[c])>=k):
                 canc+=1
                 ls.remove (s)
                 break
             
    return canc

