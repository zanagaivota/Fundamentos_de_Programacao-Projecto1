

artigo_def = ("A","O")

vogal_palavra = artigo_def + ("E",)

vogal = vogal_palavra + ("I","U")

ditongo_palavra = ("AI","AO","EU","OU")

ditongo = ditongo_palavra + ("AE","AU","EI","OE","OI","IU")

par_vogais = ditongo + ("IA","IO")

consoante_freq = ("D","L","M","N","P","R","S","T","V")

consoante_terminal = ("L","M","R","S","X","Z")

consoante_final = ("N","P") + consoante_terminal

consoante = ("B","C","D","F","G","H","J","L","M","N","P","Q","R","S","T","V","X","Z")

par_consoantes = ("BR","CR","FR","GR","PR","TR","VR","BL","CL","FL","GL","PL")

def tupleProdutoCartesiano (t1,t2):
    
    """
    Receives two tuples and returns a tuple which is the result of 
    concatenating each element of one tuple with each element of the other
    """
    
    t1index = 0
    t2index = 0
    newTuple = ()
    t1Length = len(t1)
    t2Length = len(t2)
    newTupleIndex = 0
    while t1index < t1Length:
        while t2index < t2Length :
            newTuple = newTuple[:newTupleIndex] + (t1[t1index]+t2[t2index],)
            t2index = t2index + 1
            newTupleIndex = newTupleIndex + 1
        t1index = t1index + 1
        t2index = 0
    return newTuple


monossilabo_2 = ("AR","IR","EM","UM") + tupleProdutoCartesiano(vogal_palavra,("S",)) + ditongo_palavra + tupleProdutoCartesiano(consoante_freq,vogal)


monossilabo_3 = tupleProdutoCartesiano(tupleProdutoCartesiano(consoante,vogal),consoante_terminal) + tupleProdutoCartesiano(consoante,ditongo) + tupleProdutoCartesiano(par_vogais,consoante_terminal)



def e_monossilabo(string):  
    """
    Receives a string and checks if it is a monossilabo.
    A string is a monossilabo if it is:
    <vogal_palavra> or <monossilabo_2> or <monossilabo_3>    
    """
    
    if not isinstance(string,str):
        raise ValueError ("e_monossilabo:argumento invalido")
  
    else:
        return string in vogal_palavra or string in monossilabo_2 or string in monossilabo_3



def e_silaba_2 (string):
    """
    Receives a string and checks if it is a silaba_2.
    A string is a silaba_2 if it is:
    <par_vogais> or <consoante><vogal> or <vogal><consoante_final>
    """    
    return string in par_vogais or string in tupleProdutoCartesiano(consoante,vogal) or string in tupleProdutoCartesiano(vogal,consoante_final)


def e_silaba_3 (string):
    """
    Receives a string and checks if it is a silaba_3.
    A string is a silaba_3 if it is:
    "QUA" or "QUE" or "QUI" or "GUE" or "GUI" or
    <vogal>NS or <consoante><par_vogais> or
    <consoante><vogal><consoante_final> or
    <par_vogais><consoante_final> or
    <par_consoantes><vogal>
    """    
    return string in ("QUA","QUE","QUI","GUE","GUI") or string in tupleProdutoCartesiano(vogal,("NS",)) or string in tupleProdutoCartesiano(consoante,par_vogais) or string in tupleProdutoCartesiano(tupleProdutoCartesiano(consoante,vogal),consoante_final) or string in tupleProdutoCartesiano(par_vogais,consoante_final) or string in tupleProdutoCartesiano(par_consoantes,vogal) 

def e_silaba_4 (string):
    """
    Receives a string and checks if it is a silaba_4.
    A string is a silaba_4 if it is:
    <par_vogais>NS or <consoante><vogal>NS or <consoante><vogal>IS or
    <par_consoantes><par_vogais> or <consoante><par_vogais><consoante_final>
    """    
    return string in tupleProdutoCartesiano(par_vogais,("NS",)) or string in tupleProdutoCartesiano(tupleProdutoCartesiano(consoante,vogal),("NS",)) or string in tupleProdutoCartesiano(tupleProdutoCartesiano(consoante,vogal),("IS",)) or string in tupleProdutoCartesiano(par_consoantes,par_vogais) or string in tupleProdutoCartesiano(tupleProdutoCartesiano(consoante,par_vogais),consoante_final)

def e_silaba_5 (string):
    """
    Receives a string and checks if it is a silaba_5.
    A string is a silaba_5 if it is:
    <par_consoantes><vogal>NS
    """    
    return string in tupleProdutoCartesiano(tupleProdutoCartesiano(par_consoantes,vogal),("NS",))

def e_silaba_final (string):
    """
    Receives a string and checks if it is a silaba_final.
    A string is a silaba_final if it is:
    <monossilabo_2> or <monossilabo_3> or <silaba_4> or <silaba_5> 
    """    
    return string in monossilabo_2 or string in monossilabo_3 or e_silaba_4(string) or e_silaba_5(string)

def e_silaba (string):
    """
    Receives a string and checks if it is a silaba
    A string is a silaba if it is:
    <vogal> or <silaba_2> or <silaba_3> or <silaba_4> or <silaba_5>
    """   
     
    if not isinstance(string,str):
        raise ValueError ("e_silaba:argumento invalido")    
    else:
        return string in vogal or e_silaba_2(string) or e_silaba_3(string) or e_silaba_4(string) or e_silaba_5(string)




def e_silaba_multi (stringSilabas):
    
    """
    Receives a string and checks if it is:
    <silaba> or 
    multi <silaba>: <silaba>...<silaba>
    In summary, it does the following:
    """
    # In summary, it does the fllowing:
    # tries to find a silaba and continues throughout the rest of the string to see if it finds another silaba and so on
    # if it doesn't, it goes back to the last silaba found and adds another character to see if it is a silaba
    # and so forth to check if the string given can be divided in silabas
    
    
    result = False
    silabasTest = stringSilabas 
    tIndexSilabas = (0,) # saves the index where each silaba found ends
    processedIndexes = 1
    processedIndexesTemp = 1
    stringSilabasLength = len(stringSilabas)
    
    while processedIndexes <= stringSilabasLength:
        silabasTestTemp = silabasTest[:processedIndexesTemp]
        if e_silaba (silabasTestTemp): 
            tIndexSilabas = tIndexSilabas + (processedIndexes,) 
            silabasTest = silabasTest [processedIndexesTemp:] # updates the variable that keeps the part of the string to be tested next
            processedIndexes = processedIndexes + 1 
            processedIndexesTemp = 1 # resets processedIndexesTemp because the string to be tested next was updated and so we need to start at the beggining of it
            
        elif processedIndexes < stringSilabasLength:
            processedIndexes = processedIndexes + 1 
            processedIndexesTemp = processedIndexesTemp + 1
            
        elif processedIndexes == stringSilabasLength and len(tIndexSilabas) > 1: # when silabasTestTemp is not a silaba, it checks if we already reached the end of the given string and if it already found a silaba before, if that's the case:
            silabasTest = stringSilabas[tIndexSilabas[-2]:] # updates the string to test to start in the index where the last silaba started
            processedIndexesTemp = tIndexSilabas[-1] - tIndexSilabas[-2] + 1 # updates processedIndexesTemp so we continue to iterate from where we last found a silaba
            processedIndexes = tIndexSilabas[-1] + 1 # resets processedIndexes to the index after the index where the last silaba found ends 
            tIndexSilabas = tIndexSilabas[:-1] # removes the index where the last silaba found ended because we will continue adding characters to that last silaba found until we found a silaba again
        
        else:
            break
    
    if tIndexSilabas[-1] == stringSilabasLength: # if the structure that keeps the indexes where each silaba ends has the last element equal to the length of string in analysis it means it was able to divide the whole string in analysis in silabas  
        result = True
        
    return result 



def e_silaba_complex_back(string):   
    """
    Receives a string and checks if it is:
    <silaba_final> or
    <silaba><silaba_final> or
    multi <silaba> followed by <silaba_final> 
    """    
    

    
    if e_silaba_final (string):
        result = True
        

    # In summary, this part does the following:
    # tries to find a silaba final and continues from there to see if it the rest of the given string is a silaba or a multi silaba
    # if it's not, it goes back to the silaba final found and adds another character to see if it is a silaba_final
    # and so forth to check if the string given is a silaba + silaba_final or a multi silaba + silaba_final
    
    else:
        
        stringTest = string
        result = False
        count_silaba_final = 0 # variable that lets us know if a silaba final has been found already
        
        stringTestIndex = len(stringTest)-1
        
        
        while stringTestIndex >= 0: # iterates through the given string starting by the last character until it finds a silaba final
            
            if count_silaba_final == 0: 
                            
                stringTestBeginning = stringTest[:stringTestIndex]
                stringTestEnd = stringTest[stringTestIndex:]
                
                if e_silaba(stringTestBeginning) and e_silaba_final (stringTestEnd):
                    result = True
                    break
                
                elif e_silaba(stringTestBeginning) == False and e_silaba_final (stringTestEnd) == True: # checks if a silaba final was found and if that is the case it checks if the rest of the string is a multi silaba
                    count_silaba_final = 1
                    stringSilabas = stringTestBeginning
                    
                    if e_silaba_multi(stringSilabas): # it is here that we check if the rest of the string is a multi silaba and if so the cycle stops
                        result = True
                        break
                    
                    else: # if the rest of the string in analysis is not a multi silaba
                        count_silaba_final = 0 # updates the variable that keeps track that we found a silaba final to zero so that we continue to add characters to the last silaba final found until we find another silaba final to check again if the new rest of the given string is a silaba or a multi silaba
                        
            
            stringTestIndex = stringTestIndex - 1 
            
                 
    return result


def e_palavra(string):
    """
    Receives a string and checks if it is a palavra.
    A string is a palavra if it is:
    <monossilabo> or 
    <silaba_final> or 
    <silaba><silaba_final> or 
    multi <silaba> followed by <silaba_final>
    """          
    
    if not isinstance (string, str):
        raise ValueError ("e_palavra:argumento invalido")
    else:
        return e_monossilabo(string) or e_silaba_complex_back(string)









