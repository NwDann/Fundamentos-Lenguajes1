
# FUERZA BRUTA ALGORITMO

def brute_force(text, pattern):
    l1 = len(text)
    l2 = len(pattern) #Control de tamaños
    
    i = 0 # Variable para bucle
    
    flag = False # Es falso hasta encontrarse un match
    
    while (i < l1):
        j = 0 # Variable para bucle
        count = 0
        
        while j < l2: # iterar desde el indice e del patrón hasta len-1
            if i+j < l1 and text [i+j] == pattern[j]: # statement to check if a match has occurred or not 
                count += 1 # count aumenta en 1 si hay coincidencia en los caracteres

            else:
                break

            j+1

        if count == l2: # it shows a matching of pattern in the text
            print("\nPattern occurs at index", i) # print el indice donde empieza el match 
            flag = True # flag se convierte en True porque se ha enconctrado al menos un match.
        i += 1
        
    if not flag:
    #If the pattern doesn't occur at all, means no match of pattern in the text string
        print('\nPattern is not at all present in the array')