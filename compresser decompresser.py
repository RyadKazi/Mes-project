string = str(input("enter anything you want to compress: "))
liste = []
def compresser(chaine_of_characteres):
    count = 0
    precedent = ""
    for actual in chaine_of_characteres:    #checks for the actual caractere in the string
        if precedent == "":
            precedent = actual
            count = 1
        elif actual == precedent:
            count += 1
        else:
            liste.append((count, precedent)) #adds to the list that we've made
            precedent = actual
            count = 1
    if precedent:
        liste.append((count, precedent))
    return liste                            # returns the new list of tuples
result = compresser(chaine_of_characteres=string)
print("Compressed:", result)
def decompresser(liste):
    string = ""
    for (j, k) in liste:                #for each tuple in the list
        string += (j * k)               #constructe a string
    return string
result2 = decompresser(liste=liste)
print(result2)